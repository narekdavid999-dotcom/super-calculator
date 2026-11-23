import math
from builtins import input, print


def show_menu():
    print("=========== Advanced calculator ===========")
    print(" 1. Addition")
    print(" 2. Subtraction")
    print(" 3. Multiplication")
    print(" 4. Division")
    print(" 5. Floor Division")
    print(" 6. Modules")
    print(" 7. Absolute Value")
    print(" 8. power")
    print(" 9. Square Root")
    print(" 10. sine")
    print(" 11. cosine")
    print(" 12. Exit")
    print("==========================================")

show_menu()

def Addition(a, b):
    return a + b

def Subtraction(a, b):
    return a - b

def Multiplication(a, b):
    return a * b

def Division(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def Floor_Division(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a // b

def Module(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a % b

def Absolute_Value(a):
    return abs(a)

def power(a, b):
    return math.pow(a, b)

def SquareRoot(a):
    if a <= 0:
        return("error")
    return math.sqrt(a)

def Sine(a):
    radian = math.radians(a)
    return math.sin(radian)

def cosine(a):
    radian = math.radians(a)
    return math.cos(radian)

def get_choice():
    while True:
        choice =(input("enter number between 1- 12 "))

        if choice.isdigit():
            choice = int(choice)

            if 1 <= choice <= 12:
                return choice
            print(" you enter wrong value")
def run_calculator():
    while True:
        show_menu()
        choice = get_choice()

        if choice == 1:
            input1 = int(input("Enter first number: "))
            input2 = int(input("Enter second number: "))
            result = Addition(input1, input2)
            print(input1, "+", input2, "=", result)
        elif choice == 2:
            input1 = int(input("Enter first number: "))
            input2 = int(input("Enter second number: "))
            result = Subtraction(input1, input2)
            print(input1, "-", input2, "=", result)
        elif choice == 3:
            input1 = int(input("Enter first number: "))
            input2 = int(input("Enter second number: "))
            result = Multiplication(input1, input2)
            print(input1, "*", input2, "=", result)
        elif choice == 4:
            input1 = int(input("Enter first number: "))
            input2 = int(input("Enter second number: "))
            result = Division(input1, input2)
            print(input1, "/", input2, "=", result)
        elif choice == 5:
            input1 = int(input("Enter first number: "))
            input2 = int(input("Enter second number: "))
            result = Floor_Division(input1, input2)
            print(input1, "//", input2, "=", result)
        elif choice == 6:
            input1 = int(input("Enter first number: "))
            input2 = int(input("Enter second number: "))
            result = Module(input1, input2)
            print(input1, "%", input2, "=", result)
        elif choice == 7:
            input1 = int(input("Enter first number: "))
            result = Absolute_Value(input1)
            print("|", input1, "| =", result)
        elif choice == 8:
            input1 = int(input("Enter first number: "))
            input2 = int(input("Enter second number: "))
            result = power(input1, input2)
            print(input1, "^", input2, "=", result)
        elif choice == 9:
            input1 = int(input("Enter first number: "))
            result = SquareRoot(input1)
            print("sqrt(", input1, ") =", result)
        elif choice == 10:
            input1 = int(input("Enter first number: "))
            result = Sine(input1)
            print("sin(", input1, "°) =", result)
        elif choice == 11:
            input1 = int(input("Enter first number: "))
            result = cosine(input1)
            print("cos(", input1, "°) =", result)
        elif choice == 12:
            print("calculator closed")
            break


import tkinter as tk

# --- Add this at the bottom (replace run_calculator()) ---
window = tk.Tk()
window.title("Advanced Calculator")
window.geometry("360x420")

# Input boxes (replaces input())
tk.Label(window, text="First Number (a):").pack(pady=3)
entry_a = tk.Entry(window, font=("Arial", 12))
entry_a.pack()

tk.Label(window, text="Second Number (b) - if needed:").pack(pady=3)
entry_b = tk.Entry(window, font=("Arial", 12))
entry_b.pack()

# Result display (replaces print())
result_label = tk.Label(window, text="Result: ", font=("Arial", 14, "bold"), fg="blue")
result_label.pack(pady=15)

# Helper to connect your functions to buttons
def calculate(func, two_inputs=True):
    try:
        a = float(entry_a.get())
        if two_inputs:
            b = float(entry_b.get())
            res = func(a, b)
        else:
            res = func(a)
        result_label.config(text=f"Result: {res}")
    except ValueError:
        result_label.config(text="Error: Enter valid numbers")

# Buttons arranged in a neat grid
btn_frame = tk.Frame(window)
btn_frame.pack()

buttons = [
    ("+", lambda: calculate(Addition)),
    ("-", lambda: calculate(Subtraction)),
    ("*", lambda: calculate(Multiplication)),
    ("/", lambda: calculate(Division)),
    ("//", lambda: calculate(Floor_Division)),
    ("%", lambda: calculate(Module)),
    ("|a|", lambda: calculate(Absolute_Value, False)),
    ("a^b", lambda: calculate(power)),
    ("√a", lambda: calculate(SquareRoot, False)),
    ("sin(a°)", lambda: calculate(Sine, False)),
    ("cos(a°)", lambda: calculate(cosine, False)),
]

for i, (text, cmd) in enumerate(buttons):
    tk.Button(btn_frame, text=text, width=8, height=2, command=cmd).grid(row=i//3, column=i%3, padx=4, pady=4)

window.mainloop()
