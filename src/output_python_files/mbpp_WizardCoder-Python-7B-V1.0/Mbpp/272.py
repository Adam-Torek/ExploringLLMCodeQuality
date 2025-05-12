"""
Write a function that takes in a list of tuples and returns a list containing the rear element of each tuple.
assert rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]) == [21, 20, 19]
"""

def rear_extract(lst):
    return [t[2] for t in lst]

# Test cases
print(rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)])) # Output: [21, 20, 19]
print(rear_extract([(4, 'Aman', 25), (5, 'Sakshi', 23), (6, 'Kartik', 22)])) # Output: [25, 23, 22]
print(rear_extract([(7, 'Aman', 26), (8, 'Sakshi', 24), (9, 'Kartik', 21)])) # Output: [26, 24, 21]