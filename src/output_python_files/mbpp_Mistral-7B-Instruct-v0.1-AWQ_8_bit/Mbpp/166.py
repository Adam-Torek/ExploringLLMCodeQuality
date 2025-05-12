"""
Write a function that counts the number of pairs of integers in a list that xor to an even number.
assert find_even_pair([5, 4, 7, 2, 1]) == 4
"""

def find_even_pair(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] ^ lst[j] == 0:
                count += 1
    return count

assert find_even_pair([5, 4, 7, 2, 1]) == 4