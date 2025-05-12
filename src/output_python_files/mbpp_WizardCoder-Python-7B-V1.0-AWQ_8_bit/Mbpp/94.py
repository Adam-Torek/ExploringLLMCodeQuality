"""
Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
"""

def index_minimum(lst):
    return min(lst, key=lambda x: x[1])[0]

print(index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)])) # Output: Varsha
print(index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100), ('Ayush', 100)])) # Output: Rash
print(index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100), ('Ayush', 100), ('Ayush', 100)])) # Output: Rash