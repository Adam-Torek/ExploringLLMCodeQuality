"""
The input is given as - a dictionary with a student name as a key and a tuple of float (student_height, student_weight) as a value, - minimal height, - minimal weight. Write a function to filter students that have height and weight above the minimum.
assert filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70)=={'Cierra Vega': (6.2, 70)}
"""
def filter_data(students_data, min_height, min_weight):
    """
    :param students_data: dictionary with student names as keys and tuples of height and weight as values
    :param min_height: minimal height
    :param min_weight: minimal weight
    :return: dictionary with student names as keys and tuples of height and weight as values, where height and weight are above the minimum
    """
    result = {}
    for student, student_data in students_data.items():
        if student_data[0] > min_height and student_data[1] > min_weight:
            result[student] = student_data
    return result

# test
students_data = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
min_height = 6.0
min_weight = 70
assert filter_data(students_data, min_height, min_weight) == {'Cierra Vega': (6.2, 70)}

students_data = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
min_height = 6.5
min_weight = 70
assert filter_data(students_data, min_height, min_weight) == {}

students_data = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
min_height = 6.0
min_weight = 65
assert filter_data(students_data, min_height, min_weight) == {'Alden Cantrell': (5.9, 65)}

students_data = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
min_height = 6.0
min_weight = 71
assert filter_data(students_data, min_height, min_weight) == {}