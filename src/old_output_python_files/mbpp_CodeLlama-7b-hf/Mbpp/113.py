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
    print(check_integer("123.45e-10"))
    print(check_integer("123.45e-100"))
    print(check_integer("123.45e-1000"))
    print(check_integer("123.45e-10000"))
    print(check_integer("123.45e-100000"))
    print(check_integer("123.45e-1000000"))
    print(check_integer("123.45e-10000000"))
    print(check_integer("123.45e-100000000"))
    print(check_integer("123.45e-1000000000"))
    print(check_integer("123.45e-10000000000"))
    print(check_integer("123.45e-100000000000"))
    print(check_integer("123.45e-1000000000000"))
    print(check_integer("123.45e-10000000000000"))
    print(check_integer("123.45e-100000000000000"))
    print(check_integer("123.45e-1000000000000000"))
    print(check_integer("123.45e-10000000000000000"))
    print(check_integer("123.45e-100000000000000000"))
    print(check_integer("123.45e-1000000000000000000"))
    print(check_integer("123.45e-10000000000000000000"))
    print(check_integer("123.45e-100000000000000000000"))
    print(check_integer("123.45e-1000000000000000000000"))
    print(check_integer("123.45e-10000000000000000000000"))
    print(check_integer("123.45e-100000000000000000000000"))
    print(check_integer("123.45e-1000000000000000000000000"))
    print(check_integer("123.45e-10000000000000000000000000"))
    print(check_integer("123.45e-100000000000000000000000000"))
    print(check_integer("123.45e-1000000000000000000000000000"))
    print(check_integer("123.45e-10000000000000000000000000000"))