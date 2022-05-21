import SGGCaesar as sgc

def SGT(x,y):
    og = x.lower()
    new = ""
    for i in og:
        if (i == "a"):
            new += "z"
        elif (i == "b"):
            new += "y"
        elif (i == "c"):
            new += "x"
        elif (i == "d"):
            new += "w"
        elif (i == "e"):
            new += "v"
        elif (i == "f"):
            new += "u"
        elif (i == "g"):
            new += "t"
        elif (i == "h"):
            new += "s"
        elif (i == "i"):
            new += "r"
        elif (i == "j"):
            new += "q"
        elif (i == "k"):
            new += "p"
        elif (i == "l"):
            new += "o"
        elif (i == "m"):
            new += "n"
        elif (i == "n"):
            new += "m"
        elif (i == "o"):
            new += "l"
        elif (i == "p"):
            new += "k"
        elif (i == "q"):
            new += "j"
        elif (i == "r"):
            new += "i"
        elif (i == "s"):
            new += "h"
        elif (i == "t"):
            new += "g"
        elif (i == "u"):
            new += "f"
        elif (i == "v"):
            new += "e"
        elif (i == "w"):
            new += "d"
        elif (i == "x"):
            new += "c"
        elif (i == "y"):
            new += "b"
        elif (i == "z"):
            new += "a"
        else:
            new += i
        
    return(sgc.SGC(new,y))
