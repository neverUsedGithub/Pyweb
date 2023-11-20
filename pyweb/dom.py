from .html import WebElement, WebElementChild
from typing import Callable
from .signals import Signal
from .styles import Style
from .refs import Ref

class WebRenderer:
    def __init__(self, element: WebElementChild) -> None:
        self.root = element
        self.actions: dict[str, Callable[..., None]] = {}

    def render_element_to_string(self, element: WebElementChild) -> str:
        if element == None:
            return ""

        if isinstance(element, Signal) or isinstance(element, Ref):
            return self.render_element_to_string(element.get())
        
        if callable(element):
            return self.render_element_to_string(element())
        
        if type(element) == int:
            return str(element)
        
        if type(element) == str:
            return element
        
        if type(element) == tuple:
            return "".join(self.render_element_to_string(child) for child in element)
        
        if type(element) == WebElement:
            concat = f"<{element.type}"
            for attr, val in element.attributes.items():
                if attr == "class_name": attr = "class"

                if isinstance(val, Style):
                    concat += f" {attr}={val.class_name}"
                    
                    if val.class_name is None:
                        raise Exception("Don't global_style in class_name attributes.")
                elif callable(val):
                    attribute_id = str(id(element)) + "@" + attr

                    if not self.actions.get(attribute_id):
                        self.actions[attribute_id] = val

                    if attr == "oninput":
                        concat += f' {attr}="ws.send(\'trigger${attribute_id}$\'+JSON.stringify([ event.target.value ]))"'
                    elif attr == "onchecked":
                        concat += f' onchange="ws.send(\'trigger${attribute_id}$\'+JSON.stringify([ event.target.checked ]))"'
                    else:
                        concat += f' {attr}="ws.send(\'trigger${attribute_id}\')"'
                elif type(val) == str:
                    concat += f" {attr}={val}"
                elif type(val) == bool:
                    concat += f" {attr}" if val else ""
                else:
                    raise Exception("Invalid attribute value.")
                
            concat += ">"

            for child in element.children:
                concat += self.render_element_to_string(child)
            concat += f"</{element.type}>"

            return concat
        
        raise Exception("Found invalid child when rendering.")

    def render(self):
        self.actions = {}
        return self.render_element_to_string(self.root)

def create_renderer(element: WebElementChild):
    return WebRenderer(element)