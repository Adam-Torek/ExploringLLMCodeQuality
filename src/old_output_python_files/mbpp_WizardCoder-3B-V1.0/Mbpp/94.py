"""
Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
"""

def index_minimum(lst):
    min_index = 0
    for i in range(1, len(lst)):
        if lst[i][1] < lst[min_index][1]:
            min_index = i
    return lst[min_index][0]

# Test the function
print(index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)])) # Output: Varsha<|endoftext|>