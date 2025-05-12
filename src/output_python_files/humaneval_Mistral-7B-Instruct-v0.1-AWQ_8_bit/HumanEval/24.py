def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Find the largest divisor of n
    for i in range(1, n):
        if n % i == 0:
            return i
    return 1


def main():
    # Test the function
    num = int(input("Enter a number: "))
    print(f"The largest divisor of {num} is {largest_divisor(num)}")


if __name__ == "__main__":
    main()