def calculate_area(shape, dimensions):
    if shape == 'circle':
        radius = dimensions[0]
        area = 3.14 * (radius ** 2)
        return area

    elif shape == 'square':
        side_length = dimensions[0]
        area = side_length ** 2
        return area

    else:
        print("Unsupported shape")
        return None
