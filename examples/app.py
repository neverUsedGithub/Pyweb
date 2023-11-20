from dataclasses import dataclass
import pyweb.html as html
from pyweb.http import create_app, Request
from pyweb.signals import signal
from pyweb.each import each
from pyweb.whether import whether
from pyweb.styles import style, global_style

app = create_app()

app.add_global(global_style({
    "*": {
        "font-family": "Seravek, 'Gill Sans Nova', Ubuntu, Calibri, 'DejaVu Sans', source-sans-pro, sans-serif"
    }
}))

@app.page("/")
def home_page(request: Request):
    count = signal(0)

    def clicked():
        count(lambda count: count + 1)

    return (
        html.div(
            html.h1("Hello, World!"),
            html.h3("The count is ", count),
            html.h3("The count doubled is ", count.like(lambda count: count * 2)),

            whether(
                lambda: count.get() > 5,
                lambda: (
                    html.h1("The count is more than 5!")
                )
            ),

            html.button(
                "Click me!",
                onclick=clicked
            ),

            html.h3("Try out some other things:"),
            html.ul(
                html.li(html.a("greeter", href="/greet/Python")),
                html.li(html.a("todo app", href="/todos"))
            ),
        )
    )

@app.page("/greet/{name}")
def user_page(request: Request, name: str):
    return (
        html.h1(f"Hello, {name}!")
    )

@dataclass
class Todo:
    text: str
    done: bool

button_style = style({
    "padding": [ 4, 6 ],
    "background": "rgb(200, 200, 200)",
    "border": None,
    "cursor": "pointer",
    "transition": ".2s",

    ":hover": {
        "background": "rgb(230, 230, 230)"
    }
})

@app.page(
    "/todos",
    uses = [ button_style ]
)
def todo_page(request: Request):
    todos = signal([
        Todo("some", False),
        Todo("example", True),
        Todo("todos", False)
    ])
    text = signal("")

    def oninput(new_text: str):
        text(lambda _: new_text)

    def add_todo():
        if text.get() != "":
            todos(lambda todos: [ *todos, Todo(text.get(), False) ])
            text(lambda _: "")

    def todo_update(id: int, checked: bool):
        todo_items = todos.get()
        todo_items[id].done = checked
        todos(lambda _: todo_items)

    def remove_done():
        todos(lambda todos: list(todo for todo in todos if not todo.done))

    return (
        html.h1("Todo App"),

        whether(
            lambda: len(todos.get()) == 0,
            lambda: html.h3("No todos!")
        ),

        each(todos, lambda todo, index: (
            html.div(
                html.input(
                    type="checkbox",
                    checked=todo.done,
                    onchecked=lambda new: todo_update(index, new)
                ),
                html.span(todo.text)
            )
        )),

        html.input(oninput=oninput),
        html.button(
            "Add Todo",
            onclick=add_todo,
            class_name=button_style
        ),
        html.button(
            "Remove Done",
            onclick=remove_done,
            class_name=button_style
        ),
    )

app.listen(3000)