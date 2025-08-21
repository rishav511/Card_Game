import random

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