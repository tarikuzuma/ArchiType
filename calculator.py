import tkinter as gui
import math 

def open_calc(aParent): #function to create new window
    root = gui.Toplevel(aParent)

    def add_to_calculation(symbol): #Done so calculator can see do what it's supposed to do. Returns the argument "symbol"
        nonlocal calculation #so that we can maniupualte variable in function 
        if symbol in ["sin", "cos", "tan", "sqrt"]:
            calculation += f"math.{symbol}("
        elif symbol == "pi":
            calculation += "math.pi"
        elif symbol == "!":
            calculation += "math.factorial("
        else:
            calculation += str(symbol)
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)

    def eval_calculation(): #python func that evaulates python statements
        nonlocal calculation
        try:
            result = str(eval(calculation))
            text_result.delete(1.0, "end")
            text_result.insert(1.0, result)
        except:
            clear_field()
            text_result.insert(1.0, "Syntax Error")

    def clear_field(): #function that clears the calculation field in the calculator
        nonlocal calculation
        calculation = ""
        text_result.delete(1.0, "end") #deletes the content of widget

    root.title("Calculator")
    root.geometry("600x300")

    calculation = ""
    text_result = gui.Text(root, height=2, width=16, font=("Helvetica", 24))
    text_result.grid(columnspan=5)

    # list contains tuples that specify the text to be displayed on each button, as well as its row and column position in the window.
    button_data = [
        ("1", 2, 1), ("2", 2, 2), ("3", 2, 3),
        ("4", 3, 1), ("5", 3, 2), ("6", 3, 3),
        ("7", 4, 1), ("8", 4, 2), ("9", 4, 3),
        ("0", 5, 2),
        ("+", 2, 4), ("-", 3, 4), ("*", 4, 4), ("/", 5, 4),
        ("(", 5, 1), (")", 5, 3),
        ("sin", 2, 5), ("cos", 2, 6), ("tan", 2, 7),
        ("sqrt", 3, 5), ("pi", 3, 6), ("!", 3, 7)
    ]

    for data in button_data: #for loop that creates button widget honestly dont know how to explain this, i just found it off the internet
        text, row, col = data
        button = gui.Button(root, text=text, width="5", font=("Helvetica", 14))
        button.grid(row=row, column=col)
        button["command"] = lambda x=text: add_to_calculation(x)

    btn_clear = gui.Button(root, text="C", command=clear_field, width="5", font=("Helvetica", 14)) #pass the function as an entity
    btn_clear.grid(row=6, column= 1)

    btn_equals = gui.Button(root, text="=", command=eval_calculation, width="11", font=("Helvetica", 14))
    btn_equals.grid(row=6, column= 3, columnspan=2)

    root.mainloop()