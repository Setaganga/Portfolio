opList = []
for _ in range(int(input())):
    temp = input()
    currentCommand = temp.split()
    nOargs = len(currentCommand)
    print(currentCommand)
    if nOargs > 2:
        opList.insert(int(currentCommand[1]),int(currentCommand[2]))
    elif nOargs > 1:
        if currentCommand[0] == "remove":
            opList.remove(int(currentCommand[1]))
        elif currentCommand[0] == "append":
            opList.append(int(currentCommand[1]))
        else:
            print("Command outside of available methods")
    else:
        if currentCommand[0] == "print":
            print(opList)
        elif currentCommand[0] == "sort":
            opList.sort()
        elif currentCommand[0] == "pop":
            opList.pop()
        elif currentCommand[0] == "reverse":
            opList.reverse()
        else:
            print("Command outside of available methods")
    print(opList)