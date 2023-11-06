from player import Player

def sort_by_points(p):
    return p.points

class PlayerStats:
    def __init__(self,players):
        self.players = players
        
    def top_scorers_by_nationality(self, nationality):
        filtered = []
        for p in self.players.get_players():
            if p.nationality == nationality:
                filtered.append(p)
        return sorted(filtered,reverse = True, key = sort_by_points)

