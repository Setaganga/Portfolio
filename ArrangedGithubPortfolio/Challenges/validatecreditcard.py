import re
def Validate(cc):
    if not re.search("^[456]\d{3}(-?\d{4}){3}$",cc):
        print("Invalid Case 1")
    elif re.search(r"(\d)\1{3}", re.sub("-", "",cc)):
        print("Invalid Case 2")
    else:
        print("Valid")
for _ in range(int(input())):
    Validate(input())

#Invalid Case 1 checks to see if it is formatted right
#Invalid Case 2 checks to see if there are any 4 or more consecutive numbers

#6
#4123456789123456
#5123-4567-8912-3456
#61234-567-8912-3456
#4123356789123456
#5133-3367-8912-3456
#5123 - 3567 - 8912 - 3456

#V - Valid
#V - Valid
#I -  Invalid because they do not divide into equal groups of 4
#V - Valid
#I - Invalid because 3333 repeats
#I - Invalid because spaces are used as separators