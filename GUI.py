import tkinter as gui
import math 

def openWindowNumbar1(aParent):
    root = gui.Toplevel(aParent)

    def add_to_calculation(symbol):
        nonlocal calculation
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

    def eval_calculation():
        nonlocal calculation
        try:
            result = str(eval(calculation))
            text_result.delete(1.0, "end")
            text_result.insert(1.0, result)
        except:
            clear_field()
            text_result.insert(1.0, "Syntax Error")

    def clear_field():
        nonlocal calculation
        calculation = ""
        text_result.delete(1.0, "end")

    root.title("Calculator")
    root.geometry("600x300")

    calculation = ""
    text_result = gui.Text(root, height=2, width=16, font=("Helvetica", 24))
    text_result.grid(columnspan=5)

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

    for data in button_data:
        text, row, col = data
        button = gui.Button(root, text=text, width="5", font=("Helvetica", 14))
        button.grid(row=row, column=col)
        button["command"] = lambda x=text: add_to_calculation(x)

    btn_clear = gui.Button(root, text="C", command=clear_field, width="5", font=("Helvetica", 14)) #pass the function as an entity
    btn_clear.grid(row=6, column= 1)

    btn_equals = gui.Button(root, text="=", command=eval_calculation, width="11", font=("Helvetica", 14))
    btn_equals.grid(row=6, column= 3, columnspan=2)

    root.mainloop()
