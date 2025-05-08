def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

def main():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    if choice == '1':
        result = add(x, y)
    elif choice == '2':
        result = subtract(x, y)
    elif choice == '3':
        result = multiply(x, y)
    elif choice == '4':
        result = divide(x, y)
    else:
        result = "Invalid choice"

    print("Result:", result)

main()
