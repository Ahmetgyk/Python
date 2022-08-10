import tkinter as tk
from tkinter import *

def degistir():
    fred.config(bg="YELLOW")

pencere = tk.Tk()
pencere.geometry("600x500")

fred = Frame(bg="RED", width=300, height=150)
fred.place(x=10,y=35)

but = Button(text="Sarı Farme", command=degistir)
but.pack()
but.place(x=10,y=10)

pencere.mainloop()

bbox