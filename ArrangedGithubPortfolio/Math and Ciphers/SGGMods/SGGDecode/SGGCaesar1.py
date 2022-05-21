import SGGTrans1

def SGC(x,y):
    og = x.lower()
    txtNew = og[::-1]
    new = ""
    letterList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in txtNew:
        if i in letterList:
            tempNum = letterList.index(i)
            new += letterList[tempNum - y]
        else:
            new += i
        
    return(SGGTrans1.SGT(new))