 import random
import string
def generate_code(n):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(n))