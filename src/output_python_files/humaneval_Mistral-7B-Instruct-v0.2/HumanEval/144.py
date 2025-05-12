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
    # Your code here
    x_num, x_denom = map(int, x.split('/'))
    n_num, n_denom = map(int, n.split('/'))

    # Find the greatest common divisor of the numerators and denominators
    gcd = math.gcd(x_num, n_num)
    gcd_denom = math.gcd(x_denom, n_denom)

    # Simplify the fractions by dividing both the numerator and denominator by their greatest common divisor
    simplified_x = str(x_num // gcd) + '/' + str(x_denom // gcd)
    simplified_n = str(n_num // gcd_denom) + '/' + str(n_denom // gcd_denom)

    # Check if the simplified expression evaluates to a whole number
    simplified_x_num, simplified_x_denom = map(int, simplified_x.split('/'))
    return simplified_x_num * simplified_n_denom == simplified_x_denom * simplified_n_num

# Test cases
print(simplify("1/5", "5/1")) # True
print(simplify("1/6", "2/1")) # False
print(simplify("7/10", "10/2")) # False
print(simplify("1/2", "1/2")) # True
print(simplify("3/4", "2/3")) # False
print(simplify("1/3", "1/3")) # True
print(simplify("2/5", "1/2")) # False
print(simplify("1/2", "3/4")) # False
print(simplify("1/2", "1/2")) # True
print(simplify("1/2", "1/1")) # True
print(simplify("1/2", "2/1")) # False
print(simplify("1/2", "1/3")) # False
print(simplify("1/2", "1/6")) # False
print(simplify("1/2", "1/12")) # False
print(simplify("1/2", "2/3")) # False
print(simplify("1/2", "3/2")) # False
print(simplify("1/2", "4/3")) # False
print(simplify("1/2", "5/3")) # False
print(simplify("1/2", "6/3")) # False
print(simplify("1/2", "7/3")) # False
print(simplify("1/2", "8/3")) # False
print(simplify("1/2", "9/3")) # False
print(simplify("1/2", "10/3")) # False
print(simplify("1/2", "11/3")) # False
print(simplify("1/2", "12/3")) # False
print(simplify("1/2", "13/3")) # False
print(simplify("1/2", "14/3")) # False
print(simplify("1/2", "15/3")) # False
print(simplify("1/2", "16/3")) # False
print(simplify("1/2", "17/3")) # False
print(sim