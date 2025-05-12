"""
Write function to find the sum of all items in the given dictionary.
assert return_sum({'a': 100, 'b':200, 'c':300}) == 600
"""
def return_sum(dictionary):
    total = 0
    for key in dictionary:
        total += dictionary[key]
    return total

# assert return_sum({'a': 100, 'b':200, 'c':300}) == 600
print(return_sum({'a': 100, 'b':200, 'c':300}))