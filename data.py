from pandas import DataFrame
from nba_py import player as p
from playerInfo import Player

        
class Data:
    def __init__(self):
        playerList = p.PlayerList().info()
        self.players = []
        pIDs = playerList['PERSON_ID']
        pNames = playerList['DISPLAY_LAST_COMMA_FIRST']
        numProcessed = 15
        print "There are " + str(len(pIDs)) + " players in this list"
        print "Only displaying " + str(numProcessed)
#        for idx in range(0, len(pIDs) - 1):
        for idx in range(0, numProcessed):
            self.players.append(Player(pIDs[idx], pNames[idx]))

    def getPlayers(self):
        return self.players


# stats is expected in a data frame
def printStats(stats):
    for key in stats.keys():
        try:
            print key + ": " + str(float(stats[key]))
        except TypeError:
            print key + ": N/A"
            pass


if __name__ == '__main__':
    d = Data()
    print("-------------------------------")
    for p in d.getPlayers():
        print "Player: " + p.name
        print("-------------------------------")
        print "College Stats: "
        if p.collegeStats().empty:
            print "No College Stats found"
        else:
            printStats(p.collegeStats())
        print("--------------------------")
        print "NBA Stats: "
        printStats(p.nbaStats())
        print("--------------------------")
