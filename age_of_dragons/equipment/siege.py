class Siege:
    def __init__(self, max_speed: int, efficiency: int) -> None:
        self.max_speed = max_speed
        self.efficiency = efficiency

    def get_trip_cost(self, distance: int, food_price: int) -> float:
        return (distance / self.efficiency) * food_price

    def get_cargo_volume(self) -> float | None:
        pass