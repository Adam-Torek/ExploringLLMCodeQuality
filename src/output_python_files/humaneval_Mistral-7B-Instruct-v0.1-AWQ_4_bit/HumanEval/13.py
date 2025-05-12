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


def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = greatest_common_divisor(a, b)
    print(f"The greatest common divisor of {a} and {b} is {result}")


if __name__ == "__main__":
    main()