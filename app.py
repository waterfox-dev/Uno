from src.game import Game
from src.utils.logger import Logger

import ast

gameInstance = Game(['Clément', 'Félix'])
gameInstance.start_game()

for i in range(25):
    gameInstance.next_round()
    for element in gameInstance.player_objects :
        round = True
        while round :
            Logger.log("Jeu", gameInstance.card)
            accept = False
            Logger.log("Main", element.cards)
            while not accept :
                card = ast.literal_eval(input('Card ->'))
                if card in element.cards :
                    accept = True
                else:
                    print("You not got this card")

            if gameInstance.player_action(card) :
                element.cards.remove(card)
                round = False       
            else :
                new_card = input("You can't pose this card, take a new card ?")     
                if new_card == 'Y':
                    element.cards.append(gameInstance.game_package.random_card())
                else:
                    pass