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

def simplify_fraction(x, n):
    """
    This function takes two string representations of fractions as input and returns True if
    the simplified expression x * n evaluates to a whole number and False otherwise.
    """
    numerator, denominator = map(int, x.split('/'))
    simplified_numerator = numerator * int(n.split('/')[0])
    simplified_denominator = denominator * int(n.split('/')[1])
    if simplified_denominator == 0:
        return False
    else:
        return simplified_numerator // simplified_denominator == 0

# Test cases
print(simplify_fraction("1/5", "5/1"))  # True
print(simplify_fraction("1/6", "2/1"))  # False
print(simplify_fraction("7/10", "10/2"))  # False<|endoftext|>