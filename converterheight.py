import tkinter as gui

def unitcon():
    try:
        value = float(entry.get())
        #Used chat GPT to code for logic in temperature converting
        #Also used previous assessment to analyze code
        #Convert input values to meters to initialzie definition
        if input_unit.get() == "cm":
            value_m = value / 100
        elif input_unit.get() == "in":
            value_m = value * 0.0254
        elif input_unit.get() == "ft":
            value_m = value * 0.3048
        else:
            value_m = value

        #Convert meters to output units
        if output_unit.get() == "cm":
            value_out = value_m * 100
            unit_out = "cm"
        elif output_unit.get() == "in":
            value_out = value_m / 0.0254
            unit_out = "in"
        elif output_unit.get() == "ft":
            value_out = value_m / 0.3048
            unit_out = "ft"
        else:
            value_out = value_m
            unit_out = "m"

        #Update output:
        output_label.config(text=f"{value} {input_unit.get()} = {value_out:.2f} {unit_out}")
    
    except ValueError:
        output_label.config(text="Invalid input")


def clear_field():
    entry.delete(0, "end")

root = gui.Tk()

#makes Entry Field for user type
entry = gui.Entry(root, width=10)
entry.grid(row=0, column=0,padx=0,pady=5)

#List for dropdown menu
unit_list = ["cm","m","in","ft"]

#Input Unit
input_unit = gui.StringVar()
input_unit.set("cm")
input_menu = gui.OptionMenu(root, input_unit, *unit_list)
input_menu.grid(row=0, column=1,padx=5,pady=5)

#Output Unit
output_unit = gui.StringVar()
output_unit.set("cm")
output_menu = gui.OptionMenu(root, output_unit, *unit_list)
output_menu.grid(row=1, column=1,padx=5,pady=5)

#Convert Button
btn_con = gui.Button(root, text = "Convert", font=('Helvetica', 10), command=unitcon)
btn_con.grid(row=0, column=2, padx=5, pady=5)

#Clear Button
btn_clr = gui.Button(root, width = 5, text = "C", font=('Helvetica', 10), command=clear_field)
btn_clr.grid(row=1, column=2, padx=5, pady=5)

#Create output of label
output_label = gui.Label(root, text="Output: ")
output_label.grid(row=1, column=0, padx=5, pady=5)

root.mainloop() #calls the mainloop of tkinter