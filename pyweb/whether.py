from typing import TypeVar, Callable
from .signals import Signal
from .refs import Ref
from .html import WebElementChild

T = TypeVar("T")

def whether(
    condition: bool | Signal[bool] | Ref[bool] | Callable[..., bool],
    truthy: Callable[[], WebElementChild],
    falsy: Callable[[], WebElementChild] | None = None,
) -> Callable[[], WebElementChild]:
    def inner():
        if isinstance(condition, Signal) or isinstance(condition, Ref):
            if condition.get(): return truthy()
        elif callable(condition):
            if condition(): return truthy()
        else:
            if condition: return truthy()
        
        if falsy: return falsy()
        return None
    
    return inner