#Initialize

#Import math so that we can use square root in our operations
#Special thanks to Tharchen Ozzy for the Pythagorean Theorem idea! https://www.codegrepper.com/profile/tharchen-ozzy
import math

def unitcon():
    print()
    print ("Continuation -Next Time-\n")

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
    print ("1. Meters, Kilometers, Miles, Feet")
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

    print("\n")
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
            print("\n")
            print("Finding Base of Triangle\n")
            b = float(input("Height: ")) #Codes inside of parentheses becuz why not easy and fast code (gumagana pa utak ko neto)
            c = float(input("Hypotenuse: "))
            a = math.sqrt(c ** 2 - b ** 2) #math.sqrt uses library math to squareroot the ff equation
            triangleexe()
            print("Base of the triangle is", "%.2f" %a)
            print("\n")
            return 0

        #Height Formula
        elif side == "b":
            print("Finding Height of Triangle\n")
            a = float(input("Base: "))
            c = float(input("Hypotenuse: "))
            b = math.sqrt(c ** 2 - a ** 2)
            triangleexe()
            print("Height of the triangle is","%.2f" %b)
            print("\n")
            return 0

        #Hypotenuse Formula
        elif side == "c":
            print("Finding Hypotenuse of Triangle\n")
            a = float(input("Base: "))
            b = float(input("Height: "))
            c = math.sqrt(a ** 2 + b ** 2)
            triangleexe()
            print("Hypotenuse of the triangle is","%.2f" %c)
            print("\n")
            return 0

        else:
            print("Value is Invalid.")
            break

    
    


########## Code starts here #########
while True:
    print ("Welcome! Input a program you'd like to use")

    print ("1. Unit Conversion")
    print ("2. Finding for Pythagorean Theorem (Base, Leg, and Hypotenuse)")
    print ("3. End the program")


    choice = input('Input choice: ')

    if choice == '1':
        conversion()
        
    elif choice == '2':
        pytha()

    elif choice == '3':
        print ("-Program End-")
        break
        #Finishes Program
        
    else:
        print ("Choice Incomprehensible")
        

#Add unit for finding unit for volume etc.
#Fix Theorem

#Yung program na 'toh ay may halong GALIT sa paggawa kasi si Wiwiw ay mag o-one-on-one kasama si Yuyu! ! ! 
#Taena angas ah, sino di magaglait kung yung babaeng mahal mo makikipag gala kasama yung lalaking pinagseselosan mo 
#NAGCOCODE ka nang may taninm na sama nang loob? Tas nalaman mo na lang na nilibre niya yung GF mo 24/7 NANG sila lang.
#Kabet ! 
#eddie likes etits 
