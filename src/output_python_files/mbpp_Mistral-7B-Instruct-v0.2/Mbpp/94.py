"""
Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
"""
def index_minimum(lst):
    """
    :param lst: list of tuples
    :return: string, the first value of the tuple with the smallest second value
    """
    return next((i[0] for i in lst), None)[0] if lst else None

assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
assert index_minimum([]) is None
assert index_minimum([('Rash', 143), ('Manjeet', 200)]) is None
assert index_minimum([('Rash', 143)]) == 'Rash'</s>