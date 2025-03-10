
import random

def get_random_python_code():
    operators = ["+", "-", "*", "/", "%"]
    operands = [str(i) for i in range(10)]
    equations = []
    for _ in range(3):
        equation = ""
        for _ in range(4):
            operand1 = random.choice(operands)
            operand2 = random.choice(operands)
            operator = random.choice(operators)
            equation += f"{operand1} {operator} {operand2}"
        equations.append(equation)
    return "".join(equations)