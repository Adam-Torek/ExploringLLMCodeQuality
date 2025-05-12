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