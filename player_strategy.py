import random
from player_class import Player

class RandomPlayer(Player):
    def play(self, face_value):
        choice = random.choice(self.options)
        self.options.remove(choice)
        return choice


class FaceValuePlayer(Player):
    def play(self, face_value):
        if face_value in self.options:
            self.options.remove(face_value)
            return face_value
        choice = min(self.options)
        self.options.remove(choice)
        return choice


class StrategicPlayer(Player):
    def play(self, face_value):
        higher_cards = [c for c in self.options if c > face_value]
        if higher_cards:
            choice = min(higher_cards)  
        else:
            choice = min(self.options)  
        self.options.remove(choice)
        return choice


class OpponentAwarePlayer(Player):
    def play(self, face_value):
        
        if face_value > 7:
            higher_cards = [c for c in self.options if c > face_value]
            if higher_cards:
                bid = min(higher_cards)
            else:
                bid = min(self.options)
        else:
            bid = min(self.options)

        
        all_opp_cards = [c for cards in self.opp_cards.values() for c in cards]
        if all(c <= face_value for c in all_opp_cards) and self.options:
            bid = min([c for c in self.options if c >= face_value] or [min(self.options)])

        self.options.remove(bid)
        return bid

class OpponentAwareStrategicPlayer(Player):
    def play(self, face_value):
        if not self.options:
            return None

        if face_value < 7:
            options = [c for c in self.options if c < face_value or (face_value < c <= face_value + 2)]

        elif face_value == 7:
            options = [c for c in self.options if c in [8, 9] or c < 7]

        elif face_value == 8:
            options = [c for c in self.options if c in [9, 10, 11]]

        elif face_value == 9:
            options = [c for c in self.options if c in [10, 11]]

        elif face_value == 10:
            options = [c for c in self.options if c in [10, 11, 12]]

        elif face_value == 11:
            options = [c for c in self.options if c in [11, 12, 13]]

        elif face_value == 13:
            if 13 in self.opp_cards.values():
                if 13 in self.options:
                    return 13
                else:
                    options = self.options
            else:
                options = [c for c in self.options if c != 13]
                if not options:
                    options = self.options

        else:
            options = self.options

        if not options:
            return random.choice(self.options)

        choice = max(options)
        self.options.remove(choice)
        return choice


class UserPlayer(Player):
    def play(self, face_value):
        print(f"{self.name}, your available cards: {self.options}")
        while True:
            try:
                choice = int(input(f"Enter your bid for face card {face_value}: "))
                if choice in self.options:
                    self.options.remove(choice)
                    return choice
                else:
                    print("Invalid choice! Pick from your available cards.")
            except ValueError:
                print("Please enter a number!")