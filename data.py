from pandas import DataFrame
from nba_py import player as p
from playerInfo import Player

import cPickle as pickle
import sys

# These will act as the parameters for our machine learning 
#relevantKeys = ["MIN", "FGM", "FGA", "FG3M", "FG3A", "FTM" ,"FTA", "REB", "AST", "STL", "BLK", "TOV"]
relevantKeys = ["FG_PCT", "FG3_PCT", "FT_PCT"]

# These are a list of parameters that are used as keys
allKeys = ["PLAYER_ID", "LEAGUE_ID", "TEAM_ID", "GP", "GS", "MIN", "FGM", "FGA", "FG_PCT", "FG3M", "FG3A", "FG3_PCT",
        "FTM", "FTA", "FT_PCT", "OREB", "DREB", "REB", "AST", "STL", "BLK", "TOV", "PF", "PTS"]

savedPlayerData = "savedFiles/playerData.p"
playerNamesList = "savedFiles/nbaplayernames.txt"

def getPlayerNames():
    f = open(playerNamesList, "r") 
    players = []
    for line in f:
        l = line.rstrip()
        players.append(l)
    return players

class Data:
    def __init__(self):
        try:
            self.players = pickle.load(open(savedPlayerData, "rb"))
            print "Pickle file found! Loading..."
        except: 
            # When the saved file doesn't exist...
            players = getPlayerNames()
            self.players = []
            i = 1
            for player in players:
                try: 
                    last, first = "".join(player.split()).split(',', 1)
                except:
#                    print "Skipping over " + player
                    continue

                print "Found " + first + " " + last
                pID = p.get_player(first, last)
                new_player = Player(pID, player)
                if new_player.career:
                    self.players.append(new_player)
            pickle.dump(self.players, open(savedPlayerData, "wb"))

    def getPlayers(self):
        return self.players

    def processNBAData(self):
        processedData = []
        for player in self.players:
            playerData = []
            failed = False
            for key in relevantKeys:
                try:
                    playerData.append(float(player.regStats[key]))
                except:
                    # do not include this player in the list
                    # print "Skipping " + player.name
#                    self.players.remove(player)
                    playerData.append(-1.0)
#                    failed = True
#                    break
            if not failed:
                processedData.append(playerData)
        return processedData

    def processCollegeData(self):
        processedData = []
        for player in self.players:
            playerData = []
            failed = False
            for key in relevantKeys:
                try:
                    playerData.append(float(player.collegeStats[key]))
                except:
                    # do not include this player in the list
                    print "Skipping " + player.name
                    failed = True
                    break
            if not failed:
                processedData.append(playerData)
        processedData = []
        for player in self.players:
            playerData = []
            for key in relevantKeys:
                playerData.append(player.collegeStats[key])
            processedData.append(playerData)
        return processedData






########################################################################
# All code below is just used for testing
########################################################################

# stats is expected in a data frame
def printStats(stats):
#    for key in stats.keys():
    for key in relevantKeys:
        try:
            print key + ": " + str(float(stats[key]))
        except TypeError:
            print key + ": N/A"
            pass


if __name__ == '__main__':
    d = Data()
    print("-------------------------------")
    for player in d.getPlayers():
        print "Player: " + player.name
        print("-------------------------------")
        print "College Stats: "
        if player.collegeStats.empty:
            print "No College Stats found"
        else:
            print player.collegeStats
        print("--------------------------")
        print "NBA Stats: "
        printStats(player.regStats)
        print("--------------------------")
