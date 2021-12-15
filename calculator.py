# Simple calculator version 1

what = input("What are you want(+, -, *, /): ")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if what == "+":
    c = a + b
    print('Result: ' + str(c))
elif what == "-":
    c = a - b
    print('Result: ' + str(c))
elif what == "*":
    c = a * b
    print('Result: ' + str(c))
elif what == "/":
    c = a / b
    print('Result: ' + str(c))
else:
    print('Something went wrong!')
