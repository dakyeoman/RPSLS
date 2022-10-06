from RPSLS_game import RPSLS_game
from RPSLS_player import RPSLS_player
import random

competitor = []
result_lst = []
result_num = len(result_lst)
comp_num = len(competitor)


class P17773(RPSLS_player, RPSLS_game):
    def __init__(self):
        pass
    # p1_shoot in RPSLS_game.py

    def shoot(self):
        options = ["rock", "scissors", "paper", "lizard", "spock"]
        # 1st game
        if result_num == 0:
            choice = str(random.choice(options))
            return choice
        for i in competitor:
            try:
                if result_lst[i] == "win":
                    if competitor[i] == "scissors":
                        return "rock"
                    elif competitor[i] == "paper":
                        return "scissors"
                    elif competitor[i] == "rock":
                        return "paper"
                    elif competitor[i] == "spock":
                        return "lizard"
                    else:
                        # competitor[i] == "scissors":
                        return "spock"

                elif result_lst[i] == "lose":
                    if competitor[i] == "scissors":
                        return "rock"
                    elif competitor[i] == "paper":
                        return "scissors"
                    elif competitor[i] == "rock":
                        return "paper"
                    elif competitor[i] == "spock":
                        return "lizard"
                    else:  # competitor[i] == "scissors":
                        return "spock"
                else:  # draw
                    choice = str(random.choice(options))
                    return choice

            except:
                choice = str(random.choice(options))
                return choice

    def update(self, result: str, competitor_shot: str):
        competitor.append(competitor_shot)
        # result_lst.append(result)
        #print(competitor, "and", result_lst, result_lst.count("win")/5)
