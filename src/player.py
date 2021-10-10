class Player:
    
    def __init__(self, name : str, pos : str, cards : list):
        self.name = name 
        self.pos = pos
        self.cards = cards
    
    def __str__(self):
        return f'name : {self.name}\npos : {self.pos}\ncards : {self.cards}'
        