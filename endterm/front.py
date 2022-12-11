from tkinter import * 
from tkinter import ttk 
from PIL import ImageTk, Image
from back import *
from tkinter import messagebox as mb 
import numpy as np

class WindowApp(Tk): 

    def __init__(self): 
        Tk.__init__(self) 
        self.basic = Frame(self)

        image1 = Image.open("main.jpg")
        test  = ImageTk.PhotoImage(image1)
        self.geometry('1200x675')
        label1 =  Label(self.basic, image= test)
        label1.image = test
        label1.place(x=0, y=0)
        self.basic.pack(fill = 'both', expand = 1)


        Label2 = Label(self.basic, text = 'SVD', bg ='#BDE4F4', fg = "#10316B", font = ('Papyrus', 15),  width=17, height=2)
        Label2.place(x=700, y=50)
        But1 = Button(self.basic, bd = 5, text = 'Theory',command = self.switch_to_theory,  bg ='#BDE4F4', font = ('Papyrus', 15), fg = "#10316B",  width=17,height=2, border = 2)
        But1.place(x=700, y=150)
        But2 = Button(self.basic, bd = 5, text = 'Solve',command = self.switch_to_matrix,  bg ='#BDE4F4', font = ('Papyrus', 15), fg = "#10316B",  width=17,height=2, border = 2)
        But2.place(x=700, y=250)
        
    def switch_to_matrix(self):
        self.basic.forget()  
        
        Matrix.pack(fill = 'both', expand = 1)

    def switch_to_theory(self):
        self.basic.forget()  
        
        Theory.pack(fill = 'both', expand = 1)

    def switch_to_main(self):
        Theory.forget()  
        Matrix.forget()
        self.basic.pack(fill = 'both', expand = 1)   

        
         
class MatrixScreen(Frame): 
 
    def __init__(self, root): 
        Frame.__init__(self, root, bg = '#FFF7E9') 

        image1 = Image.open("main.jpg")
        test  = ImageTk.PhotoImage(image1)
        label1 =  Label(self, image= test)
        label1.image = test
        label1.place(x=0, y=0)
        
        
        Label1 = Label(self, text = 'Matrix', bg ='#BDE4F4', fg = "#10316B", font = ('Papyrus', 15),  width=17, height=2)
        Label1.place(x=600, y=50)

        # def answer(matrix):
        #     matrix = np.array(matrix)
        #     square1 = square_matrix(matrix, mod1)
        #     Matrix_V = np.array(overall(square1, 5))

        #     Matrix_VV = np.transpose(Matrix_V)

        #     Matrix_D = np.array(diogonal(square1))

        #     Matrix_DD = np.array(inverse_diogonal(square1))

        #     Matrix_AVV = np.matmul(matrix, Matrix_VV)
        #     Matrix_B = np.matmul(Matrix_AVV, Matrix_DD)


        #     Matrix_BD = np.matmul(Matrix_B, Matrix_D)
        #     Matrix_BDV = np.matmul(Matrix_BD, Matrix_V)

        #     txt_ans = ''
        #     txt_ans += f" matrix B:\n {Matrix_B}\n\n"
        #     txt_ans += f" matrix D:\n {Matrix_D}\n\n"
        #     txt_ans += f" matrix D:\n {Matrix_V}\n\n"
        #     print(txt_ans)
           
        
        def get_mat():
            
            matrix = []
            for i in range(rows):
                matrix.append([])
                for j in range(cols):
                    matrix[i].append(text_var[i][j].get())

            matrix = np.array(matrix)
            print(matrix)

        
        text_var = []
        entries = []
        x2 = 0
        y2 = 0
        rows, cols = (3,3)
        for i in range(rows):
            # append an empty list to your two arrays
            # so you can append to those later
            text_var.append([])
            entries.append([])
            for j in range(cols):
                # append your StringVar and Entry
                text_var[i].append(StringVar())
                entries[i].append(Entry(self, textvariable=text_var[i][j],width=3))
                entries[i][j].place(x=650 + x2, y=200 + y2)
                x2 += 80

            y2 += 80
            x2 = 0
                    


        value_button1 = Button(self, text = 'SVD solve',font = ('Papyrus', 15), width = 20, command=get_mat)
        value_button1.place(x=900, y=250)

        But1 = Button(self, bd = 5, text = 'Back',command = Main.switch_to_main,  bg ='#BDE4F4', font = ('Papyrus', 13), fg = "#10316B",  width=20,height=2, border = 2)
        But1.place(x=900, y=50)

        



class TheoryScreen(Frame): 
 
    def __init__(self, root): 
        Frame.__init__(self, root, bg = '#FFF7E9') 

        image1 = Image.open("main.jpg")
        test  = ImageTk.PhotoImage(image1)
        label1 =  Label(self, image= test)
        label1.image = test
        label1.place(x=0, y=0)

        image2 = Image.open("theory.jpg")
        test1  = ImageTk.PhotoImage(image2)
        label2 =  Label(self, image= test1)
        label2.image = test1
        label2.place(x=0, y=0)
        
        
        Label1 = Label(self, text = 'SVD', bg ='#BDE4F4', fg = "#10316B", font = ('Papyrus', 15),  width=17, height=2)
        Label1.place(x=950, y=300)
        
        But1 = Button(self, bd = 5, text = 'Back',command = Main.switch_to_main,  bg ='#BDE4F4', font = ('Papyrus', 13), fg = "#10316B",  width=20,height=2, border = 2)
        But1.place(x=950, y=400)

Main = WindowApp() 
Matrix = MatrixScreen(Main)
Theory = TheoryScreen(Main)
Main.mainloop()

