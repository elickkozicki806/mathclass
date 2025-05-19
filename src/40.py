def calculate_sums(numbers):
    total_sum = sum(numbers)
    even_sum = sum(filter(lambda x: x % 2 == 0, numbers))
    odd_sum = sum(abs(x) for x in numbers if x > 0)
    
    return total_sum, even_sum, odd_sum

numbers = [1, 2, 3, -4, 5, -6]
result = calculate_sums(numbers)
print("Total Sum:", result[0])
print("Even Sum:", result[1])
print("Odd Sum:", result[2])
