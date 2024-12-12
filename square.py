def area(a):
    return a ** 2


def perimeter(a):
    if not isinstance(a, (int, float)):
        raise TypeError("Argument 'a' must be a number.")
    return 4 * a
