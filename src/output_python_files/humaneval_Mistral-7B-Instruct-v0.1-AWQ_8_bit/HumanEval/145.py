def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    def sum_digits(num):
        return sum(int(digit) for digit in str(num))

    nums.sort(key=lambda x: (sum_digits(x), x))
    return nums


if __name__ == '__main__':
    print(order_by_points([1, 11, -1, -11, -12]))