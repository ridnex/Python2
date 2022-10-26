from tkinter import *
import math
root = Tk()
root.geometry("320x760") # casio size


string_for_equations = ''
result =''

def plus(x):
    global string_for_equations
    string_for_equations = string_for_equations+str(x)

def dele():
    global string_for_equations
    string_for_equations = string_for_equations[:-1]

def ac():
    global string_for_equations
    string_for_equations = ""

def out():
    print(string_for_equations)
    try:
        global output
        output = Label(root, text = str(eval(string_for_equations)), width = 20, height = 2)
        output.grid(row = 0, column = 0, columnspan = 7)
    except:
        output = Label(root, text = 'err', width = 20, height = 2)
        output.grid(row = 0, column = 0, columnspan = 7)




Button(root, bd = 10, font = 100, text = "sin", width = 5, height = 2, command= lambda: plus('math.sin')).grid(row = 1, column = 0)
Button(root, bd = 10, font = 100, text = "cos", width = 5, height = 2, command=lambda:plus('math.cos')).grid(row = 1, column = 1)
Button(root, bd = 10, font = 100, text = "tg", width = 5, height = 2, command=lambda:plus('math.tan')).grid(row = 1, column = 2)
Button(root, bd = 10, font = 100, text = "ctg", width = 5, height = 2, command=lambda:plus('1/math.tan')).grid(row = 1, column = 3)

Button(root, bd = 10, font = 100, text = "(", width = 5, height = 2,command=lambda:plus('(')).grid(row = 2, column = 0)
Button(root, bd = 10, font = 100, text = ")", width = 5, height = 2,command=lambda:plus(')')).grid(row = 2, column = 1)
Button(root, bd = 10, font = 100, text = "1/x", width = 5, height = 2, command=lambda:plus('1/')).grid(row = 2, column = 2)
Button(root, bd = 10, font = 100, text = "%", width = 5, height = 2,command=lambda:plus('/100')).grid(row = 2, column = 3)


Button(root, bd = 10, font = 100, text = "x^y", width = 5, height = 2,command=lambda:plus('**')).grid(row = 3, column = 0)
Button(root, bd = 10, font = 100, text = "√x", width = 5, height = 2, command=lambda:plus('math.sqrt')).grid(row = 3, column = 1)
Button(root, bd = 10, font = 100, text = "x!", width = 5, height = 2, command=lambda:plus('math.factorial')).grid(row =3, column = 2)
Button(root, bd = 10, font = 100, text = "+-", width = 5, height = 2, command=lambda:plus('*-1')).grid(row = 3, column = 3)


Button(root, bd = 10, font = 100, text = "ln", width = 5, height = 2, command=lambda:plus('math.log(math.e)')).grid(row = 4, column = 0)
Button(root, bd = 10, font = 100, text = "lg", width = 5, height = 2,command=lambda:plus('math.log(10)')).grid(row = 4, column = 1)
Button(root, bd = 10, font = 100, text = "e", width = 5, height = 2, command=lambda:plus('math.e')).grid(row =4, column = 2)
Button(root, bd = 10, font = 100, text = "e^x", width = 5, height = 2, command=lambda:plus('e**')).grid(row = 4, column = 3)


Button(root, bd = 10, font = 100, text = "del", width = 5, height = 2, command=dele).grid(row = 5, column = 1)
Button(root, bd = 10, font = 100, text = "degree", width = 5, height = 2, command=lambda:plus('math.degrees')).grid(row =5, column = 2)
Button(root, bd = 10, font = 100, text = "/", width = 5, height = 2, command=lambda:plus('/')).grid(row = 5, column = 3)


Button(root, bd = 10, font = 100, text = "7", width = 5, height = 2, command=lambda:plus('7')).grid(row = 6, column = 0)
Button(root, bd = 10, font = 100, text = "8", width = 5, height = 2, command=lambda:plus('8')).grid(row = 6, column = 1)
Button(root, bd = 10, font = 100, text = "9", width = 5, height = 2, command=lambda:plus('9')).grid(row = 6, column = 2)
Button(root, bd = 10, font = 100, text = "x", width = 5, height = 2, command=lambda:plus('*')).grid(row = 6, column = 3)


Button(root, bd = 10, font = 100, text = "4", width = 5, height = 2, command=lambda:plus(4)).grid(row = 7, column = 0)
Button(root, bd = 10, font = 100, text = "5", width = 5, height = 2,command=lambda:plus(5)).grid(row = 7, column = 1)
Button(root, bd = 10, font = 100, text = "6", width = 5, height = 2,command=lambda:plus('6')).grid(row = 7, column = 2)
Button(root, bd = 10, font = 100, text = "-", width = 5, height = 2, command=lambda:plus('-')).grid(row = 7, column = 3)


Button(root, bd = 10, font = 100, text = "1", width = 5, height = 2, command=lambda:plus('1')).grid(row = 8, column = 0)
Button(root, bd = 10, font = 100, text = "2", width = 5, height = 2, command=lambda:plus('2')).grid(row = 8, column = 1)
Button(root, bd = 10, font = 100, text = "3", width = 5, height = 2, command=lambda:plus('3')).grid(row = 8, column = 2)
Button(root, bd = 10, font = 100, text = "+", width = 5, height = 2,command=lambda:plus('+')).grid(row = 8, column = 3)


Button(root, bd = 10, font = 100, text = "pi", width = 5, height = 2, command=lambda:plus('math.pi')).grid(row = 9, column = 0)
Button(root, bd = 10, font = 100, text = "0", width = 5, height = 2, command=lambda:plus('0')).grid(row = 9, column = 1)
Button(root, bd = 10, font = 100, text = ".", width = 5, height = 2, command=lambda:plus(".")).grid(row = 9, column = 2)
Button(root, bd = 10, font = 100, text = "Ac", width = 5, height = 2, command=ac).grid(row = 5, column = 0)

Button(root, bd = 10, font = 100, text = "=", width = 5, height = 2, command=out).grid(row = 9, column = 3)


root.mainloop()
