"""
Write a function to check if a string represents an integer or not.
assert check_integer("python")==False
"""


def check_integer(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    print(check_integer("python"))
    print(check_integer("12345"))
    print(check_integer("12345.12345"))
    print(check_integer("12345.12345e12"))
    print(check_integer("12345e12"))
    print(check_integer("12345e-12"))
    print(check_integer("12345e+12"))
    print(check_integer("12345e"))
    print(check_integer("12345e12.12345"))
    print(check_integer("12345e12.12345e12"))
    print(check_integer("12345e12.12345e-12"))
    print(check_integer("12345e12.12345e+12"))
    print(check_integer("12345e12.12345e"))
    print(check_integer("12345e12.12345e12.12345"))
    print(check_integer("12345e12.12345e12.12345e12"))
    print(check_integer("12345e12.12345e12.12345e-12"))
    print(check_integer("12345e12.12345e12.12345e+12"))
    print(check_integer("12345e12.12345e12.12345e"))
    print(check_integer("12345e12.12345e12.12345e12.12345"))
    print(check_integer("12345e12.12345e12.12345e12.12345e12"))
    print(check_integer("12345e12.12345e12.12345e12.12345e-12"))
    print(check_integer("12345e12.12345e12.12345e12.12345e+12"))
    print(check_integer("12345e12.12345e12.12345e12.12345e"))
    print(check_integer("12345e12.12345e12.12345e12.12345e12.12345"))
    print(check_integer("12345e12.12345e12.12345e12.12345e12.12345e12"))
    print(check_integer("12345e12.12345e12.12345e12.12345e12.12345e-12"))
    print(check_integer("12345e12.12345e12.12345e12.12345e12.12345e+12"))
    print(check