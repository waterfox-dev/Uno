from enum import Enum
from data.cardConfig import simple_game

import random

class CardPackage:

    def __init__(self):
        self.all_cards = simple_game

    def random_card(self):
        element = random.choice(self.all_cards)
        self.all_cards.remove(element)
        return element
    
    def distribute_card(self):
        main = []
        for i in range(6):
            main.append(self.random_card())
        return main
    