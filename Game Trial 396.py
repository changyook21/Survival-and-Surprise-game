import random
import math

def readlist(the_file): 
    fileRef = open(the_file,"r") 
    localList=[]
    for line in fileRef:
        string = line[0:len(line)-1]  
                                      
                                    
        localList.append(string)  
        
    fileRef.close()    
    return localList

def extractinfo(area):
    diamonds = []
    swords = []
    enemies = []
    for i in range(len(area)):
        newarea = area[i].split("-")
        diamonds.append(int(newarea[0]))
        swords.append(int(newarea[1]))
        enemies.append(int(newarea[2]))
    return diamonds, swords, enemies

def biomes():
    biomes = []
        
    for i in range(len(diamondslist)):
            biomes.append(i)        
    return biomes

def diceroll():
    roll = random.randint(1, 6)
    return roll

def choice(): 
    x = "(0..." + str(len(diamondslist) - 1) + ") "
    pos = input("Which biome should the player go to?" + x)
    return pos

def playerposition(): 
    decision = raw_input("Roll die or choose next position? (d/u): ")
    global playerpos
    if decision == "d":
        roll = diceroll()
        print "The die was... ", roll
        print "The previous position was... ", playerpos
        playerpos += roll
        if playerpos > len(biomeslist):
            playerpos = playerpos - len(biomeslist)
        if playerpos==8:
            playerpos=playerpos-playerpos
        print "The next position is... ", playerpos
        return playerpos
    elif decision == "u":
        playerpos = choice()
        return playerpos

def pythonshine(maxpos):
    while(1==1):
        ps_pos = input("Which position shall PythonShine be? (1..."+str(maxpos)+"), 0 has no effect: ")
        if(ps_pos > 0 and ps_pos<= maxpos):
            break
        else:
            print "type a number between 1 and "+str(maxpos)
    return ps_pos

'''
def turns():
    maxturns = input("Maximum number of turns this game? (1...10) ")
    return maxturns
'''

def intro():
    n='n'
    d = "biomesData1.txt"
    filename = input("Type name of board file (d for default): ")
    textinfo = readlist(filename)
	
    name = raw_input("Name? ")

    while(1==1):
        hp = input("Initial life points? (10...50) ")
        if(hp >= 10 and hp<= 50):
            break
        else:
            print "type a number between 10 and 50"

    while(1==1):    
        maxturns = input("Maximum number of turns this game? (1...10) ")
        if(maxturns >= 1 and maxturns <= 10):
            break
        else:
            print "type a number between 1 and 10"
            
    while(1==1):
        cata= input("Allow that catastrophes happen? (y/n):")
        if cata == "y":
            break
        elif cata =="n":
            break
       

    
    
    return textinfo, name, hp, maxturns, cata

def player():
    print "Showing player... about to do turn num: " + str(turn_number)
    print "The player " + name
    print "currently has: " + str(hp) + " life points"
    if(sword == 0):
        print "has no sword"
    else:
        print "has a sword of matetial: " + str(sword)
    print "has " + str(diamond) + " diamonds"
    print "is in the position: " + str(playerpos)
    if(hp > 0):
        print "so... he is... very alive!!!"
    print ""
    
    '''
    print "The current condition of player " + name
    print "HP: ", hp
    if sword == 0:
        print "No sword"
    if sword > 0:
        print "Sword of strength: ", sword
    print "Diamonds: ", diamond
    '''
    
def drawboard():
    print "\n"
    heading = ["Biome", "Diam", "Swords", "Enemies"]
    for i in range(len(heading)):
        print heading[i], "\t",
    print "\n"
    matrix = [biomeslist, diamondslist, swordslist, enemieslist]
    for r in range(len(biomeslist)):
        for c in range(len(matrix)):
            print matrix[c][r], "\t",
        if(pythonshine_pos == r):
            print " <=== PythonShine",
        if(playerpos == r):
            print " <--- Player",
        print
    print "\n"

def captureDiamond():
    newDiamond = int(math.floor(diamondslist[player_pos]/3))
    diamond += newDiamond
    diamondslist[player_pos] = diamondslist[player_pos] - newDiamond
    print "yey!!... the plater collected "+ str(newDiamond) + " diamonds"
    

def captureSword():
    if( swordslist[player_pos] > sword ):
        temp = sword
        sword = swordslist[player_pos]
        swordslist[player_pos] = temp
        print "yey!!... the plater exchanged to a better sword"
        print "The plater's new sword is of type: " + str(sword)

def fightEnemy():
    hpDiff = 0
    if( sword < enemieslist[player_pos]):
        hpDiff = -random.randint(1, hp)
    elif(sword == enemieslist[player_pos]):
        hpDiff = -random.randint(1, hp/2)
    else:
        hpDiff = random.randint(1, hp)

    if(hpDiff < 0):
        print "oh well... the player tied the fight and lost " + str(-hpDiff) + "life points"
    else:
        print "Great! the plater won the fight and won " + str(hpDiff) + " life points"
    hp += hpDiff
    print "The player now has 12 life points"
    

### Top Level Code
y = raw_input("Do you want to draw the board?(y/n): ")
x = raw_input("Do you want to play the game?(y/n): ")
while x=="y" and y == "y":
    pythonshine_pos = -1
    playerpos = 0
    textinfo, name, hp, maxturns, cata = intro()                   
    diamondslist, swordslist, enemieslist = extractinfo(textinfo)
    biomeslist = biomes()

    drawboard()

    pythonshine_pos = pythonshine(len(diamondslist)-1)
    turn_number = 0
    diamond = 0
    sword = 0

    while turn_number < maxturns and playerpos != pythonshine_pos: #game core... need to adjust condition(s)
        drawboard()
        player()
        player_pos = playerposition()
        print "";
    #check current status
        if player_pos == pythonshine_pos: 
            print "You win"
            break
        elif hp <= 0:
            print "You died"
            break


    #captureDiamond
        newDiamond = int(math.floor(diamondslist[player_pos]/3))
        diamond += newDiamond
        diamondslist[player_pos] = diamondslist[player_pos] - newDiamond
        print "yey!!... the player collected "+ str(newDiamond) + " diamonds"
    
    #captureSword
        if( swordslist[player_pos] > sword ):
            temp = sword
            sword = swordslist[player_pos]
            swordslist[player_pos] = temp
            print "yey!!... the player exchanged to a better sword"
            print "The player's new sword is of type: " + str(sword)

    #fightEnemy
        hpDiff = 0
        if( sword < enemieslist[player_pos]):
            hpDiff = -random.randint(1, hp)
        elif(sword == enemieslist[player_pos]):
            hpDiff = -random.randint(1, hp/2)
        else:
            hpDiff = random.randint(1, hp)

        if(hpDiff < 0):
            print "oh well... the player tied the fight and lost " + str(-hpDiff) + " life points"
        else:
            print "Great! the player won the fight and won " + str(hpDiff) + " life points"
        hp += hpDiff
        print "The player now has " + str(hp) + " life points"
   
    #catastraph
        if cata==y:
            catastraph = random.randint(1, (len(diamondslist)-1)*5)
            if(catastraph < len(diamondslist)-1):

                print "Oh No! A catastroph occured in biome #" + str(catastraph)
                print "and the board shrunk"
                if(player_pos == catastraph):
                    #player dead
                    hp = 0
            
                elif (player_pos > catastraph):
                    #position change
                    player_pos -= 1
                    print "but the player was not there, yet the player's position changed"
                else:
                    #position not change
                    print "but the player was not there and the player's position is not changed"
                #shrink
                diamondslist.pop(catastraph)
                swordslist.pop(catastraph)
                enemieslist.pop(catastraph)
                for i in range(len(biomeslist) - catastraph):
                    biomeslist[catastraph + i] = biomeslist[catastraph + i] - 1
                biomeslist.pop(catastraph)
        
            else:
                ##occured outside of the board
                print "great! catastroph occured outside of the board!"

        #surprise
    turn_number += 1
    u = raw_input("Do you want to play again?(y/n): ")
    if u == "n":
        print "Ending..."
        exit()

else:
    exit()


