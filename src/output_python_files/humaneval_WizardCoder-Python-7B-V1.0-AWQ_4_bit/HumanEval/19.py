from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    num_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    num_list = numbers.split()
    num_list = [num_dict[num] for num in num_list]
    num_list.sort()
    return ' '.join([str(num) for num in num_list])

def sort_strings(strings: str) -> str:
    """ Input is a space-delimited string of words.
    Return the string with words sorted alphabetically
    >>> sort_strings('cat dog elephant zebra')
    'cat dog elephant zebra'
    """
    return ' '.join(sorted(strings.split()))

def find_missing_numbers(numbers: List[int]) -> List[int]:
    """ Input is a list of integers.
    Return a list of missing numbers in ascending order.
    If there are no missing numbers, return an empty list.
    If the list is empty, return an empty list.
    If the list has only one element, return an empty list.
    If the list has two elements, return a list with the second element minus the first element.
    If the list has three or more elements, return a list with the difference between the second and third elements,
    and the difference between the third and fourth elements, and so on.
    >>> find_missing_numbers([1, 2, 3, 5, 6, 7, 8, 9])
    [4]
    >>> find_missing_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])
    [3]
    >>> find_missing_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [3, 4]
    """
    if len(numbers) < 2:
        return []
    diffs = [numbers[i+1] - numbers[i] for i in range(len(numbers)-1)]
    missing_numbers = []
    for i in range(1, len(diffs)):
        if diffs[i] != diffs[i-1]:
            missing_numbers.append(numbers[i-1] + diffs[i-1])
    return missing_numbers

if __name__ == "__main__":
    import doctest
    doctest.testmod()