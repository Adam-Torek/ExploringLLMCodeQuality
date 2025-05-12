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
    # Your code here
    return int(str(a)[-1]) * int(str(b)[-1])

# Test the function
print(multiply(148, 412))
print(multiply(19, 28))
print(multiply(2020, 1851))
print(multiply(14,-15))