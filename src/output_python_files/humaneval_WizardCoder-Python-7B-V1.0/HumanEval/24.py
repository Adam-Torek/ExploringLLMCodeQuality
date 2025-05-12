def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in range(n-1, 1, -1, -1):
        if n % i == 0:
            return i


def main():
    n = int(input("Enter a number: "))
    print("Largest divisor smaller than", n, "is", largest_divisor(n))

if __name__ == "__main__":
    main()