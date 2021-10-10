from player import Player
from cards import CardPackage
from utils.logger import Logger
from rules import Rules

import random

class Game:

    def __init__(self, player_list : list):

        self.player_list    = player_list
        self.player_objects = []
        self.game_package   = CardPackage()
        self.round          = 0

        random.shuffle(player_list)

        for i in range(len(self.player_list)):
            self.player_objects.append(Player(self.player_list[i], i, self.game_package.distribute_card()))

    def start_game(self):
        self.card = self.game_package.random_card()

    def next_round(self):
        self.round += 1
        Logger.log("Round", f"Round {self.round} has been started")
    
    def player_action(self, player_card : tuple):
        if Rules.can_pose(self.card, self.player_action):
            self.card = player_card
