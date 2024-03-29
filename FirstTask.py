import math


def diagonal(a, b):
    return round(math.sqrt((a ** 2 + b ** 2)), 2)


def area(a, b):
    return a * b


def perimeter(a, b):
    return (a + b) * 2


def dictionary(a, b):
    return {'Diagonal': diagonal(a, b), 'Area': area(a, b), 'Perimeter': perimeter(a, b)}


if __name__ == '__main__':
    print('Result:', dictionary(a=13, b=17))
