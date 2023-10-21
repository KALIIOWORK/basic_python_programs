def sierpinski(level):
    if level == 0:
        return ["*"]

    lower_triangle = sierpinski(level - 1)
    spaces = [" " * (2 ** level - 1) for _ in range(2 ** (level - 1))]

    result = []
    for i in range(2 ** level):
        if i < 2 ** (level - 1):
            result.append(lower_triangle[i] + " " + lower_triangle[i])
        else:
            result.append(lower_triangle[i - 2 ** (level - 1)] + spaces[i - 2 ** (level - 1)] + lower_triangle[i - 2 ** (level - 1)])

    return result

def print_sierpinski(level):
    sierpinski_pattern = sierpinski(level)
    for row in sierpinski_pattern:
        print(row)

# Set the desired level of the Sierpinski Triangle (adjust as needed)
level = 4

print_sierpinski(level)
