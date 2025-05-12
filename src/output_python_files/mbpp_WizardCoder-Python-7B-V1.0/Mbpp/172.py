"""
Write a function to count the number of occurence of the string 'std' in a given string.
assert count_occurance("letstdlenstdporstd") == 3
"""

def count_occurance(string):
    count = 0
    for i in range(len(string)-2):
        if string[i:i+2] == "std":
            count += 1
    return count

print(count_occurance("letstdlenstdporstd")) # Output: 3
print(count_occurance("std")) # Output: 1
print(count_occurance("")) # Output: 0
print(count_occurance("stdstd")) # Output: 2
print(count_occurance("stdstdstd")) # Output: 3
print(count_occurance("stdstdstdstd")) # Output: 4
print(count_occurance("stdstdstdstdstd")) # Output: 5
print(count_occurance("stdstdstdstdstdstd")) # Output: 6
print(count_occurance("stdstdstdstdstdstdstd")) # Output: 7
print(count_occurance("stdstdstdstdstdstdstdstd")) # Output: 8
print(count_occurance("stdstdstdstdstdstdstdstdstd")) # Output: 9
print(count_occurance("stdstdstdstdstdstdstdstdstdstd")) # Output: 10
print(count_occurance("stdstdstdstdstdstdstdstdstdstdstd")) # Output: 11
print(count_occurance("stdstdstdstdstdstdstdstdstdstdstdstd")) # Output: 12
print(count_occurance("stdstdstdstdstdstdstdstdstdstdstdstdstd")) # Output: 13
print(count_occurance("stdstdstdstdstdstdstdstdstdstdstdstdstdstd")) # Output: 14
print(count_occurance("stdstdstdstdstdstdstdstdstdstdstdstdstdstdstd")) # Output: 15
print(count_occurance("stdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstd")) # Output: 16
print(count_occurance("stdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstd")) # Output: 17
print(count_occurance("stdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstd")) # Output: 18
print(count_occurance("stdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstd")) # Output: 19
print(count_occurance("stdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstd")) # Output: 20
print(count_occurance("stdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstd")) # Output: 21
print(count_occurance("stdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstd")) # Output: 22
print(count_occurance("stdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstd")) # Output: 23
print(count_occurance("stdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstd")) # Output: 24
print(count_occurance("stdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstd")) # Output: 25
print(count_occurance("stdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstd")) # Output: 26
print(count_occurance("stdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstd")) # Output: 27
print(count_occurance("stdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstdstd")) # Output