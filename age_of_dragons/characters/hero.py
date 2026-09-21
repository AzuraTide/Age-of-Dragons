class Hero:
    def __init__(self, name: str, health: int) -> None:
        self.__name = name
        self.__health = health

    def get_name(self) -> str:
        return self.__name

    def get_health(self) -> int:
        return self.__health

    def take_damage(self, damage: int) -> None:
        self.__health -= damage
