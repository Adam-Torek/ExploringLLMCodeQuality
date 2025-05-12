def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
    x_numerator, x_denominator = map(int, x.split('/'))
    n_numerator, n_denominator = map(int, n.split('/'))

    if x_denominator * n_numerator % n_denominator == 0:
        return True
    else:
        return False


# Test cases
print(simplify("1/5", "5/1"))  # True
print(simplify("1/6", "2/1"))  # False
print(simplify("7/10", "10/2"))  # False
print(simplify("1/2", "1/4"))  # True
print(simplify("1/3", "1/3"))  # True
print(simplify("1/4", "1/2"))  # False
print(simplify("1/2", "1/4"))  # True
print(simplify("1/3", "1/6"))  # False
print(simplify("1/6", "1/3"))  # True
print(simplify("1/10", "1/6"))  # True
print(simplify("1/10", "5/6"))  # False
print(simplify("1/10", "7/6"))  # False
print(simplify("1/10", "1/10"))  # True
print(simplify("1/10", "11/10"))  # False
print(simplify("1/10", "13/10"))  # False
print(simplify("1/10", "17/10"))  # False
print(simplify("1/10", "19/10"))  # False
print(simplify("1/10", "23/10"))  # False
print(simplify("1/10", "29/10"))  # False
print(simplify("1/10", "31/10"))  # False
print(simplify("1/10", "37/10"))  # False
print(simplify("1/10", "41/10"))  # False
print(simplify("1/10", "47/10"))  # False
print(simplify("1/10", "53/10"))  # False
print(simplify("1/10", "59/10"))  # False
print(simplify("1/10", "61/10"))  # False
print(simplify("1/10", "67/10"))  # False
print(simplify("1/10", "71/10"))  # False
print(simplify("1/10", "73/10"))  # False
print(simplify("1/10", "79/10"))  # False
print(simplify("1/10", "83/10"))  # False
print(simplify("1/10", "89/10"))  # False
print(simplify("1/10", "97/10"))  # False
print(simplify("1/10", "101/10"))  # False
print(simplify("1/10", "103/10"))  # False
print(simplify("