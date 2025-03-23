def find_common_factors(n):
    """
    This function finds all common factors of n.
    
    Args:
        n (int): An integer to be checked for factors.
        
    Returns:
        list: A list of integers that are common factors of n.
    """
    if n == 0 or n < 1:
        return []
    factors = [i for i in range(1, n + 1) if n % i == 0]
    return sorted(factors)

def prime_factorization(n):
    """
    This function returns the prime factorization of a given integer.
    
    Args:
        n (int): An integer to be factorized.
        
    Returns:
        list: A list of integers representing the prime factors and their exponents.
    """
    if n == 0 or n < 1:
        return []
    
    factors = {}
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            if i not in factors:
                factors[i] = 0
            factors[i] += 1
            n //= i
    
    if n > 1:
        if n not in factors:
            factors[n] = 0
        return [n]
    
    # List of prime factors and their exponents, sorted by increasing order.
    factor_list = [(k, v) for k, v in sorted(factors.items(), key=lambda item: (item[1], item[0]))]
    return factor_list

def main():
    n = 48
    common_factors = find_common_factors(n)
    print("Common factors of", n, "are:", common_factors)
    
    prime_factorization_result = prime_factorization(n)
    if prime_factorization_result:
        print("Prime factorization of", n, "is:")
        for factor in prime_factorization_result:
            print(factor[0], "^", factor[1])

if __name__ == "__main__":
    main()
