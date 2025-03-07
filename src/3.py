import random

def get_random_code(length):
    """Generate a random string of letters and digits"""
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(random.choice(letters) for i in range(length))
