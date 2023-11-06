class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality =dict['nationality']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.team = dict['team']
        self.points = self.goals +self.assists


    def __str__(self):
        return f"{self.name:20}" + f"{self.team:5}" + f"{self.goals:2}" + " + " +f"{self.assists:2}" + " = " + str(self.points)
