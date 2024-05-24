def add(x, y):
    """Adds two numbers."""
    return x + y

def subtract(x, y):
    """Subtracts second number from the first."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers."""
    return x * y

def divide(x, y):
    """Divides first number by the second. Raises an error if the second number is zero."""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def main():
    print("Select operation:")
    print("1. +")
    print("2. -")
    print("3. x")
    print("4. /")

    choice = input("Enter choice(1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"The result is: {add(num1, num2)}")
        elif choice == '2':
            print(f"The result is: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result is: {multiply(num1, num2)}")
        elif choice == '4':
            try:
                print(f"The result is: {divide(num1, num2)}")
            except ValueError as e:
                print(e)
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()