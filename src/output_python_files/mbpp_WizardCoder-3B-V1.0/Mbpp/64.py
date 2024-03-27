"""
Write a function to sort a list of tuples using the second value of each tuple.
assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])==[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
"""

def subject_marks(marks_list):
    return sorted(marks_list, key=lambda x: x[1])

print(subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]))<|endoftext|>