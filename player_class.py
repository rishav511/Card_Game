class Player:
    def __init__(self, name):
        self.name = name
        self.options = list(range(1, 14))   
        self.seen_cards = []                
        self.opp_cards = {}                 
        self.score = 0

    def update_seen(self, card):
        self.seen_cards.append(card)

    def update_opponent(self, opp_name, card_played):
        if opp_name not in self.opp_cards:
            self.opp_cards[opp_name] = []
        self.opp_cards[opp_name].append(card_played)

    def play(self, face_value):
        raise NotImplementedError

    def add_score(self, points):
        self.score += points