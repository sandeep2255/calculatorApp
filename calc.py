import math

# Function to add two numbers
def sum(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Function to calculate percentage of a number
def percentage(x, y):
    return (x * y) / 100

# Function to calculate exponentiation
def exponentiation(x, y):
    return x ** y

# Function to calculate square root
def square_root(x):
    if x < 0:
        return "Error! Square root of a negative number is not defined."
    else:
        return math.sqrt(x)

# Function to calculate factorial
def factorial(x):
    if x < 0:
        return "Error! Factorial of a negative number is not defined."
    elif x == 0:
        return 1
    else:
        return x * factorial(x - 1)

# Main function to run the calculator
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Percentage")
    print("6. Exponentiation")
    print("7. Square Root")
    print("8. Factorial")

    choice = input("Enter choice (1/2/3/4/5/6/7/8): ")

    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    elif choice in ['6', '7', '8']:
        num = float(input("Enter number: "))

    if choice == '1':gitgit
        print(f"{num1} + {num2} = {sum(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    elif choice == '5':
        print(f"{num2}% of {num1} = {percentage(num1, num2)}")
    elif choice == '6':
        print(f"{num1} ^ {num2} = {exponentiation(num1, num2)}")
    elif choice == '7':
        print(f"Square root of {num} = {square_root(num)}")
    elif choice == '8':
        print(f"Factorial of {num} = {factorial(num)}")
    else:
        print("Invalid input")

# Run the calculator
calculator()
