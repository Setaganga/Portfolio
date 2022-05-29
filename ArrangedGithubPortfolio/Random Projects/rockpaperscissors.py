#Ah, a classic game of Rock Paper Scissors. It's too bad the code design is a nightmare for games like these
from random import sample
userchoice = ""
botletters = "RPS"

while True: #Force user to not be dumb
    userchoice = input("R,P, or S? ")
    if userchoice == "R" or userchoice == "P" or userchoice == "S":
        break

botchoice = "".join(sample(botletters,1))
print("\n")
if userchoice == "R":
    if botchoice == "R":
        print(f"Draw with (User:{userchoice} Bot:{botchoice})")
    elif botchoice == "P":
        print(f"Bot wins with (User:{userchoice} Bot:{botchoice})")
    else:
        print(f"User wins with (User:{userchoice} Bot:{botchoice})")

elif userchoice == "P":
    if botchoice == "R":
        print(f"User wins with (User:{userchoice} Bot:{botchoice})")
    elif botchoice == "P":
        print(f"Draw with (User:{userchoice} Bot:{botchoice})")
    else:
        print(f"Bot wins with (User:{userchoice} Bot:{botchoice})")

else:
    if botchoice == "R":
        print(f"Bot wins with (User:{userchoice} Bot:{botchoice})")
    elif botchoice == "P":
        print(f"User wins with (User:{userchoice} Bot:{botchoice})")
    else:
        print(f"Draw with (User:{userchoice} Bot:{botchoice})")