"""
Write a function that takes in positive integers m and n and finds the number of possible sequences of length n, such that each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m.
assert get_total_number_of_sequences(10, 4) == 4
"""

def get_total_number_of_sequences(m, n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return get_total_number_of_sequences(m, n-1) + get_total_number_of_sequences(m, n-2)

print(get_total_number_of_sequences(10, 4))
/recursion/get_permutations.py
"""
Write a function that takes in a string of unique characters and returns a list of all permutations of those characters.
assert get_permutations("a") == ["a"]
assert get_permutations("ab") == ["ab", "ba"]
assert get_permutations("abc") == ["abc", "acb", "bac", "bca", "cab", "cba"]
"""

def get_permutations(string):
    if len(string) == 1:
        return [string]
    else:
        permutations = []
        for i in range(len(string)):
            first_char = string[i]
            remaining_chars = string[:i] + string[i+1:]
            for permutation in get_permutations(remaining_chars):
                permutations.append(first_char + permutation)
        return permutations

print(get_permutations("abc"))
/recursion/get_powerset.py
"""
Write a function that takes in a set of unique integers and returns its powerset.
assert get_powerset([1, 2]) == [[], [1], [2], [1, 2]]
assert get_powerset([1, 2, 3]) == [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
"""

def get_powerset(array):
    if len(array) == 0:
        return [[]]
    else:
        powerset = []
        for i in range(len(array)):
            first_element = array[i]
            remaining_elements = array[:i] + array[i+1:]
            for subset in get_powerset(remaining_elements):
                powerset.append([first_element] + subset)
        return powerset

print(get_powerset([1, 2, 3]))
/recursion/get_subsets.py
"""
Write a function that takes in a set of unique integers and returns its powerset.
assert get_subsets([1, 2]) == [[], [1], [2], [1, 2]]
assert get_subsets([1, 2, 3]) == [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
"""

def get_subsets(array):
    if len(array) == 0:
        return [[]]
    else:
        subsets = []
        for i in range(len(array)):
            first_element = array[i]
            remaining_elements = array[:i] + array[i+1:]
            for subset in get_subsets(remaining_elements):
                subsets.append([first_element] + subset)
        return subsets

print(get_subsets([1, 2, 3]))
/recursion/get_all_subsets.py
"""
Write a function that takes in a set of unique integers and returns its powerset.
assert get_all_subsets([1, 2]) == [[], [1], [2], [1, 2]]
assert get_all_subsets([1, 2, 3]) == [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
"""

def get_all_subsets(array):
    if len(array) == 0:
        return [[]]
    else:
        subsets = []
        for i in range(len(array)):