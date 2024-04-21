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
    num1, den1 = map(int, x.split('/'))
    num2, den2 = map(int, n.split('/'))

    # Find the greatest common divisor of the numerators and denominators
    gcd_num, gcd_den = gcd(num1, num2), gcd(den1, den2)

    # Simplify the fraction by dividing both numerator and denominator by their gcd
    simplified_x = str(num1 // gcd_num) + '/' + str(den1 // gcd_den)

    # Check if the simplified fraction is equal to the given n
    return simplified_x == n

def gcd(a, b):
    """Your task is to implement the Euclidean Algorithm to find the greatest common divisor of two numbers.

    gcd(15, 21) = 3
    gcd(13, 12) = 1
    """
    # Your code here
    while b != 0:
        a, b = b, a % b
    return a

# Test cases
print(simplify("1/5", "5/1")) # True
print(simplify("1/6", "2/1")) # False
print(simplify("7/10", "10/2")) # False
print(simplify("1/3", "2/3")) # True
print(simplify("1/4", "1/2")) # False
print(simplify("3/4", "1/2")) # True
print(simplify("1/7", "1/14")) # True
print(simplify("1/8", "3/8")) # True
print(simplify("1/9", "3/9")) # True
print(simplify("1/11", "2/11")) # True
print(simplify("1/12", "1/3")) # False</s>