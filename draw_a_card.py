import random 
class Deck:
    def __init__(self):
        self.deck = list(range(1, 14))
        random.shuffle(self.deck)

    def is_deck_not_empty(self) -> bool:
        return len(self.deck) != 0

    def draw_a_card(self) -> int:
        if self.is_deck_not_empty():
            card = self.deck.pop(0)
            print(f"Card drawn: {card}")
            return card
        else:
            print("Deck is empty.")
            return -1