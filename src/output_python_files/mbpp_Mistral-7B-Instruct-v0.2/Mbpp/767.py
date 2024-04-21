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
    numbers = [1, 1, 1, 1]
    sum = 2
    assert get_pairs_count(numbers, sum) == 6
    print("Test passed!")</s>