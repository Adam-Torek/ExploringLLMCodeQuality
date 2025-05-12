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
    def digit_sum(num):
        return sum(int(digit) for digit in str(abs(num)))

    nums.sort(key=lambda x: (digit_sum(x), nums.index(x)))
    return nums

# Test cases
print(order_by_points([1, 11, -1, -11, -12]))
print(order_by_points([]))
print(order_by_points([1, 2, 3, 4, 5]))
print(order_by_points([-1, -11, 1, -12, 11]))