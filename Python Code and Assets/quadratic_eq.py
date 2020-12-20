# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 02:50:02 2020

@author: Mohammad Monjur-E-Elahi
"""

# Tkinter is the original free graphics library for the Python language, allowing the creation of graphical interfaces.
# It comes from an adaptation of the Tk graphics library written for Tcl.

import tkinter as tk                     # import tkinter and alias that to tk. This is known as an "alias import"
from tkinter import ttk                  # ttk are new set of widgets that makes button, label that are themeable
from tkinter import Canvas               # The Canvas is a rectangular area intended for drawing pictures or other 
                                         # complex layouts. You can place graphics, text, widgets or frames on a Canvas.

from tkinter import PhotoImage           # Image can be added with the help of PhotoImage() method.

 
root = tk.Tk()                           # Main window tk.Tk() is a tk object
root.title("Project App: Quadratic Equation Solver")  # Title of the whole GUI Window

root.config(padx=30, pady=30)            # Padding in horizontal and vertical axis respectively

a = tk.StringVar()
b = tk.StringVar()
c = tk.StringVar()

x1_value = tk.StringVar()  #(value="x1 appears here")
x2_value = tk.StringVar()  #( value="x2 appears here")

# The below function calculates the roots of a quadratic equation when the funcion is called with necessary arguments

def quadratic_equation(*args):
    try:
        a1 = float(a.get())
        b1 = float(b.get())
        c1 = float(c.get())
        x1 = (-b1+(b1**2 - 4*a1*c1)**0.5)/(2*a1)
        x2 = (-b1-(b1**2 - 4*a1*c1)**0.5)/(2*a1)
        x1_value.set(f"{x1:.3f}")
        x2_value.set(f"{x2:.3f}")
    except ValueError:
        pass

canvas = Canvas(height=500, width=900)
logo_img = PhotoImage(file="./assets/quad.png")
canvas.create_image(450,200, image=logo_img)
canvas.pack()                                   # .pack() puts the element in to the window

a_label = ttk.Label(root, text='Insert "a"')    # Will create a new Label object inside the ttk package
a_label.pack()                                  # Labels, buttons etc is put inside the root window

a_entry = ttk.Entry(root, textvariable=a)       # a will reference to a = tk.StringVar()
a_entry.pack()

b_label = ttk.Label(root,text='Insert "b"')
b_label.pack()

b_entry = ttk.Entry(root, textvariable=b)       # b will reference to b = tk.StringVar()
b_entry.pack()

c_label = ttk.Label(root, text='Insert "c"')
c_label.pack()

c_entry = ttk.Entry(root, textvariable=c)       # c will reference to c = tk.StringVar()
c_entry.pack()

calculate_x_button = ttk.Button(root, text = "Calculate Roots", command=quadratic_equation)  # This button will make the
                                                                                             # function call
calculate_x_button.pack(pady=25)

x1_label = ttk.Label(root, text = "X1 :")
x1_label.pack(side="left")

x1_label1 = ttk.Label(root, pad=20, textvariable=x1_value)       # x1_value will reference to x1_value = tk.StringVar()
x1_label1.pack(side="left")

x2_label = ttk.Label(root, text = "X2 :")                  
x2_label.pack(side="left")

x2_label1 = ttk.Label(root, pad=20, textvariable=x2_value)       # x2_value will reference to x2_value = tk.StringVar()   
x2_label1.pack(side="left")

quit_button = ttk.Button(root, text = "Quit", command=root.destroy) # root.destroy destroys the window
quit_button.pack(side = "right") 

root.mainloop()       # Starts tkinter running. Python code is paused at this line. tkinter takes over meanbs tkinter will be 
                      # constantly running and we can make tkinter do stuff in the background when click a button etc
                      # any python code after this will not run unless we close the window                              