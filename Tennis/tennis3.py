class TennisGame3:
    def __init__(self, player1_name, player2_name):
        self.p1_name = player1_name
        self.p2_name = player2_name
        self.p1_score = 0
        self.p2_score = 0

    def won_point(self, player_name):
        if player_name == self.p1_name:
            self.p1_score += 1
        else:
            self.p2_score += 1

    def score(self):
        is_draw = self.p1_score == self.p2_score
        is_not_win = (self.p1_score - self.p2_score) * (self.p1_score - self.p2_score) == 1
        
        if (self.p1_score < 4 and self.p2_score < 4) and (self.p1_score + self.p2_score < 6):
            
            point_to_name = ["Love", "Fifteen", "Thirty", "Forty"]
            player1_results = point_to_name[self.p1_score]
            player2_results = point_to_name[self.p2_score]
            
            return player1_results + "-All" if (is_draw) else player1_results + "-" + player2_results
        else:
            if is_draw:
                return "Deuce"
            winning_player_name = self.p1_name if self.p1_score > self.p2_score else self.p2_name
            return (
                "Advantage " + winning_player_name
                if is_not_win
                else "Win for " + winning_player_name
            )
