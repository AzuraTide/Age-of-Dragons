from .unit import Unit

class Dragon(Unit):
    def __init__(self, name: str, pos_x: int, pos_y: int, fire_range: int, element="fire") -> None:
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range
        self.element = element

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
