import tkinter as gui

def open_tempcon(aParent):
    root = gui.Toplevel(aParent)

    #cels = (fahr - 32.0) * 5.0/9.0;
    #Fahr = (x * (9/5)) + 32

    def temp_convert(symbol):
        try:
            computation = text_result.get("1.0", "end-1c")
            result = round(eval(computation), 2)
            text_result.delete("1.0", "end")
            text_result.insert("1.0", result)
            
            if symbol == "C":
                c = (result - 32) * (5 / 9)
            elif symbol == "F":
                c = (result * (9 / 5)) + 32
            
            text_result.delete("1.0", "end")
            text_result.insert("1.0", round(c, 2))
            
        except:
            clear_field()
            text_result.insert("1.0", "Syntax Error")

    def clear_field():
        text_result.delete("1.0", "end")
    
    root.title("Converter")
    root.geometry("300x200")

    text_result = gui.Text(root, height=2, width=16, font=("Helvetica", 24))
    text_result.grid(row=0, column=0, columnspan=3, pady=20)

    #made code shorter by parsing gui into a button, then griding it with.grid
    gui.Button(root, text="to F°", command=lambda: temp_convert("F"), width=5, height=2, font=("Helvetica", 14)).grid(row=1, column=0, padx=5)
    gui.Button(root, text="C", command=clear_field, width=5, font=("Helvetica", 14)).grid(row=1, column=1, padx=5)
    gui.Button(root, text="to C°", command=lambda: temp_convert("C"), width=5, height=2, font=("Helvetica", 14)).grid(row=1, column=2, padx=5)

    root.mainloop()
