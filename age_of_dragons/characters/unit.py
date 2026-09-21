class Unit:
    def __init__(self, name: str, pos_x: int, pos_y: int) -> None:
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1: int, y_1: int, x_2: int, y_2: int) -> bool:
        return (
            self.pos_x >= x_1
            and self.pos_x <= x_2
            and self.pos_y >= y_1
            and self.pos_y <= y_2
        )