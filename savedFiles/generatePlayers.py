# nba_py doesn't have a way to include all players that exist historically 
# This file is used only to generate a list of all players.
# The txt file used is listed under here:
originalFile = "nbaplayers.txt"
# I went to stats.nba.com/players and went to historic and just copied all of the player names into a text file.
# That's where it came from

# The new txt file will be saved as:
newFile = "nbaplayernames.txt"


f1 = open(originalFile, "r")
f2 = open(newFile, "w")

for line in f1:
    l = line.rstrip()
    l = l.split('[', 1)[0]
    if len(l) > 1: # Skips single letters
        f2.write(l + '\n')
f1.close()






