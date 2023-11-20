from . import page_info
from typing import TypeVar, Generic, Callable

T = TypeVar("T")
class Signal(Generic[T]):
    def __init__(self, initial: T) -> None:
        self.value = initial

        if not page_info.current_page:
            raise Exception("Signals should only be used inside a page handler.")
        
        self.page = page_info.current_page

    def __call__(self, new_value: Callable[[T], T]) -> None:
        old_value = self.value
        self.value = new_value(self.value)

        if old_value != self.value:
            self.page.rerender()

    def like(self, transformer: Callable[[T], T]) -> Callable[..., T]:
        return lambda: transformer(self.value)
    
    def get(self) -> T:
        return self.value

U = TypeVar("U")
def signal(initial: U) -> Signal[U]:
    return Signal(initial)