def area(a, b, c):
    p = (a + b + c) / 2
    s = p * (p - a) * (p - b) * (p - c)
    return s ** 0.5


def perimeter(a, b, c):
    return a + b + c
