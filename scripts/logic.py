############################### THIS IS ALL FOR CLASSES ABOVE, YOU DON'T NEED THIS ############################
import csv
import os

class Role:
    def __init__(self, listylist):
        self.champion = listylist[0] #champion name
        self.name = listylist[1]     #lane
        self.winrate = float(listylist[2])  #overall winrate percent
        
    def __str__(self):
        return "{0} in {1} has a winrate of {2}".format(self.champion, self.name, self.winrate)

class Winrate:
    def __init__(self, role1, role2, winrate):
        self.champ = role1
        self.opponent = role2
        self.winrate = float(winrate)

roleslist = []
winratelist = []
csvpath = '/CSV Files'

readfile = open(os.getcwd() + csvpath + '/role.csv')
readfile2 = open(os.getcwd() + csvpath + '/winrate.csv')
reader = csv.reader(readfile)
reader2 = csv.reader(readfile2)
for row in reader:
    if not row[0] == 'Champion':
        roleslist.append(Role(row))
for row in reader2:
    if not row[0] == 'Name':
        for item in roleslist:
            if item.champion == row[0] and item.name == row[2]:
                champ1 = item
            elif item.champion == row[1] and item.name == row[2]:
                champ2 = item
        winratelist.append(Winrate(champ1, champ2, row[3]))

readfile.close()
############################### THIS IS ALL FOR CLASSES ABOVE, YOU DON'T NEED THIS ############################

def sorttopten(tops):#sorts the top ten champions so far from lowest winrate to highest winrate
    done = False
    while not done:
        done = True
        for i in range(9):
            if tops[i][2] > tops[i+1][2]:#stupid bubble sort, but it works
                temp = tops[i]
                tops[i] = tops[i+1]
                tops[i+1] = temp
                done = False

    return tops


def bestpicks(team1, team2, bans):
    topten = []
    for champ in roleslist: #iterates over the roles table
##        print 'Current topten'
##        for item in topten:                  #debugging print statements
##            print '\t',item
##        print '\nLooking at ' + champ.champion + ' with a winrate of ' + str(champ.winrate)
        if not (champ.champion in bans or champ.champion in team1 or champ.champion in team2):
            if len(topten) < 10: #puts the first ten in there because it was easier for the other function
                topten.append([champ.champion, champ.name, champ.winrate])
            else:
                topten = sorttopten(topten) #sorts them
                for index, item in enumerate(topten): #iterator, item pair to know what to replace
                    if item[2] < champ.winrate:
                        topten[index] = [champ.champion, champ.name, champ.winrate]
                        break    #break so that it doesn't compare or replace more than it needs to
    return topten

def bestcounter(team1, team2, bans): #team1 should be the team currently picking, makes code less repetitive
    topten = []
    applicable = []
    for pair in winratelist:   #iterates over the winrate table
        if not (pair.champ.champion in bans or pair.champ.champion in team1 or
                            pair.champ.champion in team2) and pair.opponent.champion in team2:
                    #If the champ hasn't been picked and the opponent is on the enemy
                    #team (because we don't care if they aren't on team2)
            if len(applicable) == 0: #defaulting to add something to the list that is applicable
                applicable.append([pair.champ.champion, pair.champ.name, pair.winrate])
            else:
                found = False
                for item in applicable:
                    if item[0] == pair.champ.champion and item[1] == pair.champ.name: #if previous roles match
                        found = True
                        item[2] = (item[2] + pair.winrate)/2 #average the winrate in this situation for this champ
                        break
                if not found:
                    applicable.append([pair.champ.champion, pair.champ.name, pair.winrate])

    for champ in applicable:
##        print 'Current topten'
##        for item in topten:                  #debugging print statements
##            print '\t',item
##        print '\nLooking at ' + champ[0] + ' with a winrate of ' + str(champ[2])
        if len(topten) < 10:
            topten.append(champ)
        else:
            topten = sorttopten(topten)
            for index, item in enumerate(topten):
                if item[2] < champ[2]:
                    topten[index] = [champ[0], champ[1], champ[2]]
                    break


                    
    return topten
