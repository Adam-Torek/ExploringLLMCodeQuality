"""
Write a function to calculate the value of 'a' to the power 'b'.
assert power(3,4) == 81
"""

def power(a,b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        return power(a,b/2) * power(a,b/2)
    else:
        return a * power(a,b-1)


def power_recursive(a,b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        return power_recursive(a,b/2) * power_recursive(a,b/2)
    else:
        return a * power_recursive(a,b-1)


def power_iterative(a,b):
    result = 1
    for i in range(b):
        result *= a
    return result


def power_iterative_2(a,b):
    result = a
    for i in range(b-1):
        result *= a
    return result


def power_iterative_3(a,b):
    result = a
    for i in range(b):
        result *= a
    return result


def power_iterative_4(a,b):
    result = a
    for i in range(b):
        result *= a
    return result


def power_iterative_5(a,b):
    result = a
    for i in range(b):
        result *= a
    return result


def power_iterative_6(a,b):
    result = a
    for i in range(b):
        result *= a
    return result


def power_iterative_7(a,b):
    result = a
    for i in range(b):
        result *= a
    return result


def power_iterative_8(a,b):
    result = a
    for i in range(b):
        result *= a
    return result


def power_iterative_9(a,b):
    result = a
    for i in range(b):
        result *= a
    return result


def power_iterative_10(a,b):
    result = a
    for i in range(b):
        result *= a
    return result


def power_iterative_11(a,b):
    result = a
    for i in range(b):
        result *= a
    return result


def power_iterative_12(a,b):
    result = a
    for i in range(b):
        result *= a
    return result


def power_iterative_13(a,b):
    result = a
    for i in range(b):
        result *= a
    return result


def power_iterative_14(a,b):
    result = a
    for i in range(b):
        result *= a
    return result


def power_iterative_15(a,b):
    result = a
    for i in range(b):
        result *= a
    return result


def power_iterative_16(a,b):
    result = a
    for i in range(b):
        result *= a
    return result


def power_iterative_17(a,b):
    result = a
    for i in range(b):
        result *= a
    return result


def power_iterative_18(a,b):
    result = a
    for i in range(b):
        result *= a
    return result


def power_iterative_19(a,b):
    result = a
    for i in range(b):
        result *= a
    return result


def power_iterative_20(a,b):
    result = a
    for i in range(b):
        result *= a
    return result


def power_iterative_21(a,b):
    result = a
    for i in range(b):
        result *= a
    return result


def