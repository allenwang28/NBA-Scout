from sklearn.cluster import KMeans
from data import Data

if __name__ == "__main__":
    d = Data()
    nbaData = d.processNBAData()

    numGroups = 20
    pred = KMeans(n_clusters=numGroups).fit_predict(nbaData)
    players = d.getPlayers()

    groups = []

    for i in range(0, numGroups):
        groups.append([])

    print len(pred)

    for idx, player in enumerate(players):
        try:
            groups[pred[idx]].append(player)
        except:
            print idx

    thisGroup = 5
    print "Group " + str(thisGroup) + " results: "
    for player in groups[thisGroup]:
        print player.name




