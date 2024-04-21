"""
Write a function to create a list of N empty dictionaries.
assert empty_list(5)==[{},{},{},{},{}]
"""
def empty_list(n):
    return [{} for _ in range(n)]

# Test the function
assert empty_list(5) == [{}, {}, {}, {}, {}]

# Alternative solution using list comprehension
assert empty_list(5) == [dict() for _ in range(5)]</s>