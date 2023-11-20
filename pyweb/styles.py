from typing import TypeAlias
from .signals import Signal
from .refs import Ref

StylesheetValue: TypeAlias = "None | str | int | Signal[StylesheetValue] | Ref[StylesheetValue] | list[StylesheetValue] | Stylesheet"
Stylesheet: TypeAlias = "dict[str, StylesheetValue]"

def stylesheet_value_to_string(value: StylesheetValue) -> str:
    if isinstance(value, Signal) or isinstance(value, Ref):
        return stylesheet_value_to_string(value.get())
    
    if value is None:
        return "none"
    
    if type(value) == int:
        return f"{value}px"
    
    if type(value) == str:
        return value
    
    if type(value) == list:
        return " ".join(stylesheet_value_to_string(val) for val in value)
    
    raise Exception(f"Invalid stylesheet value: {value}")

def stylesheet_to_string(stylesheet: Stylesheet, parent: str) -> str:
    text = parent + "{"

    for k, v in stylesheet.items():
        if type(v) == dict:
            text = stylesheet_to_string(v, parent + k) + text
        else:
            text += f"{k}: {stylesheet_value_to_string(v)};"

    return text + "}"

class Style:
    def __init__(
        self,
        stylesheet: Stylesheet,
        is_global: bool = False
    ) -> None:
        self.raw = stylesheet
        self.class_name = None

        if not is_global:
            self.class_name = "style-" + str(id(self))
            self.style_text = stylesheet_to_string(
                stylesheet,
                f".{self.class_name}"
            )
        else:
            self.style_text = stylesheet_to_string(stylesheet, "")

    def add(self, *styles: "Style") -> "Style":
        combined = { **self.raw }
        for style in styles: combined.update(style.raw)
        return Style(combined)
    
    @staticmethod
    def combine(*styles: "Style") -> "Style":
        combined: Stylesheet = {}
        for style in styles: combined.update(style.raw)
        return Style(combined)

def style(stylesheet: Stylesheet) -> Style:
    return Style(stylesheet)

def global_style(stylesheet: Stylesheet) -> Style:
    return Style(stylesheet, is_global=True)
