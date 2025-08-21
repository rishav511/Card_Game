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

