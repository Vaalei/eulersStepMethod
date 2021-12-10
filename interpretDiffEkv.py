# Made only to interpret the differential equation


def splitEquations(equation):
    separated = []
    temp = ""
    for i in equation:
        if i == "+" or i == "-":
            separated.append(temp)
            temp = i
        else:
            temp+=i
    separated.append(temp)
    if separated[0] == "": separated.pop(0)
    return separated

def removeLetters(string):
    list = []
    for i in string:
        if not i.isalpha():
            list.append(i)
    strvalue = "".join(list)
    if strvalue == "-" or strvalue == "+" or strvalue == "": strvalue += "1"
    return  float(strvalue)

def getXYvalues(ekv):
    splitted = splitEquations(ekv)
    x = 0
    y = 0
    for i in splitted:
        amount = removeLetters(i)
        for j in i:
            if j == "x": x+=amount
            if j == "y": y+=amount
    return x, y

# ekv = input("Diff ekv")
ekv = "-y+2x"  # = y'


values = getXYvalues(ekv)

print("Equation:",ekv)
print("x:", values[0], "\ny:", values[1])






