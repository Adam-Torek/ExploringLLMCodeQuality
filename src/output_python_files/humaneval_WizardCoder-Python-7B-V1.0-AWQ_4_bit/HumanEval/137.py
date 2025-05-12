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
    a = float(a.replace(",", ".")) if isinstance(a, str) else a
    b = float(b.replace(",", ".")) if isinstance(b, str) else b
    
    if a == b:
        return None
    elif a > b:
        return a if isinstance(a, type(b)) else b
    else:
        return b if isinstance(b, type(a)) else a


# Test cases
print(compare_one(1, 2.5))  # 2.5
print(compare_one(1, "2,3"))  # "2,3"
print(compare_one("5,1", "6"))  # "6"
print(compare_one("1", 1))  # None
print(compare_one(1, "2,3"))  # "2,3"
print(compare_one("1", "2,3"))  # "2,3"
print(compare_one(1, 3))  # 3
print(compare_one("1", "3"))  # "3"
print(compare_one("1", "1"))  # None
print(compare_one(1, 1))  # None
print(compare_one("1", "1"))  # None
print(compare_one("1.5", "2.5"))  # "2.5"
print(compare_one("1,5", "2.5"))  # "2.5"
print(compare_one("1.5", "2,5"))  # "2,5"
print(compare_one("1.5", "2,5"))  # "2,5"
print(compare_one("1.5", "2.5"))  # "2.5"
print(compare_one("1.5", "2.5"))  # "2.5"
print(compare_one("1.5", "2,5"))  # "2,5"
print(compare_one("1.5", "2.5"))  # "2.5"
print(compare_one("1.5", "2.5"))  # "2.5"
print(compare_one("1.5", "2,5"))  # "2,5"
print(compare_one("1.5", "2.5"))  # "2.5"
print(compare_one("1.5", "2.5"))  # "2.5"
print(compare_one("1.5", "2,5"))  # "2,5"
print(compare_one("1.5", "2.5"))  # "2.5"
print(compare_one("1.5", "2.5"))  # "2.5"
print(compare_one("1.5", "2,5"))  # "2,5"
print(compare_one("1.5", "2.5"))  # "2.5"
print(compare_one("1.5", "2,5"))  # "2,5"
print(compare_one("1.5", "2.5"))  # "2.5"
print(compare_one("1.5", "2,5"))  # "2,5"
print(compare_one("1.5", "2.5"))  # "2.5"
print(compare_one("1.5", "2,5"))  # "2,5"
print(compare_one("1.5", "2.5"))  # "2.5"
print(compare_one("1.5", "2,5"))  # "2,5"
print(compare_one