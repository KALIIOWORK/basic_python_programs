#!/bin/python3
import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y
def divide(x, y):
    if y==0:
        return("Denominator cannot be zero, please enter a valid number")
    else:
        return x / y
    
def root(x):
    if x<=0:
        return("Number must be greater than zero, please enter a valid number")
    else:
        return math.sqrt(x)


print("Welcome to my calculator. Please choose your desired operation below:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Square root")

def calculate():
    while True:
        option = input("Enter option(1/2/3/4/5): ")
        
        if option in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if option == '1':
                print(num1, "+", num2, "=", add(num1, num2))

            elif option == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif option == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif option == '4':
                print(num1, "/", num2, "=", divide(num1, num2))
            
            next_calculation = input("Would you like to do another calculation? (yes/no): ")
            if next_calculation != "yes":
                break
            
        elif option == '5':
            try:
                num1=float(input("Enter a number: "))
            except ValueError:
                print("Invalid Input. Please enter a number or a value greater than zero")
            print("Square root of ", num1, "=", root(num1) )
           
            next_calculation = input("Would you like to do another calculation? (yes/no): ")
            if next_calculation != "yes":
                break
        else:
            print("Invalid Input. Please enter a number or a value greater than zero")

if __name__ == "__main__":
    calculate()