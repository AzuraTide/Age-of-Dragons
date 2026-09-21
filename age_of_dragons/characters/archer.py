from .human import Human

class Archer(Human):
    name: str
    health: int
    num_arrows: int

    def __init__(self, name: str, pos_x: int, pos_y: int, speed: int, stamina: int, health: int, num_arrows: int) -> None:
        super().__init__(name, pos_x, pos_y, speed, stamina)
        self.health = health
        self.__num_arrows = num_arrows

    def take_hit(self) -> None:
        self.health -= 1
        if self.health <= 0:
            raise Exception(f"{self.get_name()} is dead")

    def shoot(self, target: "Archer") -> None:
        if self.__num_arrows <= 0:
            raise Exception(f"{self.get_name()} can't shoot")
        else:
            self.__num_arrows -= 1
        print(f"{self.get_name()} shoots {target.get_name()}")
        target.take_hit()

    def get_status(self) -> tuple[str, int, int]:
        return self.get_name(), self.health, self.__num_arrows

    def print_status(self) -> None:
        print(f"{self.get_name()} has {self.health} health and {self.__num_arrows} arrows")

    def get_num_arrows(self) -> int:
        return self.__num_arrows

    def use_arrows(self, num: int) -> None:
        if self.__num_arrows < num:
            raise Exception("not enough arrows")
        self.__num_arrows -= num
