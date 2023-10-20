# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Division by zero is not allowed."
    else:
        return x / y

# Welcome message
print("Welcome to the Simple Calculator!")

# Input for the first number
try:
    num1 = float(input("Please enter the first number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

# Input for the second number
try:
    num2 = float(input("Please enter the second number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

# Input for the operation
operation = input("Select operation (+, -, *, /): ")

# Perform the calculation based on the selected operation
if operation == '+':
    result = add(num1, num2)
    print(f"Result: {num1} + {num2} = {result}")
elif operation == '-':
    result = subtract(num1, num2)
    print(f"Result: {num1} - {num2} = {result}")
elif operation == '*':
    result = multiply(num1, num2)
    print(f"Result: {num1} * {num2} = {result}")
elif operation == '/':
    result = divide(num1, num2)
    print(f"Result: {num1} / {num2} = {result}")
else:
    print("Invalid operation. Please select +, -, *, or /.")
