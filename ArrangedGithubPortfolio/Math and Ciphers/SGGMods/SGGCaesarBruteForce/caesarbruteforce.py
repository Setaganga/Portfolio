#Hey! Thanks for using SGG's Caesarbruteforce!
def cbfRun(inString):
    cText = inString.lower()
    for r in range(0,26):
        new = ""
        letterList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        for i in cText:
            if i in letterList:
                tempNum = letterList.index(i)
                new += letterList[tempNum - r]
            else:
                new += i
        new += "[{}]".format(r)
        print(new)

    print("Search for your text, and thank you for using SGG Caesar Brute Force")