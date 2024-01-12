# num1 = 3
# num2 = 4

# print(num1 * num2)

## Add
def add(num1, num2):
    return num1 + num2

## Subtract
def subtract(num1, num2):
    return num1 - num2

## Multiple
def multiply(num1, num2):
    return num1 * num2

## Divide
def divide(num1, num2):
    if num2 == 0:
        return "Cannot have 0 in denominator"
    return num1/num2


# result = divide(3,9)

while True:
    num1 = float(input("State 1st number: "))
    num2 = float(input("State 2nd number: "))
    operation = input("Select operator (add, subtract, multiply, or divide): ")

    if operation == "add":
        result = add(num1,num2)
    elif operation == "subtract":
        result = subtract(num1,num2)
    elif operation == "multiply":
        result = multiply(num1,num2)
    elif operation == "divide":
        result = divide(num1,num2)
    else:
        result = "Incorrect Opertation"

    print("Result: " ,result)
    
    response = input("Do you want to compute another calculation?")
    
    if response == "no":
        break