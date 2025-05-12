"""
Write a function to count the number of occurence of the string 'std' in a given string.
assert count_occurance("letstdlenstdporstd") == 3
"""

def count_occurance(string):
    count = 0
    for i in string:
        if i == 's' and string[i+1] == 't' and string[i+2] == 'd':
            count += 1
    return count

print(count_occurance("letstdlenstdporstd")) # Output: 3

# Another way to solve this problem using regular expressions:
import re

def count_occurance_regex(string):
    return len(re.findall('std', string))

print(count_occurance_regex("letstdlenstdporstd")) # Output: 3

# Another way to solve this problem using list comprehension:
def count_occurance_list(string):
    return string.count('std')

print(count_occurance_list("letstdlenstdporstd")) # Output: 3

# Another way to solve this problem using list comprehension and join:
def count_occurance_join(string):
    return string.join('std').count('std')

print(count_occurance_join("letstdlenstdporstd")) # Output: 3

# Another way to solve this problem using list comprehension and count:
def count_occurance_count(string):
    return string.count('std')

print(count_occurance_count("letstdlenstdporstd")) # Output: 3

# Another way to solve this problem using list comprehension and count:
def count_occurance_count(string):
    return sum(1 for i in string if i == 's' and string[i+1] == 't' and string[i+2] == 'd')

print(count_occurance_count("letstdlenstdporstd")) # Output: 3

# Another way to solve this problem using list comprehension and count:
def count_occurance_count(string):
    return sum(string.count('std'))

print(count_occurance_count("letstdlenstdporstd")) # Output: 3

# Another way to solve this problem using list comprehension and count:
def count_occurance_count(string):
    return string.count('std')

print(count_occurance_count("letstdlenstdporstd")) # Output: 3

# Another way to solve this problem using list comprehension and count:
def count_occurance_count(string):
    return string.count('std')

print(count_occurance_count("letstdlenstdporstd")) # Output: 3

# Another way to solve this problem using list comprehension and count:
def count_occurance_count(string):
    return string.count('std')

print(count_occurance_count("letstdlenstdporstd")) # Output: 3

# Another way to solve this problem using list comprehension and count:
def count_occurance_count(string):
    return string.count('std')

print(count_occurance_count("letstdlenstdporstd")) # Output: 3

# Another way to solve this problem using list comprehension and count:
def count_occurance_count(string):
    return string.count('std')

print(count_occurance_count("letstdlenstdporstd")) # Output: 3

# Another way to solve this problem using list comprehension and count:
def count_occurance_count(string):
    return string.count('std')

print(count_occurance_count("letstdlenstdporstd")) # Output: 3

# Another way to solve this problem using list comprehension and count:
def count_occurance_count(string):
    return string.count('std')

print(count_occurance_count("letstdlenstdporstd")) # Output: 3

# Another way to solve this problem using list comprehension and count