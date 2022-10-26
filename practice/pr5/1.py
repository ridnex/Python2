from cProfile import label
from tkinter import *
root = Tk()
def button_fuc(event):
    print("HEKKOOOO")
    new_wind = Tk()
    label(new_wind, text= "Fjk").pack()
    new_wind.mainloop()
E1 = Entry(root)
E1.pack()
widget = Label(root, text="GG")
widget.pack(side=RIGHT)
B = Button(root, text="LOE")
B.bind('<Button-1>', button_fuc)

B.pack()
root.mainloop()