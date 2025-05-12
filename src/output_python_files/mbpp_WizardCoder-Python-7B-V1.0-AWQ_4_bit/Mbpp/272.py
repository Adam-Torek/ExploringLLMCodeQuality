"""
Write a function that takes in a list of tuples and returns a list containing the rear element of each tuple.
assert rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]) == [21, 20, 19]
"""

def rear_extract(lst):
    return [t[-1] for t in lst]

# Test cases
print(rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)])) # Output: [21, 20, 19]
print(rear_extract([(4, 'Aman', 25, 'Engineer'), (5, 'Sonam', 22, 'Doctor'), (6, 'Yogi', 23, 'Teacher')]) # Output: [25, 22, 23]