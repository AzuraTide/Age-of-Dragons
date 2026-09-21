from .archer import Archer
from .human import Human

class Crossbowman(Archer):
    def __init__(self,  name: str, pos_x: int, pos_y: int, speed: int, stamina: int, health: int, num_arrows: int) -> None:
        super().__init__(name, pos_x, pos_y, speed, stamina, health, num_arrows)

    def triple_shot(self, target: Human) -> str:
        self.use_arrows(3)
        target_name = target.get_name()
        return f"{target_name} was shot by 3 crossbow bolts"
