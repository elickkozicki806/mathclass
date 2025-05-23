def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    sequence = fibonacci(n-1)
    sequence.append(sequence[-1] + sequence[-2])
    return sequence

print(fibonacci(5))  # Output: [0, 1, 1, 2, 3, 5]
