import tkinter as gui
from GUI import *

root = gui.Tk() #returns title of the screen #Parent
root.title("Architype") #sets title of the screen

root.geometry("300x300") #root.geometry() is a method in the tkinter library for Python that allows you to set the size and position of the main window in your GUI

text = gui.Label(root, text="Architype Main Menu!" , font = ('Helvetica', 18))
text.pack(padx=20, pady=20)

button1 = gui.Button(root, text="Calculator", font = ('Helvetica', 13), height= 2, width=50, fg='white', bg='gray', command=lambda: openWindowNumbar1(root))
button1.pack(padx=20, pady= 7)

button2 = gui.Button(root, text="Loram Ipsum", font = ('Helvetica', 13), height= 2, width=50, fg='white', bg='gray')
button2.pack(padx=20, pady= 7)

button3 = gui.Button(root, text="Loram Ipsum", font = ('Helvetica', 13), height= 2, width=50, fg='white', bg='gray')
button3.pack(padx=20, pady= 7)

root.mainloop() #calls the mainloop of tkinter
