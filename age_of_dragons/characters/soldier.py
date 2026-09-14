class Soldier:
    def __init__(self, name: str, armor: int, num_weapons: int) -> None:
        self.name = name
        self.armor = armor
        self.num_weapons = num_weapons

    def get_speed(self) -> int:
        speed = 10
        speed -= self.armor
        speed -= self.num_weapons
        return speed
