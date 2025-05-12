def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Your code here
    product = 1
    n_str = str(n)
    for digit in n_str:
        if int(digit) % 2 != 0:
            product *= int(digit)
    return product

# Test cases
print(digits(1))
print(digits(4))
print(digits(235))
print(digits(12345))
print(digits(123045))
print(digits(123004500))