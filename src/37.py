import numpy as np
from scipy.stats import uniform

def calculate_probability(x):
    """
    Calculate the probability using the uniform distribution.
    
    Parameters:
    x (float): The input value to be evaluated.
    
    Returns:
    float: The calculated probability.
    """
    if x < 0 or x > 1:
        return 0.0
    else:
        # Use scipy.stats.uniform.rvs for the distribution, we need to use np.random instead of uniform for CPython compatibility
        return np.random.rand() * (1 - x) + x

# Example usage
probability = calculate_probability(0.5)
print(f"The probability is: {probability}")
