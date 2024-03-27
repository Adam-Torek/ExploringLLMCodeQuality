"""
Write a function to sort a dictionary by value.
assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87})==[('Chemistry', 87), ('Physics', 83), ('Math', 81)]
"""
def sort_counter(d):
    return sorted(d.items(), key=lambda item: item[1])

assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87})==[('Chemistry', 87), ('Physics', 83), ('Math', 81)]

# Alternative solution using built-in function
assert sorted(d.items(), key=lambda x: x[1]) == [('Chemistry', 87), ('Physics', 83), ('Math', 81)]</s>