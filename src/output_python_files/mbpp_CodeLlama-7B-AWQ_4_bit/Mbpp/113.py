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
    print(check_integer("123"))
    print(check_integer("123.45"))
    print(check_integer("123.45e-2"))
    print(check_integer("123.45e+2"))
    print(check_integer("123.45e-2"))
    print(check_integer("123.45e+2"))
    print(check_integer("123.45e-2"))
    print(check_integer("123.45e+2"))
    print(check_integer("123.45e-2"))
    print(check_integer("123.45e+2"))
    print(check_integer("123.45e-2"))
    print(check_integer("123.45e+2"))
    print(check_integer("123.45e-2"))
    print(check_integer("123.45e+2"))
    print(check_integer("123.45e-2"))
    print(check_integer("123.45e+2"))
    print(check_integer("123.45e-2"))
    print(check_integer("123.45e+2"))
    print(check_integer("123.45e-2"))
    print(check_integer("123.45e+2"))
    print(check_integer("123.45e-2"))
    print(check_integer("123.45e+2"))
    print(check_integer("123.45e-2"))
    print(check_integer("123.45e+2"))
    print(check_integer("123.45e-2"))
    print(check_integer("123.45e+2"))
    print(check_integer("123.45e-2"))
    print(check_integer("123.45e+2"))
    print(check_integer("123.45e-2"))
    print(check_integer("123.45e+2"))
    print(check_integer("123.45e-2"))
    print(check_integer("123.45e+2"))
    print(check_integer("123.45e-2"))
    print(check_integer("123.45e+2"))
    print(check_integer("123.45e-2"))
    print(check_integer("123.45e+2"))
    print(check_integer("123.45e-2"))
    print(check_integer("123.45e+2"))
    print(check_integer("123.45e-2"))
    print(check_integer("123.45e+2"))
    print(check_integer("123.45e-2"))
    print(check_integer("123.45e+2"))
    print(check_integer("123.45e-2"))
    print(check_integer("123.45e+2"))
    print(check_integer("123.45e-2"))
    print(check_integer("123.45e+2"))
    print(check_integer("123.45e-2"))
    print(check_integer("123.45e+2"))