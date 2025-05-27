import numpy as np
def calculate_area(length, width):
    """
    Calculate the area of a rectangle

    :param length: Length of the rectangle
    :type length: float or int
    :param width: Width of the rectangle
    :type width: float or int
    :return: Area of the rectangle
    :rtype: float
    """
    return length * width

if __name__ == "__main__":
    # Example usage
    length = 5.0
    width = 3.5
    area = calculate_area(length, width)
    print(f"The area of the rectangle with length {length} and width {width} is: {area}")
