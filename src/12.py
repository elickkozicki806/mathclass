import random

def generate_random_code():
    # Generate a random number between 1 and 10
    num = random.randint(1, 10)
    # Generate a random operator (+, -, *, /)
    op = random.choice(["+", "-", "*", "/"])
    # Generate two random numbers to operate on
    rand_num1 = random.randint(1, 10)
    rand_num2 = random.randint(1, 10)
    # Evaluate the expression using eval() function
    result = eval(f"{rand_num1} {op} {rand_num2}")
    return f"{result}"
