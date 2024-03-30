equation = input("What is the equation? ")

equation = equation.strip().split()

x = float(equation[0])
y = equation[1]
z = float(equation[2])

if y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "*":
    print(x * z)
elif y == "/":
    print(x / z)