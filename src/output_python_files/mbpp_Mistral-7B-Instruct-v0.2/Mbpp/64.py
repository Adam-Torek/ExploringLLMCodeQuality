"""
Write a function to sort a list of tuples using the second value of each tuple.
assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])==[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
"""
def subject_marks(lst):
    """
    This function takes a list of tuples as an argument and sorts it based on the second value of each tuple.

    :param lst: list of tuples
    :return: sorted list of tuples
    """
    return sorted(lst, key=lambda x: x[1])

# Test the function
assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])==[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
print("Test passed!")</s>