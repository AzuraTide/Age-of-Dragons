class Rectangle:
    def __init__(self, length: int, width: int) -> None:
        self.__length = length
        self.__width = width

    def get_area(self) -> int:
        return self.__length * self.__width

    def get_perimeter(self) -> int:
        return 2 * (self.__length + self.__width)


