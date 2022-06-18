#For info about challenge, please visit: 
#https://www.hackerrank.com/challenges/validating-credit-card-number/

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