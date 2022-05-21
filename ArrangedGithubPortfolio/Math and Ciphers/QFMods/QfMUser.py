import QuadfuncsModule

def RunS2V():
    print("Currently Running Standard Form to Vertex Form Calculator\nPlease choose an A, B, and C.")
    inputa = input("a:")
    inputb = input("b:")
    inputc = input("c:")
    print("Processing function currently, will return result with data of:" + inputa + "," + inputb + ", and " + inputc)
    senda = float(inputa)
    sendb = float(inputb)
    sendc = float(inputc)
    print(QuadfuncsModule.Standard2Vertex(senda,sendb,sendc))
    print("^^Your equation is right here^^\nThank you for using Fossilmilk's QuadfuncsModule!")

def RunV2S():
    print("Currently Running Vertex Form to Standard Form Calculator\nPlease choose an A, H, and K.")
    inputa = input("a:")
    inputh = input("h:")
    inputk = input("k:")
    print("Processing function currently, will return result with data of:" + inputa + "," + inputh + ", and " + inputk)
    senda = float(inputa)
    sendh = float(inputh)
    sendk = float(inputk)
    print(QuadfuncsModule.Vertex2Standard(senda,sendh,sendk))
    print("^^Your equation is right here^^\nThank you for using Fossilmilk's QuadfuncsModule!")

def RunQF():
    print("Currently Running Quadratic Formula\nPlease choose an A, B, and C.")
    inputa = input("a:")
    inputb = input("b:")
    inputc = input("c:")
    print("Processing function currently, will return result with data of:" + inputa + "," + inputb + ", and " + inputc)
    senda = float(inputa)
    sendb = float(inputb)
    sendc = float(inputc)
    print(QuadfuncsModule.QuadraticFormulaFunc(senda,sendb,sendc))
    print("^^Your answers are right here^^\nThank you for using Fossilmilk's QuadfuncsModule!")

def RunDF():
    print("Currently Running Distance Formula\nPlease choose an x1, y1, x2, and y2.")
    inputx1 = input("x1:")
    inputy1 = input("y1:")
    inputx2 = input("x2:")
    inputy2 = input("y2:")
    print("Processing function currently, will return result with data of:" + inputx1 + "," + inputy1 + "," + inputx2 + ", and " + inputy2)
    sendx1 = float(inputx1)
    sendy1 = float(inputy1)
    sendx2 = float(inputx2)
    sendy2 = float(inputy2)
    print(QuadfuncsModule.DistanceFormula(sendx1,sendy1,sendx2,sendy2))
    print("^^Your answers are right here^^\nThank you for using Fossilmilk's QuadfuncsModule!")

def RunMF():
    print("Currently Running Midpoint Formula\nPlease choose an x1, y1, x2, and y2.")
    inputx1 = input("x1:")
    inputy1 = input("y1:")
    inputx2 = input("x2:")
    inputy2 = input("y2:")
    print("Processing function currently, will return result with data of:" + inputx1 + "," + inputy1 + "," + inputx2 + ", and " + inputy2)
    sendx1 = float(inputx1)
    sendy1 = float(inputy1)
    sendx2 = float(inputx2)
    sendy2 = float(inputy2)
    print(QuadfuncsModule.MidpointFormula(sendx1,sendy1,sendx2,sendy2))
    print("^^Your answers are right here^^\nThank you for using Fossilmilk's QuadfuncsModule!")

def Run():
    chooseVS = input("Choose either 1, 2, 3, 4, or 5:\nStandard2Vertex, Vertex2Standard, QuadraticFormula,\nDistanceFormula or MidpointFormula: ")
    if chooseVS == "1":
        RunS2V()
    elif chooseVS == "2":
        RunV2S()
    elif chooseVS == "3":
        RunQF()
    elif chooseVS == "4":
        RunDF()
    elif chooseVS == "5":
        RunMF()
    else:
        print("Not a valid input, try again.")
        Run()


Run()