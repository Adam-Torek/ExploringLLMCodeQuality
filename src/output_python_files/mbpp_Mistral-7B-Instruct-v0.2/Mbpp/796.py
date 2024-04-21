"""
Write function to find the sum of all items in the given dictionary.
assert return_sum({'a': 100, 'b':200, 'c':300}) == 600
"""
def return_sum(dictionary):
    total = 0
    for key, value in dictionary.items():
        total += value
    return total

assert return_sum({'a': 100, 'b':200, 'c':300}) == 600</s>