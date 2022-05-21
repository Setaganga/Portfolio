import SGGde as sgd
newInput = raw_input("Enter:")
newShift = int(raw_input("Enter shift code:"))
if newShift > 26:
    print("Not valid number!")
elif newShift < 0:
    print("Not valid number!")
else:
    coolString = sgd.Decode(newInput,newShift)
    lenOString = len(coolString)
    print(coolString[4:lenOString])