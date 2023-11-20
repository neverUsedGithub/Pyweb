from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .http import AppCurrentPage

current_page: "AppCurrentPage | None" = None