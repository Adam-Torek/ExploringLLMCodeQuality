"""
Write a python function to count the number of pairs whose sum is equal to ‘sum’. The funtion gets as input a list of numbers and the sum,
assert get_pairs_count([1,1,1,1],2) == 6
"""


def get_pairs_count(nums, sum):
    """
    :param nums: list of numbers
    :param sum: sum of the pairs
    :return: number of pairs
    """
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == sum:
                count += 1
    return count


if __name__ == '__main__':
    print(get_pairs_count([1, 1, 1, 1], 2))
    print(get_pairs_count([1, 1, 1, 1], 3))
    print(get_pairs_count([1, 1, 1, 1], 4))
    print(get_pairs_count([1, 1, 1, 1], 5))
    print(get_pairs_count([1, 1, 1, 1], 6))
    print(get_pairs_count([1, 1, 1, 1], 7))
    print(get_pairs_count([1, 1, 1, 1], 8))
    print(get_pairs_count([1, 1, 1, 1], 9))
    print(get_pairs_count([1, 1, 1, 1], 10))
    print(get_pairs_count([1, 1, 1, 1], 11))
    print(get_pairs_count([1, 1, 1, 1], 12))
    print(get_pairs_count([1, 1, 1, 1], 13))
    print(get_pairs_count([1, 1, 1, 1], 14))
    print(get_pairs_count([1, 1, 1, 1], 15))
    print(get_pairs_count([1, 1, 1, 1], 16))
    print(get_pairs_count([1, 1, 1, 1], 17))
    print(get_pairs_count([1, 1, 1, 1], 18))
    print(get_pairs_count([1, 1, 1, 1], 19))
    print(get_pairs_count([1, 1, 1, 1], 20))
    print(get_pairs_count([1, 1, 1, 1], 21))
    print(get_pairs_count([1, 1, 1, 1], 22))
    print(get_pairs_count([1, 1, 1, 1], 23))
    print(get_pairs_count([1, 1, 1, 1], 24))
    print(get_pairs_count([1, 1, 1, 1], 25))
    print(get_pairs_count([1, 1, 1, 1], 26))
    print(get_pairs_count([1, 1, 1, 1], 27))
    print(get_pairs_count([1, 1, 1, 1], 28))
    print(get_pairs_count([1, 1, 1, 1], 29))
    print(get_pairs_count([1, 1, 1, 1], 30))
    print(get_pairs_count([1, 1, 1, 1], 31))
    print(get_pairs_count([1, 1, 1, 1], 32))
    print(get_pairs_count([1, 1, 1, 1], 33))
    print(get_pairs_count([1,