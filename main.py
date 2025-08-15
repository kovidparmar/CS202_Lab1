# calculator.py
# A simple calculator program with multiple operations
# Written for demonstration purposes with more than 30 lines of code excluding comments

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the quotient of two numbers, raises error if dividing by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def modulus(a, b):
    """Return the remainder when a is divided by b."""
    if b == 0:
        raise ValueError("Cannot find modulus with zero divisor")
    return a % b

def power(a, b):
    """Return a raised to the power of b."""
    return a ** b

def calculator():
    """Interactive calculator loop."""
    print("Simple Calculator")
    print("Operations: add, subtract, multiply, divide, modulus, power, quit")

    while True:
        op = input("\nEnter operation: ").strip().lower()

        if op == "quit":
            print("Exiting calculator.")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if op == "add":
            print("Result:", add(num1, num2))
        elif op == "subtract":
            print("Result:", subtract(num1, num2))
        elif op == "multiply":
            print("Result:", multiply(num1, num2))
        elif op == "divide":
            try:
                print("Result:", divide(num1, num2))
            except ValueError as e:
                print(e)
        elif op == "modulus":
            try:
                print("Result:", modulus(num1, num2))
            except ValueError as e:
                print(e)
        elif op == "power":
            print("Result:", power(num1, num2))
        else:
            print("Unknown operation. Try again.")

if __name__ == "__main__":
    calculator()
