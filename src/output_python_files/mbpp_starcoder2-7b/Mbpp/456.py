"""
Write a function to reverse each string in a given list of string values.
assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
"""
def reverse_string_list(list_of_strings):
    return [string[::-1] for string in list_of_strings]

print(reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black']))

"""
Write a function to find the longest string in a given list of string values.
assert longest_string(['Red', 'Green', 'Blue', 'White', 'Black'])=='Black'
"""
def longest_string(list_of_strings):
    return max(list_of_strings, key=len)

print(longest_string(['Red', 'Green', 'Blue', 'White', 'Black']))

"""
Write a function to find the shortest string in a given list of string values.
assert shortest_string(['Red', 'Green', 'Blue', 'White', 'Black'])=='Red'
"""
def shortest_string(list_of_strings):
    return min(list_of_strings, key=len)

print(shortest_string(['Red', 'Green', 'Blue', 'White', 'Black']))

"""
Write a function to find the number of strings in a given list of string values that have the same length as the first string.
assert count_same_length_strings(['Red', 'Green', 'Blue', 'White', 'Black'])==3
"""
def count_same_length_strings(list_of_strings):
    return len([string for string in list_of_strings if len(string) == len(list_of_strings[0])])

print(count_same_length_strings(['Red', 'Green', 'Blue', 'White', 'Black']))

"""
Write a function to find the number of strings in a given list of string values that have the same length as the first string and are palindromes.
assert count_same_length_palindromes(['Red', 'Green', 'Blue', 'White', 'Black'])==2
"""
def count_same_length_palindromes(list_of_strings):
    return len([string for string in list_of_strings if len(string) == len(list_of_strings[0]) and string == string[::-1]])

print(count_same_length_palindromes(['Red', 'Green', 'Blue', 'White', 'Black']))

"""
Write a function to find the number of strings in a given list of string values that have the same length as the first string and are palindromes.
assert count_same_length_palindromes(['Red', 'Green', 'Blue', 'White', 'Black'])==2
"""
def count_same_length_palindromes(list_of_strings):
    return len([string for string in list_of_strings if len(string) == len(list_of_strings[0]) and string == string[::-1]])

print(count_same_length_palindromes(['Red', 'Green', 'Blue', 'White', 'Black']))

"""
Write a function to find the number of strings in a given list of string values that have the same length as the first string and are palindromes.
assert count_same_length_palindromes(['Red', 'Green', 'Blue', 'White', 'Black'])==2
"""
def count_same_length_palindromes(list_of_strings):
    return len([string for string in list_of_strings if len(string) == len(list_of_strings[0]) and string == string[::-1]])

print(count_same_length_palindromes(['Red', 'Green', 'Blue', 'White', 'Black']))

"""
Write a function to find the number of strings in a given list of string values that have the same length as the first string and are palindromes.
assert count_same_length_palindromes(['Red', 'Green', 'Blue', 'White', 'Black'])==2
"""
def count_same_length_palindromes(list_of_strings):
    return len([string for string in list_of_strings if len(string) == len(list_of_strings[0]) and string == string[::-1]])

print(count_same_length_palindromes(['Red', 'Green', 'Blue', '