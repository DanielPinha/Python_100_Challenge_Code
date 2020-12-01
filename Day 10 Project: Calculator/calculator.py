import calculator_artwork


def sum_numbers(num1, num2):
    """"It will receive two numbers and return the sum of them"""
    return num1 + num2


def subtract_numbers(num1, num2):
    """"It will receive two numbers and return the first minus the second"""
    return num1 - num2


def multiply_numbers(num1, num2):
    """"It will receive two numbers and return the multiplication of them"""
    return num1 * num2


def divide_numbers(num1, num2):
    """It will receive two numbers and return the first divided by the second"""
    if num2 == 0:
        return "Cannot divide a number per zero"
    return num1 / num2


def calculate(num1, num2, operator, operator_dict):
    """it will receive the two numbers and the operator and it will return the correct operation result"""
    try:
        return operator_dict[operator](num1, num2)
    except KeyError:
        return "Invalid operator"


def request_input_until_float(input_text):
    """"it will receive the input text to show user and it will continue to request an input until it is a float num"""
    is_float = False
    while not is_float:
        try:
            float_num = float(input(input_text))
        except ValueError:
            print("Invalid input, please provide a number once prompted")
        else:
            is_float = True
    return float_num


def available_operators():
    """returns dictionary with available operators and its associated function that can be used in the calculator"""
    valid_operators_dict = {'+': sum_numbers,
                            '-': subtract_numbers,
                            '*': multiply_numbers,
                            '/': divide_numbers,
                            }
    return valid_operators_dict


# Print calculator artwork
print(calculator_artwork.logo)

# Request first number
first_number = request_input_until_float("What is the first number?: ")

# Create dictionary based on current available operators and its functions
current_operator_dict = available_operators()

# Loop until user is finished with program
is_user_finished = False
while not is_user_finished:
    # Show available operators and request user to pick one
    for symbol in current_operator_dict:
        print(symbol)
    operation = input("Pick a operator: ")

    # Request the second number
    second_number = request_input_until_float("What is the next number?: ")

    # Acquire result based on operator and inputted numbers and then prints result
    result = calculate(first_number, second_number, operation, current_operator_dict)
    print(f"{first_number} {operation} {second_number} = {result}")

    # Ask if wants to continue calculation with result, start a new calculation or abort program
    next_calculation = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new "
                             f"calculation or 'quit' to close the program\n")

    # user request to continue calculation with current result
    if next_calculation == 'y':
        # Previous result was invalid, request new first number
        if type(result) == str:
            print("Invalid Result cannot be use to continue calculation, please start new calculation")
            first_number = request_input_until_float("What is the first number?: ")
        # Previous result is valid and it will be assigned to first_number
        else:
            first_number = result
    # user request to start new calculation
    elif next_calculation == 'n':
        first_number = request_input_until_float("What is the first number?: ")
    # user request to quit program
    elif next_calculation == 'quit':
        is_user_finished = True
    # Unexpected input by user, handler will close program
    else:
        print("Invalid input, program will be closed")
        is_user_finished = True
