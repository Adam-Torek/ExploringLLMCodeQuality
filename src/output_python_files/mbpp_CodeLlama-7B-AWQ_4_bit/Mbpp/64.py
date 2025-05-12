"""
Write a function to sort a list of tuples using the second value of each tuple.
assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])==[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
"""


def subject_marks(marks):
    """
    >>> subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])
    [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
    """
    return sorted(marks, key=lambda x: x[1])


if __name__ == "__main__":
    import doctest

    doctest.testmod()