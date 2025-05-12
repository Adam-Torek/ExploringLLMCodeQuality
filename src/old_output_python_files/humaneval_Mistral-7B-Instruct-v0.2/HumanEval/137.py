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
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None

    elif isinstance(a, str) and isinstance(b, str):
        if float(a) > float(b):
            return a
        elif float(a) < float(b):
            return b
        else:
            return None

    elif isinstance(a, (int, float)) and isinstance(b, str):
        if float(a) > float(b):
            return a
        elif float(a) < float(b):
            return b
        else:
            return None

    elif isinstance(a, str) and isinstance(b, (int, float)):
        if float(a) > b:
            return a
        elif float(a) < b:
            return b
        else:
            return None

    else:
        raise TypeError("Invalid input types")


# Testing
print(compare_one(1, 2.5))
print(compare_one(1, "2,3"))
print(compare_one("5,1", "6"))
print(compare_one("1", 1))
print(compare_one("1", "1.0"))
print(compare_one("1.1", "1.1"))
print(compare_one("1.1", "1.2"))
print(compare_one("1.1", "1.20"))
print(compare_one("1.1", "1.200"))
print(compare_one("1.1", "1.2000"))
print(compare_one("1.1", "1.20000"))
print(compare_one("1.1", "1.200000"))
print(compare_one("1.1", "1.2000000"))
print(compare_one("1.1", "1.20000000"))
print(compare_one("1.1", "1.200000000"))
print(compare_one("1.1", "1.2000000000"))
print(compare_one("1.1", "1.20000000000"))
print(compare_one("1.1", "1.200000000000"))
print(compare_one("1.1", "1.2000000000000"))
print(compare_one("1.1", "1.20000000000000"))
print(compare_one("1.1", "1.200000000000000"))
print(compare_one("1.1", "1.2000000000000000"))
print(compare_one("1.1", "1.20000000000000000"))
print(compare_one("1.1", "1.200000000000000000"))
print(compare_one("1.1", "1.2000000000000000000"))
print(compare_one("1.1", "1.20000000000000000000"))
print(compare_one("1.1", "1.20000000