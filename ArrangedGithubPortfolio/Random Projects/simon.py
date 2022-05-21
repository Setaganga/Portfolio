from time import sleep
from random import randint
import re
SleepTimer = 1
masterList = []
playerList = []
gameRun = True
currentRound = 1
while gameRun:
    playerList = []
    num = randint(1,4)
    if num == 1:
        masterList.append(str(num))
    elif num == 2:
        masterList.append(str(num))
    elif num == 3:
        masterList.append(str(num))
    elif num == 4:
        masterList.append(str(num))
    else:
        print("Error 1: WTF Error. Randint failed to choose number")
    for _ in masterList:
        print(_)
        sleep(SleepTimer)
    print("\n\n\n\n\n\n\n\n\n\nEnter in combination:")
    for a in masterList:
        playerList.append(input())
    if masterList == playerList:
        print("Correct! Moving to next round.")
    else:
        print("You failed!")
        break
    if currentRound > 99:
        SleepTimer = 0.05
    elif re.search(r"0",str(currentRound)):
        SleepTimer - 0.1
    currentRound += 1