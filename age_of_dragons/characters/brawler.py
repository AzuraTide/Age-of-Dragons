class Brawler:
    def __init__(self, name: str, speed: int, strength: int) -> None:
        self.name = name
        self.speed = speed
        self.strength = strength
        self.power = speed * strength


def fight(attacker: Brawler, defender: Brawler) -> None:
    print(f"{attacker.name}: {attacker.power} power")
    print(f"{defender.name}: {defender.power} power")
    if attacker.power > defender.power:
        print(f"{attacker.name} wins!")
    elif attacker.power < defender.power:
        print(f"{defender.name} wins!")
    else:
        print("It's a tie!")
    print("---------------------------------")
