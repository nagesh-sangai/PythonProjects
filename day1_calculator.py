a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))

op = input("Choose an operator (+, -, *, /):")

if op == "+":
    print("Result:",a + b)
elif op == "-":
    print("Result:",a - b)
elif op == "*":
    print("Result:",a * b)
elif op == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("cannot divide by zero!")
else:
    print("Invalid operator!")