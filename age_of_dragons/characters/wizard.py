from .hero import Hero

class Wizard(Hero):
    def __init__(self, name: str, health: int, intelligence: int, mana: int, stamina: int) -> None:
        super().__init__(name, health)
        self.__intelligence = intelligence
        self.__mana = mana
        self.__stamina = stamina

    def cast_fireball(
        self, target: "Wizard", fireball_cost: int, fireball_damage: int
    ) -> None:
        if self.__mana < fireball_cost:
            raise Exception(f"{self.get_name()} cannot cast fireball")
        else:
            self.__mana -= fireball_cost
            target.get_fireballed(fireball_damage)

    def is_alive(self) -> bool:
        return self.get_health() > 0

    def get_fireballed(self, fireball_damage: int) -> None:
        fireball_damage -= self.__stamina
        self.take_damage(fireball_damage)

    def drink_mana_potion(self, potion_mana: int) -> None:
        potion_mana += self.__intelligence
        self.__mana += potion_mana
