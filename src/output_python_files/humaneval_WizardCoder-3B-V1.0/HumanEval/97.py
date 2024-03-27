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

def unit_digits(n):
    """Return a list of the unit digits of the given number."""
    return [int(d) for d in str(n) if int(d)!= 0]

def multiply_unit_digits(a, b):
    """Return the product of the unit digits of the given numbers."""
    return sum(a * b for a, b in zip(unit_digits(a), unit_digits(b)))

def main():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("The product of the unit digits of", a, "and", b, "is", multiply_unit_digits(a, b))

if __name__ == "__main__":
    main()<|endoftext|>