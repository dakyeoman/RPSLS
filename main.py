from P00001 import P00001
from P17773 import P17773
from RPSLS_game import RPSLS_game


N = 1000000000

game = RPSLS_game(P17773, P00001)
for i in range(1, N+1):
    print(f"[Round {i}]")
    game.proceed_match()

print(game.get_score())


ave = game.get_score()
ave['P17773']/N

