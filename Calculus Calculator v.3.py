'''
Thanks to:
https//www.pythonistaplanet.com/tkinter/
https://stackoverflow.com/questions/4999006/factor-a-quadratic-polynomial-in-python

Fix DOS, and Decomposistion
Make DOS/SOS Seperate Functions
'''


from fractions import *
from gcd import *
from PIL import Image,ImageTk
from math import sqrt
from functools import reduce
import tkinter as tk
import random as rand
import time
import matplotlib
main_bg_colour = 'white'
button_fg_colour = 'white'
button_bg_colour = 'black'
root = tk.Tk()
root.title(" Fraction Calculator ")
root.geometry('1100x600')
root.configure(background=main_bg_colour)
button_width=25


def Button_Cut(): # Hides The Buttons When An Option Is Entered
    Addition_Input_button_POS.grid_forget()    
    Subtraction_Input_button_POS.grid_forget()
    Multiplication_Input_button_POS.grid_forget()
    Division_Input_button_POS.grid_forget()
    Custom_Root_Input_button_POS.grid_forget()
    Decomposostion_Input_button_POS.grid_forget()
    DOS_Input_button_POS.grid_forget()
    DOC_Input_button_POS.grid_forget()
    SOC_Input_button_POS.grid_forget()


def Button_Paste(): # Adds The Buttons When The Result Is Cleared
    Addition_Input_button_POS.grid(column=1, row=0)   
    Subtraction_Input_button_POS.grid(column=2, row=0)
    Multiplication_Input_button_POS.grid(column=3, row=0)
    Division_Input_button_POS.grid(column=4, row=0)
    Custom_Root_Input_button_POS.grid(column=8, row=0)
    Decomposostion_Input_button_POS.grid(column=9, row=0)
    DOS_Input_button_POS.grid(column=1, row=1)
    DOC_Input_button_POS.grid(column=2, row=1)
    SOC_Input_button_POS.grid(column=3, row=1)
    root.unbind("<Return>")

    
def RES_Clear(A, B, C, D, RES_label1, RES_label2, question_entry, question_label): # Clears The Result, And Calls button Paste
    RES_label1.grid_forget()
    RES_label2.grid_forget()
    question_entry.grid_forget()
    question_label.grid_forget()
    Button_Paste()


def Enter(A, B, question_entry, question_label, RES): # Responsible For Displaying The Answer
    RES_label1= tk.Label(text = "The result is:")
     
    RES_label2= tk.Label(text = (str(RES)))
    
    RES_label1.configure(background=main_bg_colour)
    RES_label1.grid(column=3,row=2)

    RES_label2.configure(background=main_bg_colour)
    RES_label2.grid(column=4,row=2)

    root.bind('<Return>', lambda event, C=RES_label1, D=RES_label2: 
            RES_Clear(A, B, C, D, question_entry, question_label, RES_label1, RES_label2))


def Addition_Input(): # Handles Input For Addition
    Button_Cut()
    
    question_entry = tk.Entry()
    question_entry.configure(background='light gray')
    question_entry.grid(column=1,row=2)

    question_label = tk.Label(text = "Enter the numbers you want to add, sperated by spaces.")
    question_label.configure(background=main_bg_colour)
    question_label.grid(column=0,row=2)
    
    root.bind('<Return>', lambda event, A=question_entry, B=question_label:  
            Addition(A, B, question_entry, question_label))

    
def Addition(A, B, question_entry, question_label): # Handles Math For Addition
    question_input=(A.get())
    question_intList = [eval(i) for i in question_input.split(" ")]
    RES=reduce((lambda x, y: x + y), question_intList)
    
    Enter(A, B, question_entry, question_label, RES)


def Subtraction_Input(): # Handles Input For Subtraction
    Button_Cut()
    
    question_entry = tk.Entry()
    question_entry.configure(background='light gray')
    question_entry.grid(column=1,row=2)

    question_label = tk.Label(text = "Enter the numbers you want to subtract, sperated by spaces.")
    question_label.configure(background=main_bg_colour)
    question_label.grid(column=0,row=2), main_bg_colour
    question_label.grid(column=0,row=2)

    question_input=(question_entry.get())

    root.bind('<Return>', lambda event, A=question_entry, B=question_label:  
            Subtraction(A, B, question_entry, question_label))


def Subtraction(A, B, question_entry, question_label): # Handles Math FOr Subtraction
    question_input=(A.get())
    question_intList = [eval(i) for i in question_input.split(" ")]
    RES=reduce((lambda x, y: x - y), question_intList)
 
    Enter(A, B, question_entry, question_label, RES)


def Multiplication_Input(): # Handles Input For Multiplication
    Button_Cut()
    
    question_entry = tk.Entry()
    question_entry.configure(background='light gray')
    question_entry.grid(column=1,row=2)

    question_label = tk.Label(text = "Enter the numbers you want to multiply, sperated by spaces.")
    question_label.configure(background=main_bg_colour)
    question_label.grid(column=0,row=2)

    question_input=(question_entry.get())

    root.bind('<Return>', lambda event, A=question_entry, B=question_label:  
            Multiplication(A, B, question_entry, question_label))

    
def Multiplication(A, B, question_entry, question_label): # Handles Math For Multiplication
    question_input=(A.get())
    question_intList = [eval(i) for i in question_input.split(" ")]
    RES=reduce((lambda x, y: x * y), question_intList)

    Enter(A, B, question_entry, question_label, RES)
    

def Division_Input(): # Handles Input For Division
    Button_Cut()
    
    question_entry = tk.Entry()
    question_entry.configure(background='light gray')
    question_entry.grid(column=1,row=2)

    question_label = tk.Label(text = "Enter the numbers you want to divide, sperated by spaces.")
    question_label.configure(background=main_bg_colour)
    question_label.grid(column=0,row=2)

    question_input=(question_entry.get())

    root.bind('<Return>', lambda event, A=question_entry, B=question_label:  
            Division(A, B, question_entry, question_label))


def Division(A, B, question_entry, question_label): # Handles Math For Division
    question_input=(A.get())
    question_input=(question_entry.get())
    question_intList = [eval(i) for i in question_input.split(" ")]
    RES=reduce((lambda x, y: x / y), question_intList)
    
    Enter(A, B, question_entry, question_label, RES)


def Custom_Root_Input(): # Handles Input For Custom Root
    Button_Cut()
    
    question_entry = tk.Entry()
    question_entry.configure(background='light gray')
    question_entry.grid(column=1,row=2)

    question_label = tk.Label(text = "A**(1/B) A is second number, B is first. sperate by spaces.")
    question_label.configure(background=main_bg_colour)
    question_label.grid(column=0,row=2)

    question_input=(question_entry.get())

    root.bind('<Return>', lambda event, A=question_entry, B=question_label:  
            Custom_Root(A, B, question_entry, question_label))


def Custom_Root(A, B, question_entry, question_label): # Handles Math For Custom Root
    question_input=(A.get())
    question_intList = [eval(i) for i in question_input.split(" ")]
    RES=reduce((lambda x, y: x ** (1/y)), question_intList)
    
    Enter(A, B, question_entry, question_label, RES)
    

def Decomposistion_Input(): # Handles Input For Decomposistion
    Button_Cut()
    
    question_entry = tk.Entry()
    question_entry.configure(background='light gray')
    question_entry.grid(column=1,row=2)

    question_label = tk.Label(text = "Example: 2x^2 -2x -4 would be 2 -2 -4")
    question_label.configure(background=main_bg_colour)
    question_label.grid(column=0,row=2)

    question_input=(question_entry.get())

    root.bind('<Return>', lambda event, A=question_entry, B=question_label:  
            Decomposistion(A, B, question_entry, question_label))


        
def Decomposistion(A, B, question_entry, question_label): # Handles Math For Decomposistion
    question_input=(A.get())
    question_intList = [(i) for i in question_input.split(" ")]

    a=(eval(question_intList[0]))
    b=(eval(question_intList[1]))
    c=(eval(question_intList[2]))
    X=True
    
    if (b**2-4*a*c >= 0):
        x1 = (-b+sqrt(b**2-4*a*c))/(2*a)
        x2 = (-b-sqrt(b**2-4*a*c))/(2*a)
        mult1 = -x1 * a
        mult2 = -x2 * a
        (num1,den1) = simplify_fraction(a,mult1)
        (num2,den2) = simplify_fraction(a,mult2)
        if ((num1 > a) or (num2 > a)):
            RES=("No factorization")
        else:
            if (den1 > 0):
                sign1 = "+"
            else:
                sign1 = ""
            if (den2 > 0):
                sign2 = "+"
            else:
                sign2 = ""
            RES=("({}x{}{})({}x{}{})".format(int(num1),sign1,int(den1),int(num2),sign2,int(den2)))
    else:
        RES=("Solutions are imaginary")         
            
    Enter(A, B, question_entry, question_label, RES)
    

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def simplify_fraction(numer, denom):
    if denom == 0:
        return "Division by 0 - result undefined"
    common_divisor = gcd(numer, denom)
    (reduced_num, reduced_den) = (numer / common_divisor, denom / common_divisor)

    if common_divisor == 1:
        return (numer, denom)
    else:
        if (reduced_den > denom):
            if (reduced_den * reduced_num < 0):
                return(-reduced_num, -reduced_den)
            else:
                return (reduced_num, reduced_den)
        else:
            return (reduced_num, reduced_den)

        
def DOS_Input(): # Handles Input For DOS (Diffrence Of Squares)
    Button_Cut()
    
    question_entry = tk.Entry()
    question_entry.configure(background='light gray')
    question_entry.grid(column=1,row=2)

    question_label = tk.Label(text = "Enter the LC and the Constant seperated by spaces in that order:")
    question_label.configure(background=main_bg_colour)
    question_label.grid(column=0,row=2)

    question_input=(question_entry.get())

    root.bind('<Return>', lambda event, A=question_entry, B=question_label:  
        DOS(A, B, question_entry, question_label))


def DOS(A, B, question_entry, question_label): # Handles Math For DOS (Diffrence Of Squares)
    question_input=(A.get())
    question_intList = [(i) for i in question_input.split(" ")]

    Degree=2
    LC=eval(question_intList[0])
    Constant=eval(question_intList[1])
    
    New_LC=str(((LC)**(1/Degree)))
    
    Pos_New_Constant=str(((Constant*-1)**(1/Degree)))
    Neg_New_Constant=str(((Constant*-1)**(1/Degree))*-1)
    
    RES=('('+(New_LC)+'x+'+Pos_New_Constant+')('+(New_LC)+'x'+Neg_New_Constant+')')

    Enter(A, B, question_entry, question_label, RES)


def DOC_Input(): # Handles Input For DOC (Diffrence Of Cubes)
    Button_Cut()
    
    question_entry = tk.Entry()
    question_entry.configure(background='light gray')
    question_entry.grid(column=1,row=2)

    question_label = tk.Label(text = "Enter the LC and the Constnt seperated by spaces in that order:")
    question_label.configure(background=main_bg_colour)
    question_label.grid(column=0,row=2)

    question_input=(question_entry.get())

    root.bind('<Return>', lambda event, A=question_entry, B=question_label:  
        DOC(A, B, question_entry, question_label))

    
def DOC(A, B, question_entry, question_label): # Handles Math For DOC (Diffrence Of Cubes)
    question_input=(A.get())
    question_intList = [(i) for i in question_input.split(" ")]
    
    degree=3
    LC=float(question_intList[0])
    Constant=float(question_intList[1])
    
    New_Constant=(((Constant*-1)**(1/degree)))
    print(New_Constant)
    
    New_LC=((LC**(1/degree)))
    print(New_LC)

    RES=('(x - '+str(New_Constant)+')('+str(New_LC)+'x^2 + '+str(New_LC*New_Constant)+'x - '+str((New_Constant)**2)+')')
          
    Enter(A, B, question_entry, question_label, RES)


def SOC_Input(): # Handles Input For Sum Of Cubes
    Button_Cut()
    
    question_entry = tk.Entry()
    question_entry.configure(background='light gray')
    question_entry.grid(column=1,row=2)

    question_label = tk.Label(text = "Enter the LC and the Constnt seperated by spaces in that order:")
    question_label.configure(background=main_bg_colour)
    question_label.grid(column=0,row=2)

    question_input=(question_entry.get())

    root.bind('<Return>', lambda event, A=question_entry, B=question_label:  
        SOC(A, B, question_entry, question_label))

    
def SOC(A, B, question_entry, question_label): # Handles Math For Sum Of Cubes
    question_input=(A.get())
    question_intList = [(i) for i in question_input.split(" ")]
    
    degree=3
    
    LC=float(question_intList[0])
    Constant=float(question_intList[1])
    
    New_Constant=((Constant**(1/degree)))
    
    New_LC=((LC**(1/degree)))
    
    RES=('(x + '+str(New_Constant)+')('+str(New_LC)+'x^2 - '+str(New_LC*New_Constant)+'x + '+str((New_Constant)**2)+')')
        
    Enter(A, B, question_entry, question_label, RES)


# Creates Buttons
SOC_Input_button_POS=tk.Button(text='Sum Of Cubes', command=SOC_Input, bg=button_bg_colour, fg=button_fg_colour, font=('Comic Sans', 9, 'bold'),width=button_width)
SOC_Input_button_POS.grid(column=3, row=1)

DOC_Input_button_POS=tk.Button(text='Diffrence Of Cubes', command=DOC_Input, bg=button_bg_colour, fg=button_fg_colour, font=('Comic Sans', 9, 'bold'),width=button_width)
DOC_Input_button_POS.grid(column=2, row=1)

DOS_Input_button_POS=tk.Button(text='Diffrence Of Squares', command=DOS_Input, bg=button_bg_colour, fg=button_fg_colour, font=('Comic Sans', 9, 'bold'),width=button_width)
DOS_Input_button_POS.grid(column=1, row=1)

Decomposostion_Input_button_POS=tk.Button(text='Decomposistion', command=Decomposistion_Input, bg=button_bg_colour, fg=button_fg_colour, font=('Comic Sans', 9, 'bold'),width=button_width)
Decomposostion_Input_button_POS.grid(column=9, row=0)

Custom_Root_Input_button_POS=tk.Button(text='Custom Root', command=Custom_Root_Input, bg=button_bg_colour, fg=button_fg_colour, font=('Comic Sans', 9, 'bold'),width=button_width)
Custom_Root_Input_button_POS.grid(column=8, row=0)
    
Division_Input_button_POS=tk.Button(text='Division', command=Division_Input, bg=button_bg_colour, fg=button_fg_colour, font=('Comic Sans', 9, 'bold'),width=button_width)
Division_Input_button_POS.grid(column=4, row=0)
    
Multiplication_Input_button_POS=tk.Button(text='Multiplication', command=Multiplication_Input, bg=button_bg_colour, fg=button_fg_colour, font=('Comic Sans', 9, 'bold'),width=button_width)
Multiplication_Input_button_POS.grid(column=3, row=0)
    
Subtraction_Input_button_POS=tk.Button(text='Subtraction', command=Subtraction_Input, bg=button_bg_colour, fg=button_fg_colour, font=('Comic Sans', 9, 'bold'),width=button_width)
Subtraction_Input_button_POS.grid(column=2, row=0)

Addition_Input_button_POS=tk.Button(text='Addition', command=Addition_Input, bg=button_bg_colour, fg=button_fg_colour, font=('Comic Sans', 9, 'bold'),width=button_width)
Addition_Input_button_POS.grid(column=1, row=0)


# Creates Page
root.mainloop()


