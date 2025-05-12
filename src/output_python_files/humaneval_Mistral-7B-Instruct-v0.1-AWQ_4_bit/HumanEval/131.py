def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n % 2 == 0:
        return 0
    else:
        dig = 0
        while n > 0:
            dig += n % 10
            n //= 10
        return dig


def main():
    n = int(input("Enter a positive integer: "))
    if n < 0:
        print("Invalid input. Please enter a positive integer.")
    else:
        print(digits(n))


if __name__ == "__main__":
    main()