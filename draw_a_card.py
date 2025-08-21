import random 

def is_deck_not_empty(deck: list[int]) -> bool :
    return len(deck) != 0

def draw_a_card(deck: list[int]) -> int:
    print (deck.pop(0))

def main():
    deck = deck = list(range(1,14))
    random.shuffle(deck)
    while is_deck_not_empty(deck):
        draw_a_card((deck))

if __name__ == "__main__":
    main()

