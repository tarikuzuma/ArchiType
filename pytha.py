import math

def pytha():

    #Def triangle defined to draw top of triangle
    def triangle():
        print("               .")
        print("              /|")
        print("             / |")
        print("            /  |")
        print("           /   |")
        print("          /    |")
        print("         /     |")
        print("        /      |")

    #Draw Middle of triangle with hypotenuse and height of triangle
    def  traingle_1():
        print("     ","%.2f" %c, " ","%.2f" %b)

    #Draw Bottom of triangle with base at the bottom
    def triangle_2():
        print("      /        |")
        print("     /         |")
        print("    /          |")
        print("   /           |")
        print("  /            |")
        print(" /             |")
        print("/___","%.2f"%a,"_____|\n")

        print ("Equation Found, with given diagram too.")
        print ("\n")


    #Def shortcut to prevent longing code
    def triangleexe():
        triangle()
        traingle_1()
        triangle_2()

    print("\n \n \n \n")
    print("               /|")
    print("              / |")
    print("             /  |")
    print("            /   |")
    print("           /    |")
    print("          /     |")
    print("         /      |")
    print("     c  /       |")
    print("       /        | a ")
    print("      /         |")
    print("     /          |")
    print("    /           |")
    print("   /            |")
    print("  /             |")
    print(" /______________|")
    print("          b      \n")

    print("\n") 
    print("Please note the following indications\n")
    print("a is the base of the triangle\n")
    print("b is the height of the triangle\n")
    print("c is the hypotenus of the triangle\n")

    #Pythagoream Theorem Formula: \sqrt{c=a2+b2}

    while True:

        #Declare varuable "side" as something that can be parced to data types.
        side = input("Give the side you want to solve for (a, b, or c): ")

        #If statement to see if choice for side is a, b, c, or N/A.
        #If N/A, break the loop and start from beginning.

        #Base Formula
        if side == "a":
            try:
                print("\n")
                print("Finding Base of Triangle")
                b = float(input("Height: ")) #Codes inside of parentheses becuz why not easy and fast code (gumagana pa utak ko neto)
                c = float(input("Hypotenuse: "))

                if b == c or b == 0 or c == 0:
                    print("\nError: Triangle does not form\n")
                    break   

                try:
                    a = math.sqrt(c ** 2 - b ** 2) #math.sqrt uses library math to squareroot the ff equation
                except:
                    print("\nError: Square root failed. Make sure c > b \n")
                    break
                
                triangleexe()
                print("Base of the triangle is", "%.2f" %a)
                print("\n")
                return 0
            except ValueError:
                print("\nError: Unexpected Input\n")
                break

        #Height Formula
        elif side == "b":
            try:
                print("\nFinding Height of Triangle")
                a = float(input("Base: "))
                c = float(input("Hypotenuse: "))

                if a == c or a == 0 or c == 0:
                    print("\nError: Triangle does not form\n")
                    break

                try:
                    b = math.sqrt(c ** 2 - a ** 2)
                except:
                    print("\nError: Square root failed. Make sure c > a \n")
                    break

                triangleexe()
                print("Height of the triangle is","%.2f" %b)
                print("\n")
                return 0
            except ValueError:
                print("\nError: Unexpected Input.\n")
                break

        #Hypotenuse Formula
        elif side == "c":
            try:
                print("\nFinding Hypotenuse of Triangle")
                a = float(input("Base: "))
                b = float(input("Height: "))

                if b == a:
                    print("Shape forms an Isosceles Right triangle")

                elif b == 0 or a == 0:
                    print("\nError: Triangle does not form\n")
                    break
                c = math.sqrt(a ** 2 + b ** 2)
                triangleexe()
                print("Hypotenuse of the triangle is","%.2f" %c)
                print("\n")
                return 0
            except ValueError:
                print("\nError: Unexpected Input\n")
                break

        else:
            print("Error: Value is Invalid.")
            break

while True:
    print("Start:")
    pytha()

    while True:
        Choice = str(input("\nRetry? [Y/N]: "))
        if Choice.lower() == 'y':
            print("Repeat Process\n")
            break
        elif Choice.lower() == 'n':
            enter = input("Thanks for using me! Press [ENTER] to Leave")
            quit()
        else:
            print ("\nError: Invalid Input")