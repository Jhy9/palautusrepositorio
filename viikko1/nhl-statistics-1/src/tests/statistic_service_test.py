import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]
class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_gets_right_result(self):
        self.assertAlmostEqual(self.stats.search("Kurri").name,"Kurri")

    def test_search_not_found_gives_nothing(self):
        self.assertAlmostEqual(None, self.stats.search("AAA"))

    def test_team_gives_right_players(self):
        self.assertAlmostEqual("Gretzky", self.stats.team("EDM")[2].name)

    def test_top_gives_best_first(self):
        self.assertAlmostEqual("Gretzky", self.stats.top(4,SortBy.POINTS)[0].name)

    