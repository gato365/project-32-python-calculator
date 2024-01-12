def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

# Main program starts here
while True:
    # User input
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (add, subtract, multiply, divide): ")

    # Perform calculation
    if operation == 'add':
        result = add(num1, num2)
    elif operation == 'subtract':
        result = subtract(num1, num2)
    elif operation == 'multiply':
        result = multiply(num1, num2)
    elif operation == 'divide':
        result = divide(num1, num2)
    else:
        result = "Invalid operation"

    print("Result:", result)

    # Check if the user wants to perform another calculation
    next_calculation = input("Do another calculation? (yes/no): ")
    if next_calculation.lower() != 'yes':
        break
