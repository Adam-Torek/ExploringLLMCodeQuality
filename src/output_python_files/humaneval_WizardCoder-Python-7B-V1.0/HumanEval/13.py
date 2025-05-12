def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    if b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)


def least_common_multiple(a: int, b: int) -> int:
    """ Return a least common multiple of two integers a and b
    >>> least_common_multiple(3, 5)
    15
    >>> least_common_multiple(25, 15)
    30
    """
    return a * b // greatest_common_divisor(a, b)

def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Greatest Common Divisor:", greatest_common_divisor(a, b))
    print("Least Common Multiple:", least_common_multiple(a, b))

if __name__ == "__main__":
    main()