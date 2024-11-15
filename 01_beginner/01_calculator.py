number1 = float(input("Input first number: "))
number2 = float(input("Input second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation =="+":
    result = number1 + number2
elif operation == "-":
    result = number1 - number2
elif operation == "*":
    result = number1 * number2
elif operation == "/":
    if number2 == 0:
        print("Error: Division by zero is not allowed.")
        exit()
    result = number1 / number2
else:
    print("Error: Invalid operation. Please enter either +, -, *, or /.")
    exit()

print (f"Result {result}")