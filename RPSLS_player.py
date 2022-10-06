from abc import ABC, abstractmethod

class RPSLS_player(ABC):

  @abstractmethod
  def shoot(self) -> str:
    pass

  @abstractmethod
  def update(self, result: str, competitor_shot: str):
    pass