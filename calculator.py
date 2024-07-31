# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def main():
    import sys
    if len(sys.argv) != 4:
        print("Usage: python calculator.py <operation> <num1> <num2>")
        sys.exit(1)

    operation = sys.argv[1]
    num1 = float(sys.argv[2])
    num2 = float(sys.argv[3])

    if operation == 'add':
        print(add(num1, num2))
    elif operation == 'subtract':
        print(subtract(num1, num2))
    elif operation == 'multiply':
        print(multiply(num1, num2))
    elif operation == 'divide':
        try:
            print(divide(num1, num2))
        except ValueError as e:
            print(e)
    else:
        print("Unknown operation")

if __name__ == "__main__":
    main()
