"""
Write function to find the sum of all items in the given dictionary.
assert return_sum({'a': 100, 'b':200, 'c':300}) == 600
"""

def return_sum(dictionary):
    total = 0
    for value in dictionary.values():
        total += value
    return total

# Test the function
assert return_sum({'a': 100, 'b':200, 'c':300}) == 600<|endoftext|>