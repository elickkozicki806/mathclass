def generate_random_code():
    import random
    
    # Generate a random number between 1 and 50
    num = random.randint(1, 50)
    
    # Use the number to create a random equation
    if num % 2 == 0:
        return f"{num} + {random.randint(1, num)}"
    else:
        return f"{num} - {random.randint(1, num)}"
