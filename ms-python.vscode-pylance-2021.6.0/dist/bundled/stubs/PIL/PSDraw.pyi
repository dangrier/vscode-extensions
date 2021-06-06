# pyright: strict

from PIL.Image import Image
from typing import Any, IO, Optional, Tuple


class PSDraw:
    def __init__(self, fp: Optional[IO[Any]]) -> None: ...

    def begin_document(self, id: Optional[Any] = ...) -> None: ...

    def end_document(self) -> None: ...

    def image(self, box: Tuple[int, int, int, int], im: Image, dpi: Optional[float] = ...) -> None: ...

    def line(self, xy0: Tuple[int, int], xy1: Tuple[int, int]) -> None: ...

    def rectangle(self, box: Tuple[int, int, int, int]) -> None: ...

    def setfont(self, font: str, size: int) -> None: ...

    def text(self, xy: Tuple[int, int], text: str) -> None: ...
