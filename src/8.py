import random
def get_random_code():
    # Define a list of operators
    operators = ['+', '-', '*', '/']
    # Generate a random operator
    op = random.choice(operators)
    # Generate two random numbers
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    # Return the code
    return f'{num1} {op} {num2}'