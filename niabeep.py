from tkinter.ttk import *
from tkinter import *
import tkinter as tk

# Creating the box
window = Tk()
window.title('Authentication')
window.geometry('400x400')
window.resizable(False, False) # LOL
window['background']='#1091E4'

def closeBox():
    window.destroy()

def login():
    pass

# White frame
window.frame=Frame(window)
window.frame.place(relx=0.5, rely=0.5, width=250, height=270, anchor="center")


# User-name exntry box here
user = tk.Entry(window, width=20)
user.insert(0,"Username: ")
user.place(relx=0.5, rely=0.3, anchor="center")

#Password entry box
password = tk.Entry(window, width=20)
password.insert(0,"Password: ")
password.place(relx=0.5, rely=0.4, anchor="center")

# Buttonss to Login and close window
btn = Button(window, text='Login', command=login)
# btn.grid(row=4, column=2)
btn.place(relx=0.5, rely=0.5, anchor="center")

#Closing window box
btn1 = Button(window, text='Quit', command=closeBox)
btn1.place(relx=0.5, rely=0.6, anchor="center")


window.mainloop()



