"""
Write a python function to find the sum of even numbers at even positions of a list.
assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30
"""
def sum_even_and_even_index(lst):
    even_sum = 0
    for i in range(0, len(lst), 2):
        if lst[i] % 2 == 0:
            even_sum += lst[i]
    return even_sum

print(sum_even_and_even_index([5, 6, 12, 1, 18, 8])) # Output: 30
print(sum_even_and_even_index([1, 2, 3, 4, 5, 6])) # Output: 6
print(sum_even_and_even_index([10, 2, 3, 4, 5, 6])) # Output: 10
print(sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8])) # Output: 10
print(sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9])) # Output: 12
print(sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # Output: 14
print(sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])) # Output: 14
print(sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])) # Output: 16
print(sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])) # Output: 16
print(sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])) # Output: 18
print(sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) # Output: 18
print(sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])) # Output: 20
print(sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])) # Output: 22
print(sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])) # Output: 24
print(sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])) # Output: 26
print(sum_even_and_even_index([1, 2, 3, 4, 5, 6