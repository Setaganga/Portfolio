from time import sleep
from random import randint

SleepTimer = 1
masterList = []
playerList = []

print("-------------------\nWelcome to SIMON!!!\n-------------------")
sleep(2)
print("-------------------\nNOTE: You may have\nto re-adjust your\nterminal to play!\n-------------------")
sleep(4)

while True:
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
        print("Error 1: Randint failed to choose number...somehow.")

    for _ in masterList:
        print(_)
        sleep(SleepTimer)

    print("\n\n\n\n\n\n\n\n\n\n---------------------\nEnter in combination:")

    masterlen = len(masterList)
    for a in range(masterlen):
        playerList.append(input())
        if masterList[a] == playerList[a]:
            continue
        else:
            print("You failed!")
            exit()

    print("----------------------------------\nCorrect! Moving to the next round.")
