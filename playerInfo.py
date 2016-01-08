from pandas import DataFrame
from nba_py import player as p


class Player:
    def __init__(self, playerID, playerName):
        print "Processing " + playerName
        self.name = playerName
        self.ID = playerID
        self.career = p.PlayerCareer(self.ID)

    def collegeStats(self):
        return self.career.career_college_season_totals()
#        return self.career.college_season_totals()

    def nbaStats(self):
        return self.career.regular_season_career_totals()
#        return self.career.regular_season_totals()

