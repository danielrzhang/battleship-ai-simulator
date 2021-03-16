#########################################
# File Name: Battleship.py
# Description: Game of Battleship 
# Authors: Kathleen and Daniel
# Date: 25/11/2019
#########################################

from random import randint
import random
import copy
import pygame

pygame.init()

def chooseCoordinate(l, myShip, shipNum): #Kathleen
    SC = []
    duplicateShip = copy.deepcopy(myShip)
    x = random.randint(0,9)
    y = random.randint(0,9)
    d = random.randint(1,2)
    if(myShip[x][y] != 0):
        return chooseCoordinate(l, duplicateShip, shipNum)
    else:
        myShip[x][y] = shipNum
        SC.append(chr(x + 65) + str(y))
    if(d == 1):
        maxC = x
        minC = x
    elif(d == 2):
        maxC = y
        minC = y
    
    for i in range(l-1):
        d2 = random.randint(1,2)
        if(d == 1):
            if(maxC == 9):
                if(myShip[minC-1][y] != 0):
                    return chooseCoordinate(l, duplicateShip, shipNum)
                d2 = 1
            elif(minC == 0):
                if(myShip[maxC+1][y]!=0):
                    return chooseCoordinate(l, duplicateShip, shipNum)
                d2 = 2
            elif(myShip[maxC+1][y] !=0 and myShip[minC-1][y] !=0):
                return chooseCoordinate(l, duplicateShip, shipNum)
            elif(myShip[maxC+1][y] !=0):
                d2 = 1
            elif(myShip[minC-1][y] !=0):
                d2 = 2
            if(d2 == 1):
                minC = minC - 1
                myShip[minC][y] = shipNum
                SC.append(chr(minC+65) + str(y))
            elif(d2 == 2):
                maxC = maxC + 1
                myShip[maxC][y] = shipNum
                SC.append(chr(maxC+65) + str(y))
        elif(d==2):
            if(maxC ==9):
                if(myShip[x][minC-1] !=0):
                    return chooseCoordinate(l, duplicateShip, shipNum)
                d2 = 2
            elif(minC == 0):
                if(myShip[x][maxC+1] !=0):
                    return chooseCoordinate(l, duplicateShip, shipNum)
                d2 = 1
            elif(myShip[x][maxC+1] !=0 and myShip[x][minC-1] !=0):
                return chooseCoordinate(l, duplicateShip, shipNum)
            elif(myShip[x][maxC+1] !=0):
                d2 = 2
            elif(myShip[x][minC-1] !=0):
                d2 = 1
            if(d2 == 1):
                maxC = maxC + 1
                myShip[x][maxC] = shipNum
                SC.append(chr(x+65) + str(maxC))
            elif(d2 == 2):
                minC = minC - 1
                myShip[x][minC] = shipNum
                SC.append(chr(x+65) + str(minC))
    SC.sort()
    return myShip, SC

def PlotShip():#kathleen
    myShip = []
    shipList = []
    SC = [] 
    for i in range(10):
        myShip.append([int(0)]*10)
    myShip, SC = chooseCoordinate(5, myShip, 1)
    shipList.append(SC)
    myShip, SC = chooseCoordinate(4, myShip, 2)
    shipList.append(SC)
    myShip,SC = chooseCoordinate(3, myShip, 3)
    shipList.append(SC)
    myShip,SC = chooseCoordinate(3, myShip, 4)
    shipList.append(SC)
    myShip, SC = chooseCoordinate(2, myShip, 5)
    shipList.append(SC)
    return myShip, shipList

def printShip(shipList):#Kathleen
    for i in range(5):
        SC = shipList[i]
        if(SC[0][0] == SC[1][0]):
            pygame.draw.ellipse(gameWindow, shipGray, (52 + int(SC[0][1]) * 49, 200 + 50 * (ord(SC[0][0]) - 65), 49 * len(SC), 45))            

        else:
            pygame.draw.ellipse(gameWindow, shipGray, (50 + int(SC[0][1]) * 50, 200 + 50 * (ord(SC[0][0]) - 65), 45, 48 * len(SC)))

def shipName(z): #Kathleen
    ship = ""
    if(z == 1):
        ship ="AIRCRAFT CARRIER"
    elif(z ==2):
        ship ="BATTLESHIP"
    elif(z ==3):
        ship = "CRUISER"
    elif(z ==4):
        ship = "SUBMARINE"
    elif(z ==5):
        ship = "DESTROYER"
    return ship

def ifIn(myShip, z): #Kathleen
    for i in range(10):
        for j in range(10):
            if(myShip[i][j] == z):
                return True
    return False

def Attack(myShip):#Kathleen
    attack = input()
    if(len(attack) == 2 or len(attack) == 3):
        l = list(attack)
        x = ord(l[0])-65
        if(len(attack) == 3):
            if(l[1]=="1" and l[2]=="0"):
                y = 9
            else:
                y = 10
        else:
            if(l[1].isdigit()):
                y = int(l[1])-1
            else:
                y =10
    else:
        print("Not a valid coordinate. Please re-enter: ")
        return Attack(myShip)
    if(x > 9 or y > 9 or x < 0 or y < 0):
        print("Not a valid coordinate. Please re-enter: ")
        return Attack(myShip)
    xy = [x,y]
    return xy

def sweepStrikeZone(coordinates):#Daniel
    coords = [] 
    letter = coordinates[0]
    if len(coordinates) == 2:
        number = int(coordinates[1]) 
    elif (len(coordinates) == 3): 
        number = int(coordinates[1:])
    for i in range(0, 10):
        if letter == letterList[i]:
            newLetterAbove = letterList[i - 1]
            if(not letter == "J"):
                newLetterBelow = letterList[i + 1]
            else:
                newLetterBelow = ""
                
    coordinateLetterUp = newLetterAbove
    coordinateNumberUp = number
    coordinateLetterLeft = letter
    coordinateNumberLeft = number - 1
    coordinateLetterDown =  newLetterBelow 
    coordinateNumberDown = number
    coordinateLetterRight = letter
    coordinateNumberRight = number + 1
    
    if not (letter == "A") and not (letter == "J") and not (number == 1) and not (number == 10):
        coords.append(coordinateLetterUp + str(coordinateNumberUp))
        coords.append(coordinateLetterRight + str(coordinateNumberRight))
        coords.append(coordinateLetterDown + str(coordinateNumberDown))
        coords.append(coordinateLetterLeft + str(coordinateNumberLeft))        
    else:
        if letter == "A":
            if number == 1:
                coords.append(coordinateLetterRight + str(coordinateNumberRight))
                coords.append(coordinateLetterDown + str(coordinateNumberDown))
            elif number == 10:
                coords.append(coordinateLetterDown + str(coordinateNumberDown))
                coords.append(coordinateLetterLeft + str(coordinateNumberLeft))
            else:
                coords.append(coordinateLetterRight + str(coordinateNumberRight))
                coords.append(coordinateLetterDown + str(coordinateNumberDown))
                coords.append(coordinateLetterLeft + str(coordinateNumberLeft))
        elif letter == "J":
            if number == 1:
                coords.append(coordinateLetterUp + str(coordinateNumberUp))
                coords.append(coordinateLetterRight + str(coordinateNumberRight))
            elif number == 10:
                coords.append(coordinateLetterUp + str(coordinateNumberUp))
                coords.append(coordinateLetterLeft + str(coordinateNumberLeft))
            else:
                coords.append(coordinateLetterUp + str(coordinateNumberUp))
                coords.append(coordinateLetterRight + str(coordinateNumberRight))
                coords.append(coordinateLetterLeft + str(coordinateNumberLeft))
        else:
            if number == 1:
                coords.append(coordinateLetterUp + str(coordinateNumberUp))
                coords.append(coordinateLetterRight + str(coordinateNumberRight))
                coords.append(coordinateLetterDown + str(coordinateNumberDown))

            elif number == 10:
                coords.append(coordinateLetterUp + str(coordinateNumberUp))
                coords.append(coordinateLetterDown + str(coordinateNumberDown)) 
                coords.append(coordinateLetterLeft + str(coordinateNumberLeft))
    return coords

def untilSunk(shotList, p1, p2, directionG, bowlean, ifSunk, hitO, missO): #Kathleen and Daniel 
    reach = True 
    if (directionG==1):
        letter = p1[0]
        if(int(p2[1:]) == 10):
           bowlean = False
        if(int(p2[1:]) < int(p1[1:]) and bowlean):
            p3 = p2
            p2 = p1
            p1 = p3
            bowlean = False
        if(bowlean):
            number = int(p2[1:]) + 1
            if(letter + str(number) in shotList):
                number = int(p1[1:])-1
                bowlean = False
        else:
            number = int(p1[1:])-1
        print(letter+str(number))
        shotList.append(letter+str(number))
        status = input()
        while (not "MISS"  == status and not"HIT, DESTROYER" == status and not "HIT, CRUISER" == status and not "HIT, SUBMARINE" == status and not "HIT, BATTLESHIP" == status and not "HIT, AIRCRAFT CARRIER" == status and not "HIT, SUNK DESTROYER" == status and not"HIT, SUNK CRUISER" == status and not"HIT, SUNK SUBMARINE" == status and not"HIT, SUNK BATTLESHIP" == status and not "HIT, SUNK AIRCRAFT CARRIER" == status):
            print("Not a valid input. Please re-enter: ")
            status = input()
        if("HIT" in status):
            hitO += 1
            pygame.mixer.music.load("Explosion.mp3")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
        if(status == "MISS"):
            pygame.mixer.music.load("Splash.mp3")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
            bowlean = False
            missO += 1
        if(number == 10):
            bowlean = False
            reach = False
        if(number == 1):
            bowlean = False
        if("SUNK" in status):
            ifSunk = True
            pygame.mixer.music.load("Explosion.mp3")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
    else:
        number = p1[1:]
        if(p2[0] == "A"):
            bowlean = False
        if(ord(p2[0]) > ord(p1[0]) and bowlean):
            p3 = p2
            p2 = p1
            p1 = p3
            bowlean = False
        if(bowlean):
            letter = chr(ord(p2[0])-1)
            if(letter + str(number) in shotList):
                letter = chr(ord(p1[0])+1)
                bowlean = False
        else:
            letter = chr(ord(p1[0])+1)
        print(letter+str(number))
        shotList.append(letter+str(number))
        status = input()
        while (not "MISS"  == status and not"HIT, DESTROYER" == status and not "HIT, CRUISER" == status and not "HIT, SUBMARINE" == status and not "HIT, BATTLESHIP" == status and not "HIT, AIRCRAFT CARRIER" == status and not "HIT, SUNK DESTROYER" == status and not"HIT, SUNK CRUISER" == status and not"HIT, SUNK SUBMARINE" == status and not"HIT, SUNK BATTLESHIP" == status and not "HIT, SUNK AIRCRAFT CARRIER" == status):
            print("Not a valid input. Please re-enter: ")
            status = input()
        if("HIT" in status):
            hitO += 1
            pygame.mixer.music.load("Explosion.mp3")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
        if(status == "MISS"):
            pygame.mixer.music.load("Splash.mp3")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
            bowlean = False
            missO += 1
        if(letter == "J"):
            bowlean = False
        if(letter == "A"):
            reach = False
            bowlean = False
        if("SUNK" in status):
            ifSunk = True
            pygame.mixer.music.load("Explosion.mp3")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
    return shotList, bowlean, ifSunk, hitO, missO, status, reach

def printPoint(point, status, l):#Kathleen
    letter = ord(point[0]) - 65
    number = int(point[1:]) - 1
    if(l== 1):
        coordX = 700 + 50 * number + 25
    else:
        coordX = 50 + 50*number + 25
    coordY = 200 + 50 * letter + 25
    if(status == "MISS"):
        colour = (255, 255, 255)
    else:
        colour = (255, 0, 0)
    pygame.draw.circle(gameWindow, colour, (coordX, coordY), 15)

letterList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
numberList = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
shotList = []
bowlean = True
hitO = 0
missO = 0
shipNumO = 5
shotsO = 0
hitU = 0
missU = 0
shipNumU = 5
shotsU = 0
letterIndex = randint(0, 9)
coordinateLetter = letterList[letterIndex]
coordinateNumber = randint(0, 10)
thisHit = 0
check = []
newPoint = ""
ifSunk = False
inPlay = True
myShip, shipList = PlotShip()
coords =[]
coordNum = 0
directionG = 0
originalPoint = "" 
duplicateShip = copy.deepcopy(myShip)


gameWindow = pygame.display.set_mode((1300, 790))
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
seaBlue = (0, 45, 148)
navyBlue = (0, 0, 128)
red = (255, 0, 0)
shipGray = (169, 169, 169)
purple = (215, 120, 255)

font = pygame.font.SysFont("None", 50)
titleFont = pygame.font.SysFont("None", 100)
infoFont = pygame.font.SysFont("None", 30)
user = font.render("USER", 1, white)

opponent = font.render("OPPONENT", 1, white)
title = titleFont.render("BATTLESHIP", 1, white)
shadow = titleFont.render("BATTLESHIP", 1, black)

userWon = titleFont.render("USER HAS WON!", 1, white)
userLost = font.render("USER HAS LOST", 1, red)
opponentWon = titleFont.render("OPPONENT HAS WON!", 1, white)
opponentLost = font.render("OPPONENT HAS LOST", 1, red)
#Daniel
gameWindow.fill(navyBlue)
for squareLeftVertical in range(200, 700, 50):
    for squareLeftHorizontal in range(50, 550, 50):
        pygame.draw.rect(gameWindow, seaBlue, (squareLeftHorizontal, squareLeftVertical, 45, 45), 0)
for squareRightHorizontal in range(700, 1200, 50):
    for squareRightVertical in range(200, 700, 50):
        pygame.draw.rect(gameWindow, seaBlue, (squareRightHorizontal, squareRightVertical, 45, 45), 0)
pygame.draw.line(gameWindow, black, (610, 125), (610, 700), 7)
j = 0
k = 0
for i in letterList:
    leftLetterDisplay = font.render(i, 1, white)
    gameWindow.blit(leftLetterDisplay, (15, 210 + j * 50))
    j += 1
for l in numberList:
    leftNumberDisplay = font.render(l, 1, white)
    gameWindow.blit(leftNumberDisplay, (62 + k * 49, 160))
    k += 1
m = 0
o = 0
for n in letterList:
    rightLetterDisplay = font.render(n, 1, white)
    gameWindow.blit(rightLetterDisplay, (660, 210 + m * 50))
    m += 1
for p in numberList:
    rightNumberDisplay = font.render(p, 1, white)
    gameWindow.blit(rightNumberDisplay, (715 + o * 49, 160))
    o += 1
gameWindow.blit(user, (250, 110))
gameWindow.blit(opponent, (850, 110))
gameWindow.blit(shadow, (411, 30))
gameWindow.blit(title, (400, 25))
pygame.display.update()

printShip(shipList)

hitCounterUser = infoFont.render("HITS BY OPPONENT: " + str(hitU), 1, red)
missCounterUser = infoFont.render("MISSES BY OPPONENT: " + str(missU), 1, white)
shotCounterUser = infoFont.render("TOTAL SHOTS BY OPPONENT: " + str(shotsU), 1, purple)
shipCounterUser = infoFont.render("SHIPS LEFT FOR OPPONENT: " + str(shipNumO), 1, shipGray)
gameWindow.blit(hitCounterUser, (700, 710))
gameWindow.blit(missCounterUser, (1000, 710))
gameWindow.blit(shotCounterUser, (960, 750))
gameWindow.blit(shipCounterUser, (640, 750))

hitCounterOpponent = infoFont.render("HITS BY USER: " + str(hitO), 1, red)
missCounterOpponent = infoFont.render("MISSES BY USER: " + str(missO), 1, white)
shotCounterOpponent = infoFont.render("TOTAL SHOTS BY USER: " + str(shotsO), 1, purple) 
shipCounterOpponent = infoFont.render("SHIPS LEFT FOR USER: " + str(shipNumU), 1, shipGray)
gameWindow.blit(hitCounterOpponent, (70, 710))
gameWindow.blit(missCounterOpponent, (330, 710))
gameWindow.blit(shipCounterOpponent, (20, 750))
gameWindow.blit(shotCounterOpponent, (300, 750))

pygame.display.update()
#######################################
#Kathleen
print("Who is going first: OPPONENT or USER?")
nameShip = ""
otherPoint = ""
shipOther = False
otherShip = False
first = input()

while True:
    pygame.event.get()
    if(first == "OPPONENT"):
        xy = Attack(myShip)
        x = xy[0]
        y = xy[1]
        ship = shipName(myShip[x][y])
        if(myShip[x][y] == 0):
            pygame.mixer.music.load("Splash.mp3")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
            print("MISS")
            missU = missU + 1
            printPoint(chr(x+65)+str(y+1), "MISS", 2)
            
        else:
            print("HIT,", ship)
            pygame.mixer.music.load("Explosion.mp3")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
            myShip[x][y] = 6
            hitU = hitU + 1
            printPoint(chr(x+65)+str(y+1), "HIT", 2)
                       
        shotsU += 1
        #Daniel
        pygame.draw.rect(gameWindow, navyBlue, (625, 700, 700, 100), 0)
        hitCounterUser = infoFont.render("HITS BY OPPONENT: " + str(hitU), 1, red)
        missCounterUser = infoFont.render("MISSES BY OPPONENT: " + str(missU), 1, white)
        shotCounterUser = infoFont.render("TOTAL SHOTS BY OPPONENT: " + str(shotsU), 1, purple)
        shipCounterUser = infoFont.render("SHIPS LEFT FOR OPPONENT: " + str(shipNumO), 1, shipGray)
        gameWindow.blit(hitCounterUser, (700, 710))
        gameWindow.blit(missCounterUser, (1000, 710))
        gameWindow.blit(shotCounterUser, (960, 750))
        gameWindow.blit(shipCounterUser, (640, 750))
       
        pygame.display.update()
        pygame.event.get()
        ###########################
        break
    
    elif(first!= "USER"):
        print("Not a valid input. Please re-enter: ")
        first = input()
    else:
        break
###############################
while(inPlay):
    pygame.event.get()
    #Kathleen
    shotsO += 1
    if(not otherPoint == "" and shipOther):
        coords = sweepStrikeZone(otherPoint)
        coodNum = 0
        thisHit = 1
        shipOther = False
        originalPoint = otherPoint
        print("13", originalPoint)
        otherPoint = ""
    if(not len(coords) == 0 and thisHit == 1):
        while(coords[coordNum] in shotList):
            coordNum += 1
            print(11)
        print(coords[coordNum])
        
        shotList.append(coords[coordNum])
        newPoint = coords[coordNum]
        coordNum = coordNum + 1
        status = input()
        if("HIT" in status):
            
            if("SUNK" in status):
                nameShip2 = status[10:]
                shipOther = True
            else:
                nameShip2 = status[5:]
            print(nameShip2, nameShip)
            
            if(not nameShip2 == nameShip and not nameShip == ""):
                print(nameShip == "")
                otherShip = True
                otherPoint = coords[coordNum-1]
                print(" ", otherPoint)
                nameShip = ""
                
    ######################
    #Daniel
    elif(thisHit == 0):
        correct = True
        while(correct):
            coordinateNumber += 2
            if coordinateNumber == 12:
                if coordinateLetter == "J":
                    letterIndex = 0
                    coordinateLetter = letterList[letterIndex]
                else:
                    letterIndex += 1
                    coordinateLetter = letterList[letterIndex]
                coordinateNumber = 1
            elif coordinateNumber == 11:
                if coordinateLetter == "J":
                    letterIndex = 0
                    coordinateLetter = letterList[letterIndex]
                else:
                    letterIndex += 1
                    coordinateLetter = letterList[letterIndex]
                coordinateNumber = 2
            combined = coordinateLetter + str(coordinateNumber)

            if(combined not in shotList):
                correct = False
        
        print(combined)
        shotList.append(combined)
        newPoint = combined 
        status = input()
        if("HIT" in status):
            nameShip = status[5:]
    ##################################
    #Kathleen and Daniel
    while (not "MISS"  == status and not"HIT, DESTROYER" == status and not "HIT, CRUISER" == status and not "HIT, SUBMARINE" == status and not "HIT, BATTLESHIP" == status and not "HIT, AIRCRAFT CARRIER" == status and not "HIT, SUNK DESTROYER" == status and not"HIT, SUNK CRUISER" == status and not"HIT, SUNK SUBMARINE" == status and not"HIT, SUNK BATTLESHIP" == status and not "HIT, SUNK AIRCRAFT CARRIER" == status):
        print("Not a valid input. Please re-enter: ")
        status = input()
    ########################################
    #Kathleen
    if(thisHit >= 2):
        
        if thisHit == 2:
            if newPoint[0] in originalPoint:
                directionG = 1
            else:
                directionG = 2
        if(not "SUNK" in status):
            print(originalPoint, newPoint)
            shotList, bowlean, ifSunk, hitO, missO, status, reach, directionG = untilSunk(shotList, originalPoint, newPoint, directionG, bowlean, ifSunk, hitO, missO)
            if(not status == "MISS"):
                if (bowlean or not reach):
                    newPoint = shotList[-1]
                else:
                    originalPoint = shotList[-1]
            if(ifSunk):
                shipNumO -=1
                bowlean = True
                check = [] 
                direction = 0
                originalPoint = ""
                coordNum == 0
                newPoint = ""
                thisHit = 0
                ifSunk = False
                shipOther = True
        else:
            shipNumO -= 1
            hitO+=1
            bowlean = True
            check = [] 
            direction = 0
            originalPoint = ""
            coordNum == 0
            newPoint = ""
            thisHit = 0
            ifSunk = False
            shipOther = True
    elif("SUNK" in status):
        #Daniel
        pygame.mixer.music.load("Explosion.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
        ###############
        shipNumO -= 1
        hitO+=1
        bowlean = True
        check = [] 
        direction = 0
        originalPoint = ""
        coordNum == 0
        newPoint = ""
        thisHit = 0
        ifSunk = False
        shipOther = True
    elif("HIT" in status):
        #Daniel
        pygame.mixer.music.load("Explosion.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
        ################
        if(not otherShip):
            thisHit = thisHit + 1
            if (thisHit == 1):
                originalPoint = newPoint
            coords = sweepStrikeZone(newPoint)
            coordNum =0
        otherShip = False
        hitO +=1

    elif("MISS" in status):
        #Daniel
        pygame.mixer.music.load("Splash.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
        ##################
        missO +=1
    if(shipNumO == 0):
        #Daniel
        pygame.draw.rect(gameWindow, navyBlue, (625, 700, 700, 100), 0)
        hitCounterUser = infoFont.render("HITS BY OPPONENT: " + str(hitU), 1, red)
        missCounterUser = infoFont.render("MISSES BY OPPONENT: " + str(missU), 1, white)
        shotCounterUser = infoFont.render("TOTAL SHOTS BY OPPONENT: " + str(shotsU), 1, purple)
        shipCounterUser = infoFont.render("SHIPS LEFT FOR OPPONENT: 0", 1, shipGray)
        gameWindow.blit(hitCounterUser, (700, 710))
        gameWindow.blit(missCounterUser, (1000, 710))
        gameWindow.blit(shotCounterUser, (960, 750))
        gameWindow.blit(shipCounterUser, (640, 750))
        pygame.draw.rect(gameWindow, navyBlue, (0, 0, 1300, 700), 0)
        gameWindow.blit(userWon, (375, 300))
        gameWindow.blit(opponentLost, (475, 400))
        pygame.display.update()
        pygame.event.get()
        ##########################
        break
    point = shotList[-1]
    printPoint(point, status, 1)
    ##################################
    #Daniel
    pygame.draw.rect(gameWindow, navyBlue, (0, 700, 625, 100), 0)
    hitCounterOpponent = infoFont.render("HITS BY USER: " + str(hitO), 1, red)
    missCounterOpponent = infoFont.render("MISSES BY USER: " + str(missO), 1, white)
    shotCounterOpponent = infoFont.render("TOTAL SHOTS BY USER: " + str(shotsO), 1, purple) 
    shipCounterOpponent = infoFont.render("SHIPS LEFT FOR USER: " + str(shipNumU), 1, shipGray)
    gameWindow.blit(hitCounterOpponent, (70, 710))
    gameWindow.blit(missCounterOpponent, (330, 710))
    gameWindow.blit(shipCounterOpponent, (20, 750))
    gameWindow.blit(shotCounterOpponent, (300, 750))
    
    pygame.display.update()
    pygame.event.get()
    ##############################
    #Kathleen
    xy = Attack(myShip)
    x = xy[0]
    y = xy[1]
    if(myShip[x][y] == 0):
        #Daniel
        pygame.mixer.music.load("Splash.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
        ####################
        print("MISS")
        missU = missU + 1
        printPoint(chr(x+65)+str(y+1), "MISS", 2)
        
    else:
        z = myShip[x][y]
        if(z == 6 and not ifIn(myShip, duplicateShip[x][y])):
            # Daniel
            pygame.mixer.music.load("Splash.mp3")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
            ###################
            print("MISS")
            printPoint(chr(x+65)+str(y+1), "MISS", 2)
            missU +=1
        else:
            hitU +=1
            if(z == 6):
                ship = shipName(duplicateShip[x][y])
            else:
                ship = shipName(z)
            myShip[x][y] = 6
            if(not ifIn(myShip, z)):
                print("HIT, SUNK",ship)
                shipNumU -=1
            else:
                print("HIT,",ship)
            #Daniel
            pygame.mixer.music.load("Explosion.mp3")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
            #######################
            printPoint(chr(x+65)+str(y+1), "HIT", 2)
            
    shotsU += 1
    if(hitU == 17):
        #Daniel
        pygame.draw.rect(gameWindow, navyBlue, (0, 700, 625, 100), 0)
        hitCounterOpponent = infoFont.render("HITS BY USER: " + str(hitO), 1, red)
        missCounterOpponent = infoFont.render("MISSES BY USER: " + str(missO), 1, white)
        shotCounterOpponent = infoFont.render("TOTAL SHOTS BY USER: " + str(shotsO), 1, purple) 
        shipCounterOpponent = infoFont.render("SHIPS LEFT FOR USER: 0", 1, shipGray)
        gameWindow.blit(hitCounterOpponent, (70, 710))
        gameWindow.blit(missCounterOpponent, (330, 710))
        gameWindow.blit(shipCounterOpponent, (20, 750))
        gameWindow.blit(shotCounterOpponent, (300, 750))
        pygame.mixer.music.load("Lose.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
        pygame.draw.rect(gameWindow, navyBlue, (0, 0, 1300, 700), 0)
        gameWindow.blit(opponentWon, (250, 300))
        gameWindow.blit(userLost, (500, 400))
        pygame.display.update()
        pygame.event.get()
        ##################
        break
    ####################################
    #Daniel
    pygame.draw.rect(gameWindow, navyBlue, (625, 700, 700, 100), 0)
    hitCounterUser = infoFont.render("HITS BY OPPONENT: " + str(hitU), 1, red)
    missCounterUser = infoFont.render("MISSES BY OPPONENT: " + str(missU), 1, white)
    shotCounterUser = infoFont.render("TOTAL SHOTS BY OPPONENT: " + str(shotsU), 1, purple)
    shipCounterUser = infoFont.render("SHIPS LEFT FOR OPPONENT: " + str(shipNumO), 1, shipGray)
    gameWindow.blit(hitCounterUser, (700, 710))
    gameWindow.blit(missCounterUser, (1000, 710))
    gameWindow.blit(shotCounterUser, (960, 750))
    gameWindow.blit(shipCounterUser, (640, 750))
    pygame.display.update()
    #############################
