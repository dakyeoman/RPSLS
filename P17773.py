from RPSLS_game import RPSLS_game
from RPSLS_player import RPSLS_player
import random

competitor = ""
result_lst = []
result_num = len(result_lst)
comp_num = len(competitor)
repeat = 5


class P17773(RPSLS_player, RPSLS_game):

    def __init__(self):
        pass

# p1_shoot in RPSLS_game.py
    def shoot(self):
        if result_num == 0:
            beat = {"rock": "paper", "paper": "scissors", "scissors": "rock", "paper": "scissors", "spock": "lizard",
                    "scissors": "spock", "lizard": "rock", "lizard": "scissors", "spock": "paper", "paper": "lizard", "rock": "spock"}
            not_lose = {"rock": "PPR", "paper": "SSP", "scissors": "RRS",
                        "spock": "PPK", "lizard": "SSL"}
            my_lst = ""
            comp_lst = ""
            history = ""
            RPSLS = ["rock", "paper", "scissors",
                     "spock", "lizard"]  # Spock = k
            list_predictor = [""]*repeat
            length = 0

            temp1 = {"PP": "1", "PR": "2", "PS": "3", "PK": "4", "PL": "5",
                     "RP": "6", "RR": "7", "RS": "8", "RK": "9", "RL": "10",
                     "SP": "11", "SR": "12", "SS": "13", "SK": "14", "SL": "15",
                     "KP": "16", "KR": "17", "KS": "18", "KK": "19", "KL": "20",
                     "LP": "21", "LR": "22", "LS": "23", "LK": "24", "LL": "25"}

            temp2 = {"1": "PP", "2": "PR", "3": "PS", "4": "PK", "5": "PL",
                     "6": "RP", "7": "RR", "8": "RS", "9": "RK", "10": "RL",
                     "11": "SP", "12": "SR", "13": "SS", "14": "SK", "15": "SL",
                     "16": "KP", "17": "KR", "18": "KS", "19": "KK", "20": "KL",
                     "21": "LP", "22": "LR", "23": "LS", "24": "LK", "25": "LL"}

            who_win = {"PP": "0", "PR": "1", "PS": "-1", "PK": "1", "PL": "-1",
                       "RP": "-1", "RR": "0", "RS": "1", "RK": "-1", "RL": "1",
                       "SP": "1", "SR": "-1", "SS": "0", "SK": "-1", "SL": "1",
                       "KP": "-1", "KR": "1", "KS": "1", "KK": "0", "KL": "-1",
                       "LP": "-1", "LR": "-1", "LS": "-1", "LK": "1", "LL": "0"}

            predict_score = [0]*repeat
            my_choice = random.choice(RPSLS)
            predictors = [my_choice]*repeat
            return my_choice

        else:
            try:
                if len(list_predictor[0]) < 5:
                    front = 0
                else:
                    front = 1
                for i in range(repeat):
                    if predictors[i] == competitor:
                        result = "1"
                    else:
                        result = "0"
                    list_predictor[i] = list_predictor[i][front:5] + \
                        result

                my_lst += my_choice
                comp_lst += competitor
                history += temp1[competitor+my_choice]
                length += 1
                len_rfind = [20]
                limit = [10, 20, 60]

                for i in range(1):
                    len_size = min(length, len_rfind[i])
                    j = len_size

                    # history(my+competitor lst)
                    while j >= 1 and not history[length-j:length] in history[0:length-1]:
                        j -= 1  # j=j-1

                    if j >= 1:
                        k = history.rfind(
                            history[length-j:length], 0, length-1)
                        predictors[0+6*i] = comp_lst[j+k]
                        predictors[1+6*i] = beat[my_lst[j+k]]

                    else:
                        predictors[0+6*i] = random.choice(RPSLS)
                        predictors[1+6*i] = random.choice(RPSLS)
                    j = len_size

                    # comp_lst
                    while j >= 1 and not comp_lst[length-j:length] in comp_lst[0:length-1]:
                        j -= 1

                    if j >= 1:
                        k = comp_lst.rfind(
                            comp_lst[length-j:length], 0, length-1)
                        predictors[2+6*i] = comp_lst[j+k]
                        predictors[3+6*i] = beat[my_lst[j+k]]

                    else:
                        predictors[2+6*i] = random.choice(RPSLS)
                        predictors[3+6*i] = random.choice(RPSLS)
                    j = len_size

                    # my_lst
                    while j >= 1 and not my_lst[length-j:length] in my_lst[0:length-1]:
                        j -= 1

                    if j >= 1:
                        k = my_lst.rfind(my_lst[length-j:length], 0, length-1)
                        predictors[4+6*i] = comp_lst[j+k]
                        predictors[5+6*i] = beat[my_lst[j+k]]

                    else:
                        predictors[4+6*i] = random.choice(RPSLS)
                        predictors[5+6*i] = random.choice(RPSLS)

                for i in range(5):
                    temp = ""
                    search = temp1[(my_choice+competitor)]

                    for start in range(2, min(limit[i], length)):
                        if search == history[length-start]:
                            temp += history[length-start+1]

                    if (temp == ""):
                        predictors[6+i] = random.choice(RPSLS)

                    else:
                        # take win/lose from opponent into account
                        collectR = {"paper": 0, "rock": 0,
                                    "scissor": 0, "spock": 0, "lizard": 0}

                        for i in temp:
                            next_move = temp2[i]
                            if (who_win[next_move] == -1):
                                collectR[temp2[i][1]] += 5
                            elif (who_win[next_move] == 0):
                                collectR[temp2[i][1]] += 1
                            elif (who_win[next_move] == 1):
                                collectR[beat[temp2[i][0]]] += 1

                        max1 = -1
                        p1 = ""

                        for key in collectR:
                            if (collectR[key] > max1):
                                max1 = collectR[key]
                                p1 += key
                        predictors[6+i] = random.choice(p1)

            except:
                for i in range(9, 50):
                    predictors[i] = beat[beat[predictors[i-9]]]
                return random.choice(RPSLS)

            len_his = len(list_predictor[0])

            for i in range(repeat):
                sum = 0
                for j in range(len_his):
                    if list_predictor[i][j] == "1":
                        sum += (j+1)*(j+1)
                    else:
                        sum -= (j+1)*(j+1)
                predict_score[i] = sum
            max_score = max(predict_score)

            if max_score > 0:
                predict = predictors[predict_score.index(max_score)]
            else:
                predict = random.choice(comp_lst)

            my_choice = random.choice(not_lose[predict])
            return my_choice

    def update(self, result: str, competitor_shot: str):
        competitor = ""
        competitor += competitor_shot
        result_lst.append(result[0])  # 첫 게임 처리
        #print(competitor, "and", len(result_lst))


# (마르코프 모델을 써보려고 했는데, 실패했습니다)
# -> Shoot 함수 부분에서 RPScontest.com 참고했습니다.
