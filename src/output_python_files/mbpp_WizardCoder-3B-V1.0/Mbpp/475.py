"""
Write a function to sort a dictionary by value.
assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87})==[('Chemistry', 87), ('Physics', 83), ('Math', 81)]
"""

def sort_counter(d):
    sorted_dict = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return sorted_dict<|endoftext|>