"""
Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
"""

def index_minimum(tuples):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
    """
    return min(tuples, key=lambda x: x[1])[0]


# assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
print(index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]))