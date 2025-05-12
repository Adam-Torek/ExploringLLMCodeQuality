"""
Write a function to convert a string to a list of strings split on the space character.
assert string_to_list("python programming")==['python','programming']
"""

def string_to_list(string):
    return string.split()

print(string_to_list("python programming"))
print(string_to_list("hello world"))
print(string_to_list("programming in python"))
print(string_to_list("python is awesome"))

#Output:
#['python', 'programming']
#['hello', 'world']
#['programming', 'in', 'python']
#['python', 'is', 'awesome']