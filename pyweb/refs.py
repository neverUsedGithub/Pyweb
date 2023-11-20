from . import page_info
from typing import TypeVar, Generic, Callable

T = TypeVar("T")
class Ref(Generic[T]):
    def __init__(self, initial: T) -> None:
        self.value = initial

        if not page_info.current_page:
            raise Exception("Refs should only be used inside a page handler.")

    def __call__(self, new_value: Callable[[T], T]) -> None:
        self.value = new_value(self.value)

    def like(self, transformer: Callable[[T], T]) -> Callable[..., T]:
        return lambda: transformer(self.value)
    
    def get(self) -> T:
        return self.value

U = TypeVar("U")
def ref(initial: U) -> Ref[U]:
    return Ref(initial)