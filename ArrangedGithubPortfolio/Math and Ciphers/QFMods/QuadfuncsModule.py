import math

def Vertex2Standard(a,h,k):
	newA = a
	newH = h * -1
	FactorC = newH**2
	FactorB = newH + newH
	Distribute1 = FactorC * newA
	Distribute2 = FactorB * newA
	newK = k + Distribute1
	stringnewA = str(newA)
	stringDis2 = str(Distribute2)
	stringDis1 = str(newK)
	
	return("y=" + stringnewA + "x^2 + (" + stringDis2 + ")x + (" + stringDis1 + ")" )

def Standard2Vertex(a,b,c):
	rawh = -b / 2 * a
	k1 = 4 * a * c 
	k2 = b**2 * -1
	k3 = a * 4
	k4 = k1 + k2
	k5 = k4 / k3
	k = str(k5)
	h = str(rawh)
	stra = str(a)
	if rawh > 0:
		return("y=" + stra + "(x + " + " - " + h + ") + " + k)
	else:
		return("y=" + stra + "(x + " + " + " + h + ") + " + k)

def QuadraticFormulaFunc(a,b,c):
	denominator = 2 * a
	sqrpre = 4 * a * c
	bsqr = b ** 2
	negb = b * -1
	try:
		sqrootpart = math.sqrt(bsqr - sqrpre)
		preanswer1 = negb + sqrootpart
		preanswer2 = negb - sqrootpart
		answer1 = preanswer1 / denominator
		answer2 = preanswer2 / denominator
		if answer1 == answer2:
			return(answer1)
		else:
			return(answer1,answer2)
	except:
		negbstring = str(negb)
		bsqr1 = bsqr - sqrpre
		bsqr1string = str(bsqr1)
		denstring = str(denominator)
		return("      " + negbstring + "+- sqrt(" + bsqr1string + ")\nx= ----------------------\n" + "      " + denstring)

def DistanceFormula(x1,y1,x2,y2):
	xdiff = x2 - x1
	ydiff = y2 - y1
	xdiff2 = xdiff**2
	ydiff2 = ydiff**2
	sqrrootinterior = xdiff2 + ydiff2
	result = math.sqrt(sqrrootinterior)
	return(result)

def MidpointFormula(x1,y1,x2,y2):
	sumx = x1+x2
	sumy = y1+y2
	sumxdiv = sumx / 2
	sumydiv = sumy / 2
	return(sumxdiv,sumydiv)
