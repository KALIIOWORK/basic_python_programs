def convert_temperature(value, input_scale, output_scale):
    if input_scale == 1:
        if output_scale == 1:
            return value * 1.8 + 32
        elif output_scale == 2:
            return value + 273.15
        else:
            return value
    elif input_scale == 2:
        if output_scale == 1:
            return (value - 32) / 1.8
        elif output_scale == 2:
            return (value + 459.67) * 5 / 9
        else:
            return value
    elif input_scale == 3:
        if output_scale == 1:
            return value - 273.15
        elif output_scale == 2:
            return value * 9 / 5 - 459.67
        else:
            return value
    else:
        return value


print("Welcome to the Temperature Converter!")

print("\nSelect input unit:\n1. Celsius\n2. Fahrenheit\n3. Kelvin \n")

input_unit = int(input("Enter choice: "))

if input_unit == 1:
    temp = float(input("Enter temperature in Celsius: "))
    print("\nSelect target unit:\n1. Fahrenheit\n2. Kelvin\n")
    target = int(input("Enter choice: "))
    if target == 1:
        degree = "F"
    else:
        degree = "K"

if input_unit == 2:
    temp = float(input("Enter temperature in Fahrenheit: "))
    print("\nSelect target unit:\n1. Celsius\n2. Kelvin\n")
    target = int(input("Enter choice: "))
    if target == 1:
        degree = "C"
    else:
        degree = "K"

if input_unit == 3:
    temp = float(input("Enter temperature in Kelvin: "))
    print("\nSelect target unit:\n1. Celsius\n2. Fahrenheit\n")
    target = int(input("Enter choice: "))
    if target == 1:
        degree = "C"
    else:
        degree = "F"

result = convert_temperature(temp, input_unit, target)

print(f"Converted temperature: {result} {degree}")