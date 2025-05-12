"""
Write a function to sort a dictionary by value.
assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87})==[('Chemistry', 87), ('Physics', 83), ('Math', 81)]
"""

def sort_counter(counter):
    return sorted(counter.items(), key=lambda x: x[1], reverse=True)

# Test
assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87})==[('Chemistry', 87), ('Physics', 83), ('Math', 81)]
print("Test passed!")