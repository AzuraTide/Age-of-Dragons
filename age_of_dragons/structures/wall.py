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


def destroy_walls(wall_healths: list[int]) -> list[int]:
    new_wall_healths: list[int] = []
    for wall_health in wall_healths:
        if wall_health > 0:
            new_wall_healths.append(wall_health)
    return new_wall_healths
