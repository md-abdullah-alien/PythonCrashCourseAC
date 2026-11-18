# Mini Project: Calculator
print("Welcome to Mini Calculator")
a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
op = input("Enter an operator(+, -, *, /, %, **): ")
# For Additional Operation
if op == '+':
    print("Numbers Addition: ", a + b)
# For Subtraction Operation
elif op == '-':
    print("Numbers Subtraction: ", a - b)
# For Multiplication Operation
elif op == '*':
    print("Numbers Multiplication: ", a * b)
# For Division Operation
elif op == '/':
    print("Numbers Division: ", a / b)
# For Modulus Operation
elif op == '%':
    print("Numbers Modulus: ", a % b)
# For Power Operation
elif op == '**':
    print("Power of Number: ", a ** b)
else:
    print("Invalid Input")