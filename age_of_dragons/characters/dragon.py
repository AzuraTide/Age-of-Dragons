class Dragon:

    def __init__(self, element: str) -> None:
        self.element = element

    def get_breath_damage(self) -> int:
        if self.element == "fire":
            return 300
        if self.element == "ice":
            return 150
        return 0
