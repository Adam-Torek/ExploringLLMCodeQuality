def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    count = 0
    for num in arr:
        sum_digits = sum(abs(digit) for digit in str(abs(num)).split(''))
        if sum_digits > 0:
            count += 1
    return count

# Testing
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(count_nums([-1, 11, -11]))
    print(count_nums([1, 1, 2]))
    print(count_nums([]))
    print(count_nums([-123, 111, 120]))
    print(count_nums([-1234567890, 1111111111, 120]))
    print(count_nums([-12345678901234567890, 11111111111111111111, 120]))