# Imports
from tkinter import *

# Creating GUI
window = Tk()
window.geometry("500x500")

# Adding Inputs
a = Entry(window, width = 56, borderwidth = 5)
a.place(x=0, y=0)

# Adding buttons
b = Button(window, text="Button 1", padx=20, pady=10)
b.place(x=0, y=40)

c = Button(window, text="Button 2", padx=20, pady=10)
c.place(x=100, y=40)
