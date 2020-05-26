import sys


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        return "ERROR (div by zero)"
    return a / b


def mod(a, b):
    if b == 0:
        return "ERROR (modulo by zero)"
    return a % b


def operation(argv):
    if len(argv) == 1:
        print("Usage: python operations.py <number1> <number2>")
        print("Example:\n   python operations.py 10 3")
    elif len(argv) > 3:
        print("InputError: too many arguments\n")
        print("Usage: python operations.py <number1> <number2>")
        print("Example:\n   python operations.py 10 3")
    elif len(argv) == 3 and (argv[1].isdigit() == 0 or argv[2].isdigit() == 0):
        print("InputError: only numbers\n")
        print("Usage: python operations.py <number1> <number2>")
        print("Example:\n   python operations.py 10 3")
    elif len(argv) == 3 and (argv[1].isdigit() == 1 or argv[2].isdigit() == 1):
        print("Sum: ", add(int(argv[1]), int(argv[2])))
        print("Difference: ", sub(int(argv[1]), int(argv[2])))
        print("Product: ", mul(int(argv[1]), int(argv[2])))
        print("Quotient: ", div(int(argv[1]), int(argv[2])))
        print("Remainder: ", mod(int(argv[1]), int(argv[2])))


operation(sys.argv)
