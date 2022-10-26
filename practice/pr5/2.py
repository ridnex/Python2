from tkinter import *
root = Tk()
L1 = Label(root, text ='Welcome')
L1.pack()
dicttt = {'wer':1451, 'cscc' : 21}

E1 = Entry(root)
E1.pack()
E2 = Entry(root)
E2.pack()

def button_func(event):
    varible = E1.get()
    password = int(E2.get())
    if varible not in dicttt :
        new_wind = Tk()
        L2 = Label(new_wind, text= "LOGIN NOT FOUNDED")
        L2.pack()
        new_wind.mainloop()
    elif dicttt[varible]!=password:
        new_wind = Tk()
        L3 = Label(new_wind, text= "PASSWORD IS NOT CORRECT")
        L3.pack()
        new_wind.mainloop()
    else:
        new_wind = Tk()
        L4 = Label(new_wind, text= "GOOD JOB")
        L4.pack()
        new_wind.mainloop()




B = Button(root, text="press")
B.bind('<Button-1>', button_func)

B.pack()
root.mainloop()


