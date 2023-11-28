class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score +1
        else:
            self.player2_score = self.player2_score +1

    def get_score(self):
        if self.player1_score > self.player2_score:
            return self.score_printer("p1 lead")
        elif self.player1_score < self.player2_score: 
            return self.score_printer("p2 lead")
        else:
            return self.score_printer("tie")

    def check_for_win(self):
        if (self.player1_score - self.player2_score) >= 2 and self.player1_score >= 4:
            return "Win for player1"
        elif (self.player1_score - self.player2_score) <= -2 and self.player2_score >= 4:
            return "Win for player2"
        return None

    def score_printer(self, score):
        if self.check_for_win() is not None:
            return self.check_for_win()
        if score == "tie":
            if self.player1_score == 0:
                return "Love-All"
            elif self.player1_score == 1:
                return "Fifteen-All"
            elif self.player1_score == 2:
                return "Thirty-All"
            else:
                return "Deuce"
        elif score == "p1 lead" and self.player2_score >= 3:
            return  "Advantage player1"
        elif score == "p2 lead" and self.player1_score >= 3:
            return  "Advantage player2"
        else:
            return self.get_score_terminology(self.player1_score)+ "-"+self.get_score_terminology(self.player2_score)

    def get_score_terminology(self,score):
        if score == 0:
            return "Love"
        elif score == 1:
            return "Fifteen"
        elif score == 2:
            return "Thirty"
        else:
            return "Forty"
