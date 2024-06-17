# Function to add two numbers
def add(x, y):
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
        return "Error: Division by zero!"
    return x / y


# Function to display the menu and get user's choice
def get_user_choice():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    return input("Enter choice (1/2/3/4/5): ")


# Calculator main function
def calculator():
    while True:
        choice = get_user_choice()

        if choice == '5':
            print("Calculator has been exited.")
            break

        if choice not in ('1', '2', '3', '4'):
            print("Invalid input. Please enter a valid option (1/2/3/4/5).")
            continue

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            result = divide(num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print(f"{num1} / {num2} = {result}")


# Run the calculator
calculator()
