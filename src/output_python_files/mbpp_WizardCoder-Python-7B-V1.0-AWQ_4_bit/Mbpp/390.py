"""
Write a function to apply a given format string to all of the elements in a list.
assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']
"""

def add_string(lst, format_str):
    return [format_str.format(x) for x in lst]

# Test the function with the sample input
print(add_string([1,2,3,4],'temp{0}'))

# Test the function with a different input
print(add_string(['apple', 'banana', 'cherry'], 'fruit{0}'))

# Test the function with a different input
print(add_string(['John', 'Sarah', 'Alex'], 'Hello, {0}!'))