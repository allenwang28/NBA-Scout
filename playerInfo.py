from pandas import DataFrame
from nba_py import player as p


class Player:
    def __init__(self, playerID, playerName):
        print "Processing " + playerName
        self.name = playerName
        self.ID = playerID
        try:
            self.career = p.PlayerCareer(self.ID)
        except:
            print "There was an error with " + playerName
            self.career = None

        if self.career:
            self.collegeStats = self.career.career_college_season_totals()
            self.regStats = self.career.regular_season_career_totals()
        else: 
            self.collegeStats = None
            self.regStats = None

