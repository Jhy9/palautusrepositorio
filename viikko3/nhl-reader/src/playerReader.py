import requests
from player import Player


class PlayerReader:
    def __init__(self,url):
        self.players = requests.get(url).json()

    def get_players(self):
        player_list = []
        for player in self.players:
            player_list.append(Player(player))
        return player_list