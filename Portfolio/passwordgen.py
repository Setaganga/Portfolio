#So this would seem like a lot for just a password generator, and it is. But I wanted to try and implement a strength
#checker. Because the generator occasionally wont put a symbol or number in it.
#So I used some regex things and made it not print out the password unless it was valid

#Getting stuff I need
from random import sample
from re import search

#Setting up variables
lcase = "abcdefghijklmnopqrstuvwxyz"
ucase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "0123456789"
syms = "~`! @#$%^&*()_-+={[}]|\:;'<,>.?/"
validchars = lcase + ucase + nums + syms
leng = 16
#While loops stops when this is true
#I wanted to style it like a do while loop, but python doesn't have those. Sad.
strengthcheck = False
password = ""

def StrengthTest(PW):
    PW = "".join(sorted(PW))
    con1 = search(r"[A-Z]",PW)
    con2 = search(r"[a-z]",PW)
    con3 = search(r"[\d]",PW)
    con4 = search(r"[\~\`\!\ \@\#\$\%\^\&\*\(\)\_\-\+\=\{\[\}\]\|\\\:\;\'\<\,\>\.\?\/]",PW) #I sure do love escape characters
    if con1 and con2 and con3 and con4:
        return True
    else:
        return False

def MakePassword():
    return "".join(sample(validchars,leng))

while strengthcheck != True:
    password = MakePassword() #Make password
    strengthcheck = StrengthTest(password) #Test strength, returns True or False

print(f"Your generated password is: {password}")
