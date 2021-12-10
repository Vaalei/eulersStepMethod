from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext as st
from webbrowser import open_new


# Colours
BGCOLOUR = "#010409"
def rgb(rgb):
    # translates an rgb tuple of int to a tkinter friendly color code
    return "#%02x%02x%02x" % rgb 

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
    return float(strvalue)

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

def stepMethod(x, y, startValue, toNumber, differance):
    if differance == 0:
        return "Error: Step size cannot be 0"
    currentValue = startValue
    a = 0
    while a <= toNumber:
        yprim = currentValue*y*differance+x*differance
        currentValue += yprim
        a+=differance
    return currentValue

def calculate():
    showOutput = True

    startValue = inputField.get("1.0", END); startValue = removeLetters(startValue)
    toNumber = toNumberField.get("1.0", END); toNumber = removeLetters(toNumber)
    diffEkv = diffEkvField.get("1.0", END); diffEkv = diffEkv.replace("\n", "")
    stepSize = stepSizeField.get("1.0", END); stepSize = removeLetters(stepSize)
    x, y = getXYvalues(diffEkv)
    
    if showOutput:
        print("Startvalue:\t",startValue)
        print("To number:\t",toNumber)
        print("Diff ekv:\t",diffEkv)
        print("Stepsize:\t",stepSize)
        print("x:\t",x)
        print("y:\t",y)

    output = stepMethod(startValue=startValue, toNumber = toNumber, x=x, y=y, differance=stepSize)
    if showOutput:
        print(output)

    outputField.delete("1.0","end")
    outputField.insert("1.0", output)


# Main window
root = Tk()
#root.geometry("550x230")
root.title("Eulers stepmethod @Vaalei")
root.configure(
    background=BGCOLOUR
)
root.iconbitmap("./pictures/main.ico")

style = ttk.Style()
style.theme_use('alt')
style.configure("BW.TLabel", 
    foreground="white", 
    background=BGCOLOUR,
    font= "helvetica 10 bold"
)

style.configure(
    "BW.TButton",
    borderwidth=5,
    border=rgb((20,20,20)),
    background=BGCOLOUR,
    foreground="white",
    font="helvetica 10 bold"
)
style.map('TButton', background=[('active', BGCOLOUR)])

style.configure(
    "Github.TLabel",
    foreground="blue",
    font="Helvetica 11",
    background=BGCOLOUR
)

# Title
title = ttk.Label(root, style="BW.TLabel", text="Eulers stepmethod", font="Helvetica 18 bold", padding=10)
title.grid(column=0, row=0)


# Input
inputTitle = ttk.Label(root, style="BW.TLabel", text="Input", font="Helvetica 18 bold", padding=10)
inputTitle.grid(column=0, row=1)

inputField = Text(root, width=25, height=5, font=("Helvetica", 10))
inputField.grid(column=0, row=2)


# Output
outputTitle = ttk.Label(root, style="BW.TLabel", text="Output", font="Helvetica 18 bold", padding=10)
outputTitle.grid(column=2, row=1)

outputField = Text(root, width=25, height=5, font=("Helvetica", 10))
outputField.grid(column=2, row=2)


# Options
title = ttk.Label(root, style="BW.TLabel", text="Options", font="Helvetica 16 bold", padding=10)
title.grid(column=0, row=3)

    # Step size
title = ttk.Label(root, style="BW.TLabel", text="Step size", font="Helvetica 13 bold", padding=3)
title.grid(column=0, row=4)
stepSizeField = Text(root, width=25, height=1, font=("Helvetica", 10))
stepSizeField.grid(column=2, row=4)

    # To Number
title = ttk.Label(root, style="BW.TLabel", text="To Number", font="Helvetica 13 bold", padding=3)
title.grid(column=0, row=5)
toNumberField = Text(root, width=25, height=1, font=("Helvetica", 10))
toNumberField.grid(column=2, row=5)

    # diff ekvation, c
title = ttk.Label(root, style="BW.TLabel", text="DiffEkv, y':", font="Helvetica 13 bold", padding=3)
title.grid(column=0, row=6)
diffEkvField = Text(root, width=25, height=1, font=("Helvetica", 10))
diffEkvField.grid(column=2, row=6)

# Calculate
calculateButton = ttk.Button(root, style="BW.TButton", text="Calculate", padding=5, command=lambda: calculate(), cursor="hand2")
calculateButton.grid(column=2, row=3)


# Padding

ttk.Label(root, style="BW.TLabel", text="").grid(column=0, row=98)          # Before Github link
ttk.Label(root, style="BW.TLabel", text="     ").grid(column=99,row=100)    # Make a margin bottom right


# Github
github = ttk.Label(root, style="Github.TLabel", text="Github @Vaalei", cursor="hand2", padding= 10)
github.grid(column=0,row=99)
github.bind("<Button-1>", lambda e: open_new("https://github.com/Vaalei"))



root.mainloop()