import random
def get_random_python_code():
    code = ""
    for i in range(10):
        op = random.choice(["+", "-", "*", "/"])
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        code += f"{a} {op} {b}"
    return code