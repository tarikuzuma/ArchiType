#Initialize

#Import math so that we can use square root in our operations
#Special thanks to Tharchen Ozzy for the Pythagorean Theorem idea! https://www.codegrepper.com/profile/tharchen-ozzy
import math

def trianglecheck():
    def calculate_triangle():
        try:
            print ("")
            a = float(input("Input side A: "))
            b = float(input("Input side B: "))
            c = float(input("Input side C: "))

            if a <= 0 or b <= 0 or c <= 0:
                print("\n- Invalid input: Negative or Input is Equal to 0 -\n")
                return
            
            if (a+b<=c) or (b+c<=a) or (c+a<=b):
                print("\n- Invalid input: Triangle Inequality Theorem not Observed-\n")
                return
            
            if a == b == c:
                triangle_type = "Equilateral Triangle"

            elif a==b or b==c or a==c:
                triangle_type = "Isosceles Triangle"

            else:
                triangle_type = "Scalene Triangle"
            
            s = (a + b + c) / 2
            area = math.sqrt(s*((s-a)*(s-b)*(s-c)))
            print(f'\nIdentify the triangle_type: {area}')
            print(f'The triangle_type of triangle is: {triangle_type}\n')

        except ValueError:
            print("- Error: Invalid Input -\n")

    while True:
        calculate_triangle()
        while True:
            choice = input("Do you wish to Continue? [Y/N]: ").lower()
            if choice == 'y':
                print("\n - Continue - \n")
                break
            elif choice == 'n':
                print("\n - Good Bye - \n")
                return
            else:
                print("\n - Invalid Input - \n")
                continue

def unitcon():
    print("Enter the distance to convert:")
    distance = float(input())
    print("Enter the starting unit (m, in, cm, ft):")
    start_unit = input()
    print("Enter the unit to convert to (m, in, cm, ft):")
    end_unit = input()

    # Convert distance to meters for calculations
    if start_unit == "in":
        distance_m = distance * 0.0254
    elif start_unit == "cm":
        distance_m = distance / 100
    elif start_unit == "ft":
        distance_m = distance * 0.3048
    else:
        distance_m = distance

    # Convert distance from meters to desired unit
    if end_unit == "in":
        distance_conv = distance_m / 0.0254
    elif end_unit == "cm":
        distance_conv = distance_m * 100
    elif end_unit == "ft":
        distance_conv = distance_m / 0.3048
    else:
        distance_conv = distance_m

    print("\nConverted distance:", distance_conv, end_unit, "\n")


def temperature():

    #Line of code ensures that user only inputs digits.
    valid = False

    #While input remains non-intiger, valid == false. When it's finally true, the loop stops.
    while not valid:
        try:
            x = float(input("Enter a number: "))
            valid = True
        except ValueError:
            print("Only input digits")

    while True:
        print ("Type C if this number is in Celcius, and type F if this number is in Fahrenheit (Case sensitive)")
        q1 = input("Input Unit: ")

        if q1 == "C":
            #(0°C × 9/5) + 32 = 32°F
            c = 0
            c = (x * (9/5)) + 32
            print ("")
            print (f"Converted {x}°C to Fahrenheit is {c}°F \n")
            break
        elif q1 == "F":
            #(0°F − 32) × 5/9
            f = 0
            f = (x - 32) * (5/9)
            print ("")
            print (f"Converted {x}°F to Fahrenheit is {f}°C \n")
            break
        else:
            print ("Choice input isn't given.\n")
            

def conversion():
    #Conversion of unit to another unit.
    print ("")
    print ("This program converts:")
    print ("1. Meters, Inches, Centimeters, Feet")
    print ("2. Fahrenheit to Celsius\n")

    while True:
        unit = input("Choose a unit you want to convert (1 or 2): ")

        if unit == "1":
            unitcon()
            break
        elif unit == "2":
            temperature()
            break
        else:
            print ("Choice Incomprehensible")

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

    
    


########## Code starts here #########
while True:
    print ("Welcome! Input a program you'd like to use")

    print ("1. Unit Conversion")
    print ("2. Finding for Pythagorean Theorem (Base, Leg, and Hypotenuse)")
    print ("3. Triangle Assessment")
    print ("4. End the program")


    choice = input('Input choice: ')

    if choice == '1':
        conversion()
        
    elif choice == '2':
        pytha()

    elif choice == '3':
        trianglecheck()

    elif choice == '4':
        print ("-Program End-")
        break
        #Finishes Program
    
    else:
        print ("Choice Incomprehensible")