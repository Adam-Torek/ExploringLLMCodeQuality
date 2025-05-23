def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    count = 0
    even = 0
    odd = 0
    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            even += 1
        else:
            odd += 1
        num //= 10
    return (even, odd)


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    result = even_odd_count(num)
    print(result)