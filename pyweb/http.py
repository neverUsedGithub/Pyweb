from typing import Callable, TypeAlias, TYPE_CHECKING, Protocol, Any
from .html import WebElementChild
from .dom import create_renderer
from .styles import Style
from . import page_info
import uvicorn
import falcon # type: ignore
from falcon.asgi import App # type: ignore
from falcon.asgi.ws import WebSocket # type: ignore
import string
import random
import json

Request: TypeAlias = "falcon.Request"

class RouteHandler(Protocol):
    def __call__(self, request: Request, *params: Any) -> WebElementChild:
        ...

if TYPE_CHECKING:
    from .dom import WebRenderer

def get_random_id() -> str:
    return "".join(
        random.choices(string.ascii_letters + string.digits, k=6)
    )

def get_websocket_script(id: str) -> str:
    return  'window.ws = new WebSocket(window.location.protocol.replace("http", "ws") + "//" + window.location.host + window.location.pathname + "?id=' + id + '");' \
            'ws.addEventListener("message", msg => {' \
            'const index = msg.data.indexOf("$");' \
            'const action = msg.data.substring(0, index);' \
            'const message = msg.data.substring(index + 1);' \
            'if (action === "update") {' \
            'document.body.innerHTML = message;' \
            '}' \
            '});'
            # 'function listenerTrigger(id, event) {' \
            # 'ws.send(`trigger\\$${id}$`)' \
            # '}'

class AppCurrentPage:
    def __init__(self) -> None:
        self.update_callback: Callable[[], None] | None = None
        self.actions: dict[str, Callable[[], None]] = {}
    
    def on_update(self, funct: Callable[[], None]) -> None:
        self.update_callback = funct

    def rerender(self):
        if self.update_callback:
            self.update_callback()

class WebRequestHandler:
    def __init__(self, app: "WebApp", handler: tuple[RouteHandler, list[Style]]) -> None:
        self.app = app
        self.handler = handler[0]
        self.styles = handler[1]
        self.renderers: dict[str, tuple[AppCurrentPage, WebRenderer]] = {}
        self.all_styles = ""

        for style in self.styles:
            self.all_styles += style.style_text

    async def on_websocket(self, req: falcon.Request, socket: WebSocket):
        client_id: str = req.params.get("id") # type: ignore

        if not (pair := self.renderers.get(client_id)):
            return

        await socket.accept()

        page, renderer = pair
        
        last_rendered: str = renderer.render()

        @page.on_update
        def update_page(): # type: ignore
            nonlocal last_rendered

            if not socket.closed:
                new_content = renderer.render()

                if last_rendered != new_content:
                    falcon.get_running_loop().create_task(
                        socket.send_text("update$" + new_content)
                    )

                last_rendered = new_content

        while not socket.closed:
            text = await socket.receive_text()
            if socket.closed: break

            try:
                index = text.index("$")
                action = text[:index]
                args = text[index + 1:].split("$")

                if action == "trigger" and len(args) >= 1:
                    if not (callback := renderer.actions.get(args[0])):
                        break

                    func_args = []
                    if len(args) > 1:
                        func_args = json.loads(args[1])
                    
                    callback(*func_args)
            except Exception as e:
                print("!! EXCEPTION !!", e)
                break
        
        if not socket.closed:
            await socket.close()

    async def on_get(self, req: falcon.Request, res: falcon.Response, **kwargs: Any):
        page = AppCurrentPage()
        page_info.current_page = page

        vdom = self.handler(req, **kwargs)
        renderer = create_renderer(vdom)
        renderer_id = str(id(renderer))

        self.renderers[renderer_id] = (page, renderer)

        res.status = falcon.HTTP_200
        res.content_type = falcon.MEDIA_HTML

        global_styles = "".join(style.style_text for style in self.app.global_styles)

        res.text = \
            f'<html lang="en">' \
            f'<head>' \
            f'<script>{get_websocket_script(renderer_id)}</script>' \
            f'<style>{global_styles}{self.all_styles}</style>' \
            f'</head>' \
            f'<body>' \
            f'{renderer.render()}' \
            f'</body>' \
            f'</html>'

class WebApp:
    def __init__(self):
        self.pages: dict[str, tuple[RouteHandler, list[Style]]] = {}
        self.global_styles: list[Style] = []

    def add_global(self, style: Style):
        self.global_styles.append(style)

    def page(self, route: str, uses: list[Style] = []): # type: ignore
        def wrapper(func: Callable[..., WebElementChild]):
            self.pages[route] = [func, uses] # type: ignore

        return wrapper # type: ignore

    def listen(self, port: int, host: str = "localhost"):
        app = App()

        for route in self.pages:
            app.add_route(route, WebRequestHandler(self, self.pages[route])) # type: ignore

        # app.add_error_handler(Exception, TestHandler().handle)

        uvicorn.run( # type: ignore
            app,
            host=host,
            port=port,
            # log_level="debug"
        )

def create_app():
    return WebApp()
