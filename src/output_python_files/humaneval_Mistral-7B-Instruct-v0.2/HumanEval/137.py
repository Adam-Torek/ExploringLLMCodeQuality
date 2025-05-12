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
        raise TypeError("Both variables must be of the same type: int, float or string")


# Testing
print(compare_one(1, 2.5))
print(compare_one(1, "2,3"))
print(compare_one("5,1", "6"))
print(compare_one("1", 1))
print(compare_one("1", "1"))
print(compare_one("1", "1.1"))
print(compare_one("1.1", "1"))
print(compare_one("1.1", "1.1"))
print(compare_one("1.1", "1.2"))
print(compare_one("1.1", "1.2e0"))
print(compare_one("1.1e0", "1.2"))
print(compare_one("1.1e0", "1.2e0"))
print(compare_one("1.1e-1", "1.2e-1"))
print(compare_one("1.1e-1", "1.2e-10"))
print(compare_one("1.1e-10", "1.2e-1"))
print(compare_one("1.1e-10", "1.2e-10"))
print(compare_one("1.1e-10", "1.2e-20"))
print(compare_one("1.1e-20", "1.2e-10"))
print(compare_one("1.1e-20", "1.2e-20"))
print(compare_one("1.1e-20", "1.2e-30"))
print(compare_one("1.1e-30", "1.2e-20"))
print(compare_one("1.1e-30", "1.2e-30"))
print(compare_one("1.1e-30", "1.2e-40"))
print(compare_one("1.1e-40", "1.2e-30"))
print(compare_one("1.1e-40", "1.2e-40"))
print(compare_one("1.1e-40", "1.2e-50"))
print(compare_one("1.1e-50", "1.2e-40"))
print(compare_one("1.1e-50", "1.2e-50"))
print(compare_one("1.1e-50", "1.2e-60"))
print(compare_one("1.1e-60", "1.2e-5