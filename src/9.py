import random

def random_python_code():
    operators = ['+', '-', '*', '/', '%']
    variables = ['x', 'y', 'z']
    statements = ['if', 'for', 'while']
    functions = ['sqrt', 'sin', 'cos', 'tan']
    
    code = ''
    
    for i in range(random.randint(2, 5)):
        operator = random.choice(operators)
        variable = random.choice(variables)
        
        if operator == '+':
            code += f'{variable} {operator} {random.randint(1, 10)}'
            
        elif operator == '-':
            code += f'{variable} {operator} {random.randint(1, 10)}'
        
        elif operator == '*':
            code += f'{variable} {operator} {random.randint(1, 10)}'
            
        elif operator == '/':
            code += f'{variable} {operator} {random.randint(1, 10)}'
        
        else:
            code += f'{variable} {operator} {random.randint(1, 10)}'
            
    for i in range(random.randint(2, 5)):
        statement = random.choice(statements)
        
        if statement == 'if':
            code += f'{statement} {variable} > {random.randint(1, 10)}:'
            
        elif statement == 'for':
            code += f'{statement} {variable} in range({random.randint(1, 10)}, {random.randint(1, 10)}):'
            
        else:
            code += f'{statement} {variable} > {random.randint(1, 10)}:'
    
    for i in range(random.randint(2, 5)):
        function = random.choice(functions)
        
        if function == 'sqrt':
            code += f'{function}({variable})'
            
        elif function == 'sin':
            code += f'{function}({variable})'
            
        elif function == 'cos':
            code += f'{function}({variable})'
            
        else:
            code += f'{function}({variable})'
            
    return code