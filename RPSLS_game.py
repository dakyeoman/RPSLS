class RPSLS_game():
    """ A class used to proceed the match

    Attributes
    ----------
    _proper_shooting: list
        the list of proper answers for player's shoot method
        [None, "rock", "paper", "scissors", "lizard", "spock"]
    _game_score: list
        the list scores for player1 and player2
        [player1, player2]
    _player[n]: RPSLS_player class name
        the class name for player[n]

    Methods
    -------
    proceed_match()
        starts 1 RPSLS match and update results for player1 and player2
    get_winner(p1_shoot, p2_shoot)
        decide the winner for one match shootouts
    get_score()
        return dictionary of player_names(key) and scores(value)
    """

    _proper_shootings = [None, "rock", "paper", "scissors", "lizard", "spock"]

    def __init__(self, p1, p2):
        """
        Parameters
        ----------
        p[n] : RPSLS_player class name
            the name of RPSLS_player class for player[n]
        """

        self._game_score = [0, 0]   # default score [p1:p2] = [0, 0]
        self._player1 = p1()
        self._player2 = p2()

    def proceed_match(self):
        """
        starts 1 RPSLS match and update results for player1 and player2
        """

        # get shoots
        try:
            p1_shoot = self._player1.shoot()
        except:
            print("Error in Player 1's shoot method")
            p1_shoot = None
        try:
            p2_shoot = self._player2.shoot()
        except:
            print("Error in Player 2's shoot method")
            p2_shoot = None

        # print shoots
        print(f"Player 1: {p1_shoot}")
        print(f"Player 2: {p2_shoot}")

        # check properness of shoots
        if p1_shoot not in self._proper_shootings:
            print("Player 1's shoot is wrong")
            p1_shoot = None

        elif p2_shoot not in self._proper_shootings:
            print("Player 2's shoot is wrong")
            p2_shoot = None

        # calculate match results
        p1_result, p2_result = self.get_winner(p1_shoot, p2_shoot)

        print(f"Result: {p1_result}, {p2_result}")

        # update score
        if p1_result == "win":
            self._game_score[0] += 1
        elif p1_result == "lose":
            self._game_score[1] += 1

        # push results to players
        self._player1.update(p1_result, p2_shoot)
        self._player2.update(p2_result, p1_shoot)

    def get_winner(self, p1_shoot, p2_shoot):
        """
        decide the winner for one match shootouts

        Parameters
        ----------
        p[n]_shoot : str
            the shootout string of player[n]'s shoot
        """

        p1_win_set = (
            ("rock", "scissors"), ("scissors", "paper"), ("paper",
                                                          "rock"), ("lizard", "spock"), ("spock", "scissors"),
            ("rock", "lizard"), ("scissors", "lizard"), ("paper",
                                                         "spock"), ("lizard", "paper"), ("spock", "rock")
        )
        p2_win_set = ((x[1], x[0]) for x in p1_win_set)
        if (p1_shoot, p2_shoot) in p1_win_set:
            return ("win", "lose")
        elif (p1_shoot, p2_shoot) in p2_win_set:
            return ("lose", "win")
        else:
            return ("draw", "draw")

    def get_score(self) -> dict:
        p1_name = type(self._player1).__name__
        p2_name = type(self._player2).__name__
        p1_score, p2_score = self._game_score
        return {p1_name: p1_score, p2_name: p2_score}
