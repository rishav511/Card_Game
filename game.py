from player import Player1, Player2, Player3
from draw_a_card import Deck

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player1 = Player1("P1")
        self.player2 = Player2("P2")
        self.player3 = Player3("P3")

    def play(self):
        while self.deck.is_deck_not_empty():
            face_value = self.deck.draw_a_card()

            # Example scoring logic (uncomment & modify as needed)
            # score1 = self.player1.random_choice()
            # score2 = self.player2.same_as_face_value(face_value)

            # if score1 > score2:
            #     self.player1.add_score(face_value)
            # elif score1 < score2:
            #     self.player2.add_score(face_value)
            # else:
            #     self.player1.add_score(face_value / 2)
            #     self.player2.add_score(face_value / 2)

            # print(f"Score of 1: {self.player1.score}")
            # print(f"Score of 2: {self.player2.score}")
            # print("---------------------------------------")

        self.declare_winner()

    def declare_winner(self):
        if self.player1.score > self.player2.score:
            print("Player 1 wins!")
        elif self.player1.score < self.player2.score:
            print("Player 2 wins!")
        else:
            print("Ohhh Noooo its a tie!!!")


if __name__ == "__main__":
    game = Game()
    game.play()
