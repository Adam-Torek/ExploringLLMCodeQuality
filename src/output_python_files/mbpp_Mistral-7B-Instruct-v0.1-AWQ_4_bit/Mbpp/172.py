"""
Write a function to count the number of occurence of the string 'std' in a given string.
assert count_occurance("letstdlenstdporstd") == 3
"""

def count_occurance(string):
    count = 0
    for i in range(len(string)):
        if string[i] == 'std':
            count += 1
    return count

# test
assert count_occurance("letstdlenstdporstd") == 3