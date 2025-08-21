from player import Player1, Player2
from draw_a_card import Deck

def main():
    deck = Deck()
    player1 = Player1("P1")
    player2 = Player2("P2")

    while deck.is_deck_not_empty():
        face_value = deck.draw_a_card()

        score1 = player1.random_choice()
        score2 = player2.same_as_face_value(face_value)

        if score1 > score2:
            player1.add_score(face_value)
        elif score1 < score2:
            player2.add_score(face_value)
        else:
            player1.add_score(face_value/2)
            player2.add_score(face_value/2)
        
        print(f"Score of 1: {player1.score}")
        print(f"Score of 2: {player2.score}")
        print("---------------------------------------")
    
    if player1.score > player2.score:
        print("Player 1 wins!")
    elif player1.score < player2.score:
        print("Player 2 wins!")
    else:
        print("Ohhh Noooo its a tie!!!")

if __name__ == "__main__":
    main()
