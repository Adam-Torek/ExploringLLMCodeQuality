"""
Write a function to sort a dictionary by value.
assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87})==[('Chemistry', 87), ('Physics', 83), ('Math', 81)]
"""

def sort_counter(dictionary):
    """
    This function takes a dictionary as an input and returns a new dictionary
    sorted by the value of the key-value pairs.
    """
    # Create a list of tuples from the dictionary
    sorted_list = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)

    # Create a new dictionary from the sorted list
    new_dictionary = dict(sorted_list)

    # Return the new dictionary
    return new_dictionary

# Test the function
assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87})==[('Chemistry', 87), ('Physics', 83), ('Math', 81)]