import tkinter as gui
import math

computation = ""

#cels = (fahr - 32.0) * 5.0/9.0;
#Fahr = (x * (9/5)) + 32

def temp_convert(symbol):
    global computation
    computation = text_result.get("1.0", "end-1c")
    if symbol == "C":
        f = float(computation)
        c = (f - 32) * (5/9)
        c = round(c, 2)
        computation = str(c)
        text_result.delete(1.0, "end")
        text_result.insert(1.0, c)
    
    elif symbol == "F":
        c = float(computation)
        f = (c * (9/5)) + 32
        f = round(f, 2)
        computation = str(c)
        text_result.delete(1.0, "end")
        text_result.insert(1.0, f)

def clear_field():
    global computation
    computation = ""
    text_result.delete(1.0, "end")

root=gui.Tk()
root.title("Converter")
root.geometry("300x300") #root.geometry() is a method in the tkinter library for Python that allows you to set the size and position of the main window in your GUI

text_result = gui.Text(root, height=2, width=16, font=("Helvetica", 24))
text_result.grid(columnspan=5)

btn_far = gui.Button(root, text= "to F°", command = lambda: temp_convert("F"), width="5", height="2", font=("Helvetica", 14))
btn_far.grid(row=3, column=0, pady=20)

btn_cel = gui.Button(root, text= " to C°", command = lambda: temp_convert("C"), width="5", height="2", font=("Helvetica", 14))
btn_cel.grid(row=4, column=0, pady=5)

btn_clear = gui.Button(root, text="C", command=clear_field, width="5", font=("Helvetica", 14)) #pass the function as an entity
btn_clear.grid(row=5, column= 0, columnspan=4)

'''
btn_equals = gui.Button(root, text="=", command=eval_calculation, width="11", font=("Helvetica", 14))
btn_equals.grid(row=6, column= 3, columnspan=2)
'''

root.mainloop() #calls the mainloop of tkinter