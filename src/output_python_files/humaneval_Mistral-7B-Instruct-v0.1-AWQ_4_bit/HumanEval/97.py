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
    a_unit = a_str[-1]
    b_unit = b_str[-1]
    # convert the unit digits back to integers
    a_unit = int(a_unit)
    b_unit = int(b_unit)
    # multiply the unit digits
    product = a_unit * b_unit
    # return the product
    return product