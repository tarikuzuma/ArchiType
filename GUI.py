import tkinter as gui #tkinter is refered as gui for simplicity

def openWindowNumbar1(aParent):
    window2 = gui.Toplevel(aParent) #retruns title of the screen

    window2.geometry("800x600") #window2.geometry() is a method in the tkinter library for Python that allows you to set the size and position of the main window in your GUI
    window2.title("Architype!") #Sets title

    label = gui.Label(window2, text="Hello World", font = ('Arial', 18))
    label.pack(padx=20, pady=20)

    textbox = gui.Text(window2, height=3, font=('Arial', 15)) #used for scrollable entries
    textbox.pack(padx=20) 

    button = gui.Button(window2, text="Enter", font=('Arial', 15)) #Creates  a button
    button.pack(padx=10, pady=10)

    buttonframe = gui.Frame(window2)
    buttonframe.columnconfigure([0,1,2], weight=1)

    for i in range(1, 10):
        btn = gui.Button(buttonframe, text=str(i), font=('Arial', 15))
        btn.grid(row=(i-1)//3, column=(i-1)%3, sticky=gui.W+gui.E)

    buttonframe.pack(fill="x")

    # window2.mainloop()
