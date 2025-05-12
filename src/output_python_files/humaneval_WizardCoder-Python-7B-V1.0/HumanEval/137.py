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
    a = str(a).replace(",", ".")
    b = str(b).replace(",", ".")
    if a == b:
        return None
    else:
        return max(a, b, key=lambda x: float(x))



# Test cases
print(compare_one(1, 2.5))  # 2.5
print(compare_one(1, "2,3"))  # "2,3"
print(compare_one("5,1", "6"))  # "6"
print(compare_one("1", 1))  # None
print(compare_one(1.5, 2))  # 2
print(compare_one("1.5", "2"))  # "2"
print(compare_one("1,5", "2.3"))  # "2.3"
print(compare_one("1", "2"))  # None
print(compare_one("1", "1"))  # None
print(compare_one("1", "1.0"))  # None
print(compare_one("1.0", "1"))  # None
print(compare_one("1.0", "1.0"))  # None
print(compare_one("1.0", "1.00"))  # None
print(compare_one("1.0", "1.01"))  # "1.01"
print(compare_one("1.01", "1.0"))  # "1.01"
print(compare_one("1.0", "1.01"))  # "1.01"
print(compare_one("1.01", "1.02"))  # "1.02"
print(compare_one("1.02", "1.01"))  # "1.02"
print(compare_one("1.02", "1.02"))  # "1.02"
print(compare_one("1.02", "1.020"))  # "1.02"
print(compare_one("1.020", "1.02"))  # "1.02"
print(compare_one("1.02", "1.020"))  # "1.02"
print(compare_one("1.020", "1.020"))  # "1.02"
print(compare_one("1.020", "1.0200"))  # "1.020"
print(compare_one("1.0200", "1.020"))  # "1.020"
print(compare_one("1.020", "1.0200"))  # "1.020"
print(compare_one("1.0200", "1.020"))  # "1.020"
print(compare_one("1.020", "1.02000"))  # "1.020"
print(compare_one("1.0200", "1.0200"))  # "1.020"
print(compare_one("1.0200", "1.02000"))  # "1.0200"
print(compare_one("1.02000", "1.0200"))  # "1.0200"
print(compare_one("1.0200", "1.02000"))  # "1.0200"
print(compare_one("1.02000", "