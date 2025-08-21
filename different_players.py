import random

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