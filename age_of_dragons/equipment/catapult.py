from .siege import Siege

class Catapult(Siege):
    def __init__(self, max_speed: int, efficiency: int, cargo_volume: int) -> None:
        super().__init__(max_speed, efficiency)
        self.cargo_volume = cargo_volume

    def get_cargo_volume(self) -> int:
        return self.cargo_volume