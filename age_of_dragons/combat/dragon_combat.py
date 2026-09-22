from age_of_dragons.characters.dragon import Dragon

def main() -> None:
    dragons = [
        Dragon("Green Dragon", 0, 0, 10, 10, 1),
        Dragon("Red Dragon", 2, 2, 0, 10, 2),
        Dragon("Blue Dragon", 4, 3, 10, 10, 3),
        Dragon("Black Dragon", 5, -1, 10, 10, 4),
    ]

    for dragon in dragons:
        describe(dragon)

    for dragon_index in range(len(dragons)):
        enemy_dragons: list[Dragon] = dragons.copy()
        dragon: Dragon = dragons[dragon_index]
        del enemy_dragons[dragon_index]
        dragon.breathe_fire(3, 3, enemy_dragons)

def describe(dragon: "Dragon") -> None:
    print(f"{dragon.name} is at {dragon.pos_x}/{dragon.pos_y}")

if __name__ == "__main__":
    main()