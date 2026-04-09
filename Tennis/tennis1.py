
class TennisGame1:
    _draw_scores = {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
            }
    
    _score_dictionary = {
                0: "Love",
                1: "Fifteen",
                2: "Thirty",
                3: "Forty",
            }
    
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.p1points += 1
        else:
            self.p2points += 1
            

    def winning_player(self):
        minusResult = self.p1points - self.p2points
        if minusResult == 1:
            return "Advantage " + self.player1_name
        elif minusResult == -1:
            return "Advantage " + self.player2_name
        elif minusResult >= 2:
            return "Win for " + self.player1_name
        else:
            return "Win for " + self.player2_name
        
        
    def score(self):
        if self.p1points == self.p2points:
            return self._draw_scores.get(self.p1points, "Deuce") 
        elif self.p1points >= 4 or self.p2points >= 4:
            return self.winning_player()
        
        return self._score_dictionary[self.p1points] + "-" + self._score_dictionary[self.p2points]
        
