"""
Write a python function to count the number of pairs whose sum is equal to ‘sum’. The funtion gets as input a list of numbers and the sum,
assert get_pairs_count([1,1,1,1],2) == 6
"""
def get_pairs_count(numbers, sum):
    """
    :param numbers: list of numbers
    :param sum: sum of pairs
    :return: number of pairs whose sum is equal to sum
    """
    count = 0
    numbers_dict = {}
    for number in numbers:
        complement = sum - number
        if complement in numbers_dict:
            count += 1
        numbers_dict[number] = True
    return count

if __name__ == "__main__":
    assert get_pairs_count([1,1,1,1], 2) == 6
    assert get_pairs_count([1,2,3,4], 5) == 2
    assert get_pairs_count([], 1) == 0
    assert get_pairs_count([1], 1) == 1
    assert get_pairs_count([1,1], 2) == 1
    assert get_pairs_count([1,1,1,1,1], 3) == 4
    assert get_pairs_count([1,1,1,1,1,1], 4) == 6
    assert get_pairs_count([1,1,1,1,1,1,1], 5) == 6
    assert get_pairs_count([1,1,1,1,1,1,1], 6) == 4
    assert get_pairs_count([1,1,1,1,1,1,1], 7) == 3
    assert get_pairs_count([1,1,1,1,1,1,1], 8) == 3
    assert get_pairs_count([1,1,1,1,1,1,1], 9) == 2
    assert get_pairs_count([1,1,1,1,1,1,1], 10) == 2
    assert get_pairs_count([1,1,1,1,1,1,1], 11) == 1
    assert get_pairs_count([1,1,1,1,1,1,1], 12) == 1
    assert get_pairs_count([1,1,1,1,1,1,1], 13) == 0
    assert get_pairs_count([1,1,1,1,1,1,1], 14) == 0
    assert get_pairs_count([1,1,1,1,1,1,1], 15) == 0
    assert get_pairs_count([1,1,1,1,1,1,1], 16) == 0
    assert get_pairs_count([1,1,1,1,1,1,1], 17) == 0
    assert get_pairs_count([1,1,1,1,1,1,1], 18) == 0
    assert get_pairs_count([1,1,1,1,1,1,1], 19) == 0
    assert get_pairs_count([1,1,1,1,1,1,1], 20) == 0
    assert get_pairs_count([1,1,1,1,1,1,1], 21) == 0
    assert get_pairs_count([1,1,1,1,1,1,1], 22) == 0
    assert get_pairs_count([1,1,1,1,1,1,1], 23) == 0
    assert get_pairs_count([1,1,1,1,1,1,1], 24) == 0
    assert get_pairs_count([1,1,1,1,1,1,1], 25) == 0
    assert get_pairs_count([1,1,