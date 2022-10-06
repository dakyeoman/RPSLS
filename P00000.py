from RPSLS_player import RPSLS_player
import random


class P00000(RPSLS_player):
    def __init__(self):
        pass

    def shoot(self):
        options = ["rock", "scissors", "paper", "lizard", "spock"]
        choice = str(random.choice(options))
        return choice

    def update(self, result: str, competitor_shot: str):
        pass
