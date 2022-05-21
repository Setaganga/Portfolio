import SGGen as sge
newInput = raw_input("Enter:")
newShift = int(raw_input("Enter shift code:"))
if newShift > 26:
    print("Not valid number!")
elif newShift < 0:
    print("Not valid number!")
else:
    print(sge.Encode(newInput,newShift))