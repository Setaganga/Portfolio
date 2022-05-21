def SGC(x,y):
    og = x.lower()
    new = ""
    letterList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in og:
        if i in letterList:
            tempNum = letterList.index(i)
            new += letterList[tempNum + y]
        else:
            new += i
        
    txtNew = new[::-1]
    if y > 9:
        txtNew += "[" + str(y) + "]"
    else:
        txtNew += " [" + str(y) + "]"
    return(txtNew)