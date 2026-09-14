from age_of_dragons.characters.brawler import Brawler, fight


def main() -> None:
    aragorn: Brawler = Brawler("Aragorn", 4, 4)
    gimli: Brawler = Brawler("Gimli", 2, 7)
    legolas: Brawler = Brawler("Legolas", 7, 7)
    frodo: Brawler = Brawler("Frodo", 3, 2)

    fight(aragorn, gimli)
    fight(legolas, frodo)
