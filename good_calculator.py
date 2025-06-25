"""Simple calculator using clean& documented code
Principles used from lecture: KISS, DRY, Document Your Code, and Clean Code
"""

def addition(a, b):
    # Return the sum of a and b
    return a + b
def subtract(a, b):
    # Return the difference between a and b
    return a - b
def multiply(a, b):
    # Return the product of a and b
    return a * b
def divide(a,b):
    # Return result of dividing a by b. Handles division by zero
    if b == 0:
        return "Error, cannot divide by zero"
    return a / b

def get_user_input():
    # Prompt user for two numbers. Returns computed value.
    try:
        # Ask user for two numbers and convert to float
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    # Handle non-numeric input
    except ValueError:
        print ("Invalid input. Please enter numeric values.")
        return None, None


def main():
    # Main function that controls calculator flow
    print ("Welcome to the simple calculator!")
    print ("Choose an operation: add, subtract, multiply, divide")

    # Read user input and normalize it to lowercase
    operation = input("Choose an operation: ").strip().lower()
    num1, num2 = get_user_input()

    # Null number handling if the number is non-numeric, exit the main function
    if num1 is None or num2 is None:
        return

    # Define a dictionary that maps operation names to functions
    operations = {"add": addition, "subtract": subtract, "multiply": multiply, "divide": divide}

    # Perform the operation if it's valid
    if operation in operations:
        result = operations[operation](num1, num2)
        print ("Result:", result)
    else:
        print ("Invalid input. Please enter numeric values.")

# Only run the main function if the script executed directly
if __name__ == "__main__":
    main()

