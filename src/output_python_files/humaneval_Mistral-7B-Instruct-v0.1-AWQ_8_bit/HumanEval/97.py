def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """
    # convert the integers to strings
    a_str = str(a)
    b_str = str(b)
    # find the unit digits of the integers
    a_digit = int(a_str[-1])
    b_digit = int(b_str[-1])
    # multiply the unit digits
    product = a_digit * b_digit
    # return the product
    return product