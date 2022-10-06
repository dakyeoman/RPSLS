from RPSLS_player import RPSLS_player

class P00001(RPSLS_player):
  def __init__(self):
    pass

  def shoot(self):
    return "lizard"
  
  def update(self, result: str, competitor_shot: str):
    pass