from .rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, length: int) -> None:
        super().__init__(length, length)