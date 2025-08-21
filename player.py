import random
from abc import ABC, abstractmethod

class Player:    
    def __init__(self, name):
        self.name = name
        self.options = list(range(1, 14))
        self.score = 0

    def random_choice(self):
        choice = random.choice(self.options)
        self.options.remove(choice)
        
        return choice
    
    def same_as_face_value(self, face_value):
        if face_value in self.options:
            self.options.remove(face_value)
            
        return face_value 

    def add_score(self, points):
        self.score += points
    
    @abstractmethod
    def make_choice(self, **kwargs):
        pass

class Player1(Player):
    def __init__(self, name):
        super().__init__(name)

    def make_choice(self):
        choice = random.choice(self.options)
        self.options.remove(choice)
        
        return choice

class Player2(Player):
    def __init__(self, name):
        super().__init__(name)

    def make_choice(self, face_value):
        if face_value in self.options:
            self.options.remove(face_value)
            
        return face_value 

class Player3(Player):
    def __init__(self, name):
        super().__init__(name)
        self.memory = []

    def make_choice(self, face_value):
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
            if 13 in self.memory:
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

    def add_memory(self, card):
        self.memory.append(card)