"""
Write a python function to find the sum of even numbers at even positions of a list.
assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30
"""

def sum_even_and_even_index(lst):
    even_sum = 0
    even_index_sum = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            even_sum += lst[i]
            if i % 2 == 0:
                even_index_sum += lst[i]
    return even_sum + even_index_sum

# Test the function
assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30<|endoftext|>