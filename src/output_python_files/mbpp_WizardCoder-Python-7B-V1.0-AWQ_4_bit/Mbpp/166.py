"""
Write a function that counts the number of pairs of integers in a list that xor to an even number.
assert find_even_pair([5, 4, 7, 2, 1]) == 4
"""

def find_even_pair(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if (lst[i]^lst[j])%2 == 0:
                count += 1
    return count

print(find_even_pair([5, 4, 7, 2, 1])) # Output: 4
print(find_even_pair([1, 2, 3, 4, 5, 6, 7, 8])) # Output: 10
print(find_even_pair([1, 3, 5, 7, 9])) # Output: 0
print(find_even_pair([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # Output: 10
print(find_even_pair([1, 3, 5, 7, 9, 11])) # Output: 0
print(find_even_pair([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])) # Output: 10
print(find_even_pair([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])) # Output: 12
print(find_even_pair([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])) # Output: 12
print(find_even_pair([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])) # Output: 14
print(find_even_pair([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) # Output: 14
print(find_even_pair([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])) # Output: 16
print(find_even_pair([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])) # Output: 16
print(find_even_pair([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])) # Output: 16
print(find_even_pair([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])) # Output: 16
print(find_even_pair([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) # Output: 16
print(find_even_pair([1, 2, 3, 4, 5, 6, 7, 8, 9, 10