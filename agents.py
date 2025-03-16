#pip install -U mesa
#pip install -U mesa[rec]

import mesa

import random

class PlayerAgent(mesa.Agent):
    def __init__(self, unique_id, model, startingX, startingY, occupation, isJackOfHeart):
        super().__init__(unique_id, model)
        self.startingX = startingX
        self.startingY = startingY

        self.occupation = occupation
        self.suit = random.choice(["Hearts", "Diamonds", "Clubs", "Spades"])
        self.strategy = random.choice(["Truthful", "Deceptive", "Random"])
        self.suitGuess = ""
        self.trustLevelsHashMap = {}
        self.sleepDeprived = 0
        
        self.isJackOfHeart = isJackOfHeart
