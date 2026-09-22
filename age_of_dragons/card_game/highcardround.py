from .round import Round
from .card import Card

class HighCardRound(Round):
    def __init__(self, card1: Card, card2: Card) -> None:
        self.card1 = card1
        self.card2 = card2

    def resolve_round(self) -> int:
        if self.card1 > self.card2:
            return 1
        elif self.card2 > self.card1:
            return 2
        else:
            return 0