"""
Write a function to count the total number of characters in a string.
assert count_charac("python programming")==18
"""
def count_charac(string):
    count = 0
    for char in string:
        count += 1
    return count

# Test the function
assert count_charac("python programming")==18<|endoftext|>