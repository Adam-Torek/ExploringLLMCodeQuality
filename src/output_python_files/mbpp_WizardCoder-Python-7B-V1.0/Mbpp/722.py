"""
The input is given as - a dictionary with a student name as a key and a tuple of float (student_height, student_weight) as a value, - minimal height, - minimal weight. Write a function to filter students that have height and weight above the minimum.
assert filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70)=={'Cierra Vega': (6.2, 70)}
"""

def filter_data(data, min_height, min_weight):
    return {k:v for k,v in data.items() if v[0]>min_height and v[1]>min_weight}

# Test the function with the given example
print(filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70))

# Test the function with some additional inputs
print(filter_data({'John Doe': (6.5, 75), 'Jane Doe': (5.8, 60), 'Bob Smith': (6.1, 70), 'Alice Johnson': (6.3, 65)},6.0,60))
print(filter_data({'John Doe': (6.5, 75), 'Jane Doe': (5.8, 60), 'Bob Smith': (6.1, 70), 'Alice Johnson': (6.3, 65)},6.2,65))
print(filter_data({'John Doe': (6.5, 75), 'Jane Doe': (5.8, 60), 'Bob Smith': (6.1, 70), 'Alice Johnson': (6.3, 65)},6.5,65))
print(filter_data({'John Doe': (6.5, 75), 'Jane Doe': (5.8, 60), 'Bob Smith': (6.1, 70), 'Alice Johnson': (6.3, 65)},6.5,60))
print(filter_data({'John Doe': (6.5, 75), 'Jane Doe': (5.8, 60), 'Bob Smith': (6.1, 70), 'Alice Johnson': (6.3, 65)},6.2,62))

# Test the function with an empty dictionary
print(filter_data({},6.0,70))

# Test the function with a dictionary with only one student
print(filter_data({'John Doe': (6.5, 75)},6.0,70))

# Test the function with a dictionary with no students
print(filter_data({},6.0,70))

# Test the function with a dictionary with no students that meet the criteria
print(filter_data({'John Doe': (5.8, 60), 'Jane Doe': (5.9, 60), 'Bob Smith': (5.7, 65), 'Alice Johnson': (5.6, 65)},6.2,65)