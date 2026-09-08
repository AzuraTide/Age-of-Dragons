Soldier = dict[str, int]

class Wall:
    armor: int = 10
    height: int = 5

    def __init__(self, depth: int, height: int, width: int) -> None:
        self.depth = depth
        self.height = height
        self.width = width
        self.volume = depth * height * width


    def fortify(self) -> None:
        self.armor *= 2

    def get_cost(self) -> int:
        return self.armor * self.height


class BatteringRam:
    damage: int = 2
    length: int = 4

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

class Archer:
    name: str
    health: int
    num_arrows: int

    def __init__(self, name: str, health: int, num_arrows: int) -> None:
        self.name = name
        self.health = health
        self.num_arrows = num_arrows

    def take_hit(self) -> None:
        self.health -= 1
        if self.health <= 0:
            raise Exception(f"{self.name} is dead")

    def shoot(self, target: "Archer") -> None:
        if self.num_arrows <= 0:
            raise Exception(f"{self.name} can't shoot")
        else:
            self.num_arrows -= 1
        print(f"{self.name} shoots {target.name}")
        target.take_hit()
    # don't touch below this line

    def get_status(self) -> tuple[str, int, int]:
        return self.name, self.health, self.num_arrows

    def print_status(self) -> None:
        print(f"{self.name} has {self.health} health and {self.num_arrows} arrows")

class Dragon:

    def __init__(self, element: str) -> None:
        self.element = element

    def get_breath_damage(self) -> int:
        if self.element == "fire":
            return 300
        if self.element == "ice":
            return 150
        return 0

class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author


class Library:
    def __init__(self, name: str) -> None:
        self.name = name
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, book: Book) -> None:
        new_books: list[Book] = []
        for lib_book in self.books:
            if lib_book.title != book.title or lib_book.author != book.author:
                new_books.append(lib_book)
        self.books = new_books

    def search_books(self, search_string: str) -> list[Book]:
        results: list[Book] = []
        for book in self.books:
            if (
                search_string.lower() in book.title.lower()
                or search_string.lower() in book.author.lower()
            ):
                results.append(book)
        return results

def destroy_walls(wall_healths: list[int]) -> list[int]:
    new_wall_healths: list[int] = []
    for wall_health in wall_healths:
        if wall_health > 0:
            new_wall_healths.append(wall_health)
    return new_wall_healths

class Wizard:
    def __init__(self, name: str, stamina: int, intelligence: int) -> None:
        self.name = name
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.mana = self.__intelligence * 10
        self.health = self.__stamina * 100

    def cast_fireball(
        self, target: "Wizard", fireball_cost: int, fireball_damage: int
    ) -> None:
        if self.mana < fireball_cost:
            raise Exception(f"{self.name} cannot cast fireball")
        else:
            self.mana -= fireball_cost
            target.get_fireballed(fireball_damage)

    def is_alive(self) -> bool:
        return self.health > 0

    def get_fireballed(self, fireball_damage: int) -> None:
        fireball_damage -= self.__stamina
        self.health -= fireball_damage

    def drink_mana_potion(self, potion_mana: int) -> None:
        potion_mana += self.__intelligence
        self.mana += potion_mana


class BankAccount:
    def __init__(self, account_number: str, initial_balance: float) -> None:
        self.__account_number = account_number
        self.__balance = initial_balance

    def get_account_number(self) -> str:
        return self.__account_number

    def get_balance(self) -> float:
        return self.__balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("cannot deposit zero or negative funds")
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("cannot withdraw zero or negative funds")
        if self.__balance < amount:
            raise ValueError("insufficient funds")
        self.__balance -= amount


def fight_soldiers(soldier_one: Soldier, soldier_two: Soldier) -> str:
    soldier_one_dps = get_soldier_dps(soldier_one)
    soldier_two_dps = get_soldier_dps(soldier_two)
    if soldier_one_dps > soldier_two_dps:
        return "soldier 1 wins"
    if soldier_two_dps > soldier_one_dps:
        return "soldier 2 wins"
    return "both soldiers die"


def get_soldier_dps(soldier: Soldier) -> int:
    return soldier["damage"] * soldier["attacks_per_second"]


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


def main() -> None:
    aragorn: Brawler = Brawler("Aragorn", 4, 4)
    gimli: Brawler = Brawler("Gimli", 2, 7)
    legolas: Brawler = Brawler("Legolas", 7, 7)
    frodo: Brawler = Brawler("Frodo", 3, 2)

    fight(aragorn, gimli)
    fight(legolas, frodo)