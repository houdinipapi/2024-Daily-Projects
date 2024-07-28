def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    else:
        return x / y


def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_operation():
    while True:
        operation = input("Enter an operator (+, -, *, /): ")
        if operation in ["+", "-", "*", "/"]:
            return operation
        else:
            print("Invalid operation. Please enter +, -, *, or /.")


def perform_calculation():
    num1 = get_number("Enter the first number: ")
    operation = get_operation()
    num2 = get_number("Enter the second number: ")

    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        result = divide(num1, num2)

    print(f"Result: {result}")


def main():
    while True:
        perform_calculation()
        again = (
            input("Do you want to perform another calculation? (yes/no): ")
            .strip()
            .lower()
        )
        if again != "yes":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
