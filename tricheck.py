import tkinter as gui
import math
def open_tricheck(aParent):
    root = gui.Toplevel(aParent)
    
    def clear():
        entries = [entry_a, entry_b, entry_c]
        for entry in entries:
            entry.delete(0, "end")

    def calculate(a ,b, c):
        try:
            a = float(a)
            b = float(b)
            c = float(c)

            s = (a + b + c) / 2
            area = math.sqrt(s*((s-a)*(s-b)*(s-c)))

            if a == b == c:
                output_area.delete(0, "end")
                output_area.insert(0, area)

                output_type.delete(0, "end")
                output_type.insert(0, "Equilateral Triangle")

            elif a==b or b==c or a==c:
                output_area.delete(0, "end")
                output_area.insert(0, area)

                output_type.delete(0, "end")
                output_type.insert(0, "Isoceles Triangle")

            else:
                output_area.delete(0, "end")
                output_area.insert(0, area)

                output_type.delete(0, "end")
                output_type.insert(0, "Scalene Triangle")

            if a <= 0 or b <= 0 or c <= 0 or (a+b<=c) or (b+c<=a) or (c+a<=b):
                output_area.delete(0, "end")
                output_area.insert(0, "Negative or Triangle Inequality")

                output_type.delete(0, "end")
                output_type.insert(0, "Negative or Triangle Inequality")

        except ValueError:
            clear()
            entry_a.insert(0, "Invalid Input")
            entry_b.insert(0, "Invalid Input")
            entry_c.insert(0, "Invalid Input")



    root.title("Triangle Checker")

    text_a = gui.Label(root, text="Input Side A = ", font=('Helvetica', 15))
    text_a.grid(row=1, column=0, padx=5, pady=5)

    entry_a = gui.Entry(root, width=30)
    entry_a.grid(row=1, column=1, padx=5, pady=5)

    text_b = gui.Label(root, text="Input Side B = ", font=('Helvetica', 15))
    text_b.grid(row=2, column=0, padx=5, pady=5)

    entry_b = gui.Entry(root, width=30)
    entry_b.grid(row=2, column=1, padx=5, pady=5)

    text_c = gui.Label(root, text="Input Side C = ", font=('Helvetica', 15))
    text_c.grid(row=3, column=0, padx=5, pady=5)

    entry_c = gui.Entry(root, width=30)
    entry_c.grid(row=3, column=1, padx=5, pady=5)

    btn_clr = gui.Button(root, text = "Clear", width=5, height=2, command=lambda: clear())
    btn_clr.grid(row=4, column=0, padx=5, pady=5)

    btn_cal = gui.Button(root, text = "Calculate", width=7, height=2, command=lambda: calculate(entry_a.get(), entry_b.get(), entry_c.get()))
    btn_cal.grid(row=4, column=1, padx=5, pady=5)


    area_text = gui.Label(root, text="Area of Triangle:", font=('Helvetica', 15))
    area_text.grid(row=5, column=0, padx=5, pady=5)

    output_area = gui.Entry(root, width=30)
    output_area.grid(row=5, column=1, padx=5, pady=5)

    type_text = gui.Label(root, text="Type of Triangle:", font=('Helvetica', 15))
    type_text.grid(row=6, column=0, padx=5, pady=5)

    output_type = gui.Entry(root, width=30)
    output_type.grid(row=6, column=1, padx=5, pady=5)

    root.mainloop()