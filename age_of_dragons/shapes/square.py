from .rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, x1, y1, length: int) -> None:
        super().__init__(x1, y1, x1 + length, y1 + length)