def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    """
    if isinstance(a, int) and isinstance(b, int):
        return max(a, b)
    elif isinstance(a, float) and isinstance(b, float):
        return max(a, b)
    elif isinstance(a, str) and isinstance(b, str):
        return max(a, b)
    else:
        return None


def compare_two(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_two(1, 2.5) ➞ 2.5
    compare_two(1, "2,3") ➞ "2,3"
    compare_two("5,1", "6") ➞ "6"
    compare_two("1", 1) ➞ None
    """
    if isinstance(a, int) and isinstance(b, int):
        return max(a, b)
    elif isinstance(a, float) and isinstance(b, float):
        return max(a, b)
    elif isinstance(a, str) and isinstance(b, str):
        return max(a, b)
    else:
        return None


def compare_three(a, b, c):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_three(1, 2.5, "3") ➞ 2.5
    compare_three(1, "2,3", "5") ➞ "5"
    compare_three("5,1", "6", "7") ➞ "7"
    compare_three("1", 1, "1") ➞ None
    """
    if isinstance(a, int) and isinstance(b, int) and isinstance(c, int):
        return max(a, b, c)
    elif isinstance(a, float) and isinstance(b, float) and isinstance(c, float):
        return max(a, b, c)
    elif isinstance(a, str) and isinstance(b, str) and isinstance(c, str):
        return max(a, b, c)
    else:
        return None


def compare_four(a, b, c, d):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_four(1, 2.5, "3", "4") ➞ 2.5
    compare_four(1, "2,3", "5", "6") ➞ "6"
    compare_four("5,1", "6", "7", "8") ➞ "8"
    compare_four("1", 1, "1", "1") ➞ None
    """
    if isinstance(a, int) and isinstance(b, int) and isinstance(c, int) and isinstance(d, int):
        return max(a, b, c, d)
    elif isinstance(a, float) and isinstance(b, float) and isinstance(