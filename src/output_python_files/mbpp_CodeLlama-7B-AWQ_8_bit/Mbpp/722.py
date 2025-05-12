"""
The input is given as - a dictionary with a student name as a key and a tuple of float (student_height, student_weight) as a value, - minimal height, - minimal weight. Write a function to filter students that have height and weight above the minimum.
assert filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70)=={'Cierra Vega': (6.2, 70)}
"""


def filter_data(students, min_height, min_weight):
    return {k: v for k, v in students.items() if v[0] >= min_height and v[1] >= min_weight}


if __name__ == '__main__':
    students = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
    min_height = 6.0
    min_weight = 70
    print(filter_data(students, min_height, min_weight))


"""
def filter_data(students, min_height, min_weight):
    return {k: v for k, v in students.items() if v[0] >= min_height and v[1] >= min_weight}


if __name__ == '__main__':
    students = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
    min_height = 6.0
    min_weight = 70
    print(filter_data(students, min_height, min_weight))
"""

"""
def filter_data(students, min_height, min_weight):
    return {k: v for k, v in students.items() if v[0] >= min_height and v[1] >= min_weight}


if __name__ == '__main__':
    students = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
    min_height = 6.0
    min_weight = 70
    print(filter_data(students, min_height, min_weight))
"""

"""
def filter_data(students, min_height, min_weight):
    return {k: v for k, v in students.items() if v[0] >= min_height and v[1] >= min_weight}


if __name__ == '__main__':
    students = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
    min_height = 6.0
    min_weight = 70
    print(filter_data(students, min_height, min_weight))
"""

"""
def filter_data(students, min_height, min_weight):
    return {k: v for k, v in students.items() if v[0] >= min_height and v[1] >= min_weight}


if __name__ == '__main__':
    students = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
    min_height = 6.0
    min_weight = 70
    print(filter_data(students, min_height, min_weight))
"""

"""
def filter