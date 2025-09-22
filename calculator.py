

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

print("Simple Calculator")
print("Operations: +  -  *  /")

while True:
    choice = input("Enter operation (+, -, *, /) or q to quit: ")
    if choice == "q":
        break
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "+":
        print("Result:", add(num1, num2))
    elif choice == "-":
        print("Result:", subtract(num1, num2))
    elif choice == "*":
        print("Result:", multiply(num1, num2))
    elif choice == "/":
        print("Result:", divide(num1, num2))
    else:
        print("Invalid operation. Try again.")

