class TennisGame2:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.p1_score()
        else:
            self.p2_score()

    def point_to_score(self, point):
        match point:
            case 0:
                return "Love"
            case 1:
                return "Fifteen"
            case 2:
                return "Thirty"
            case 3:
                return "Forty"
            case _:
                return ""

    def score(self):
        # Stan remisowy
        if self.p1points == self.p2points and self.p1points < 3:
            return self.point_to_score(self.p1points) + "-All"
        elif self.p1points == self.p2points and self.p1points >= 3:
            return "Deuce"

        # Punkty do nazwy
        p1res = self.point_to_score(self.p1points)
        p2res = self.point_to_score(self.p2points)
        
        # Róznica punktów
        if self.p1points < 4 and self.p2points < 4: 
            return p1res + "-" + p2res
            
        # Wygrana jednego z graczy
        if self.p1points != self.p2points and abs(self.p1points - self.p2points) >= 2 and (self.p1points >= 4 or self.p2points >= 4):
            if self.p1points > self.p2points:
                return "Win for " + self.player1_name
            else:
                return "Win for " + self.player2_name
        
        # Przewaga jednego z graczy
        if self.p1points != self.p2points and self.p1points >= 3 and self.p2points >= 3:
            if self.p1points > self.p2points:
                return "Advantage " + self.player1_name
            else:
                return "Advantage " + self.player2_name
        return ""
    
    def p1_score(self):
        self.p1points += 1

    def p2_score(self):
        self.p2points += 1
