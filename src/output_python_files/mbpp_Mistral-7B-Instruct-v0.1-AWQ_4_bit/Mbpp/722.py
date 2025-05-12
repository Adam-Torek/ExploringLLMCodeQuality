"""
The input is given as - a dictionary with a student name as a key and a tuple of float (student_height, student_weight) as a value, - minimal height, - minimal weight. Write a function to filter students that have height and weight above the minimum.
assert filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70)=={'Cierra Vega': (6.2, 70)}
"""

def filter_data(data:dict,min_height:float,min_weight:float) -> dict:
    """
    This function filters students that have height and weight above the minimum.
    :param data: dictionary with a student name as a key and a tuple of float (student_height, student_weight) as a value, - minimal height, - minimal weight.
    :param min_height: minimal height
    :param min_weight: minimal weight
    :return: dictionary with a student name as a key and a tuple of float (student_height, student_weight) as a value, - minimal height, - minimal weight.
    """
    filtered_data = {}
    for name, (height, weight) in data.items():
        if height > min_height and weight > min_weight:
            filtered_data[name] = (height, weight)
    return filtered_data