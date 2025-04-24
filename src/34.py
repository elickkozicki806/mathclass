def fibonacci(n):
    """
    Calculate Fibonacci sequence up to n-th number.
    
    Parameters:
    n (int): Number of elements in the Fibonacci sequence
    
    Returns:
    list: A list containing the first 'n' numbers of the Fibonacci sequence
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Example usage:
fib_gen = fibonacci(10)
for num in fib_gen:
    print(num)
