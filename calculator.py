while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")

    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input in ("add", "subtract", "multiply", "divide"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_input == "add":
            print("Result:", num1 + num2)
        elif user_input == "subtract":
            print("Result:", num1 - num2)
        elif user_input == "multiply":
            print("Result:", num1 * num2)
        elif user_input == "divide":
            if num2 == 0:
                print("Cannot divide by zero")
            else:
                print("Result:", num1 / num2)
    else:
        print("Invalid input. Please try again.")
