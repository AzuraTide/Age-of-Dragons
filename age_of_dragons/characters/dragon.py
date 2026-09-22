from .unit import Unit
from age_of_dragons.shapes.rectangle import Rectangle

class Dragon(Unit):
    def __init__(self, name: str, pos_x: int, pos_y: int, height: int, width: int, 
                 fire_range: int, element="fire", color="red") -> None:
        super().__init__(name, pos_x, pos_y)
        self.height = height
        self.width = width
        self.__fire_range = fire_range
        self.__hit_box = Rectangle(pos_x - self.width / 2, pos_y - self.height / 2,
                                   pos_x + self.width / 2, pos_y + self.height / 2)
        self.element = element
        self.color = color

    def __str__(self) -> str:
        return f"I am {self.name}, the {self.color} dragon"

    def in_area(self, x1: float, y1: float, x2: float, y2: float) -> bool:
        area = Rectangle(x1, y1, x2, y2)
        return self.__hit_box.overlaps(area)

    def breathe_fire(self, x: int, y: int, units: list[Unit]) -> list[Unit]:
        print("====================================")
        print(f"{self.name} breathes fire at {x}/{y} with range {self.__fire_range}")
        print("------------------------------------")
        hit_by_blast: list[Unit] = []
        for unit in units:
            in_area = unit.in_area(
                x - self.__fire_range,
                y - self.__fire_range,
                x + self.__fire_range,
                y + self.__fire_range,
            )
            if in_area:
                hit_by_blast.append(unit)
                print(f"{unit.name} is hit by the fire")
        return hit_by_blast

    def get_breath_damage(self) -> int:
        if self.element == "fire":
            return 300
        if self.element == "ice":
            return 150
        return 0
