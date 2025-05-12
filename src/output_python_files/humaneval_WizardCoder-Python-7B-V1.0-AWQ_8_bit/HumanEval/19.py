from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers_list = numbers.split()
    numbers_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    numbers_list = [numbers_dict[num] for num in numbers_list]
    numbers_list.sort()
    return ' '.join([str(num) for num in numbers_list])

def sort_strings(strings: str) -> str:
    """ Input is a space-delimited string of words.
    Return the string with words sorted alphabetically
    >>> sort_strings('cat dog elephant zebra')
    'cat dog elephant zebra'
    """
    return ' '.join(sorted(strings.split()))

def filter_vowels(words: str) -> str:
    """ Input is a space-delimited string of words.
    Return the string with vowels removed
    >>> filter_vowels('hello world')
    'hll wrld'
    """
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return ''.join([char for char in words if char not in vowels])

def reverse_string(string: str) -> str:
    """ Input is a string.
    Return the string with characters reversed
    >>> reverse_string('hello world')
    'dlrow olleh'
    """
    return string[::-1]

def remove_duplicates(string: str) -> str:
    """ Input is a string.
    Return the string with duplicates removed
    >>> remove_duplicates('hello world')
    'dlrw'
    """
    return ''.join(sorted(set(string), key=string.index)

def find_missing_number(numbers: List[int]) -> int:
    """ Input is a list of integers.
    Return the missing number in the range of 0 to len(numbers) + 1
    >>> find_missing_number([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    0
    """
    for num in range(len(numbers) + 1):
        if num not in numbers:
            return num

def find_longest_substring(string: str) -> str:
    """ Input is a string.
    Return the longest substring with no repeating characters
    >>> find_longest_substring('abcabcbb')
    'abc'
    """
    max_substring = ''
    current_substring = ''
    for char in string:
        if char not in current_substring:
            current_substring += char
        else:
            if len(current_substring) > len(max_substring):
                max_substring = current_substring
            current_substring = current_substring[current_substring.index(char) + 1:] + char
    if len(current_substring) > len(max_substring):
        max_substring = current_substring
    return max_substring

if __name__ == "__main__":
    import doctest
    doctest.testmod()