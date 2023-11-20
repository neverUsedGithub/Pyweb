from typing import TypeVar, Callable
from .signals import Signal
from .refs import Ref
from .html import WebElementChild
from inspect import signature

T = TypeVar("T")

def each(
    items: Signal[list[T]] | Ref[list[T]],
    mapper: Callable[[T], WebElementChild] | Callable[[T, int], WebElementChild]
) -> Callable[[], WebElementChild]:
    last_items: list[T] | None = None
    last_rendered: tuple[WebElementChild] | None = None
    is_single_param = len(signature(mapper).parameters) == 1

    def wrapper():
        nonlocal last_items
        nonlocal last_rendered

        if last_items is not None and id(last_items) == id(items.get()):
            return last_rendered
        
        last_items = items.get()

        if is_single_param:
            return (last_rendered := tuple(mapper(item) for item in items.get())) # type: ignore
        
        return (last_rendered := tuple(mapper(item, i) for i, item in enumerate(items.get()))) # type: ignore
    
    return wrapper
