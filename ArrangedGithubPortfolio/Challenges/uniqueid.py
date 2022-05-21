#The challenge said that a company made Unique Identification Numbers and needed to check if an ID was valid
#The ID required: Length of 10 chars, Made only of Alphanum chars, have at least 3 numbers, have at least 2 capital
#letters, and make sure no characters repeat

#Below is an example of how the input works and what result it should give
#2
#B1CD102354 - Invalid (because it has repeating 1)
#B1CDEF2354 - Valid (meets all requirements)
import re
def Validate(UID):
    if len(UID) == 10 and re.search("^[a-zA-Z0-9]*$",UID) and re.search("[0-9]{3,}",UID) and re.search("[A-Z]{2,}",UID):
        val = True
        for character in UID:
            if UID.count(character) > 1:
                val = False
                break
        if val == True:
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")


for x in range(int(input())):
    Validate(''.join(sorted(input())))