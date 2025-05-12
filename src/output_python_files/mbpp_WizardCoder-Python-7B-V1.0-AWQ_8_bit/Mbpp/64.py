"""
Write a function to sort a list of tuples using the second value of each tuple.
assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])==[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
"""

def subject_marks(marks):
    return sorted(marks, key=lambda x: x[1])

print(subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]))
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

# or

def subject_marks(marks):
    return sorted(marks, key=lambda x: x[1], reverse=True)

print(subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]))
# [('Maths', 97), ('Science', 90), ('English', 88), ('Social sciences', 82)]

# or

def subject_marks(marks):
    return sorted(marks, key=lambda x: x[1], reverse=True)

print(subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])[::-1]
# [('Maths', 97), ('Science', 90), ('English', 88), ('Social sciences', 82)]

# or

def subject_marks(marks):
    return sorted(marks, key=lambda x: x[1], reverse=True)

print(list(reversed(subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]))
# [('Maths', 97), ('Science', 90), ('English', 88), ('Social sciences', 82)]

# or

def subject_marks(marks):
    return sorted(marks, key=lambda x: x[1], reverse=True)

print(list(reversed(subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]))[::-1]
# [('Maths', 97), ('Science', 90), ('English', 88), ('Social sciences', 82)]

# or
def subject_marks(marks):
    return sorted(marks, key=lambda x: x[1], reverse=True)

print(list(reversed(sorted(marks, key=lambda x: x[1])))
# [('Maths', 97), ('Science', 90), ('English', 88), ('Social sciences', 82)]

# or
def subject_marks(marks):
    return sorted(marks, key=lambda x: x[1], reverse=True)

print(list(reversed(sorted(marks, key=lambda x: x[1])))
# [('Maths', 97), ('Science', 90), ('English', 88), ('Social sciences', 82)]

# or
def subject_marks(marks):
    return sorted(marks, key=lambda x: x[1], reverse=True)

print(sorted(marks, key=lambda x: x[1], reverse=True)
# [('Maths', 97), ('Science', 90), ('English', 88), ('Social sciences', 82)]

# or
def subject_marks(marks):
    return sorted(marks, key=lambda x: x[1], reverse=True)

print(sorted(marks, key=lambda x: x[1], reverse=True)
# [('Maths', 97), ('Science', 90), ('English', 88), ('Social sciences', 82)]

# or
def subject_marks(