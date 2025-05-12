"""
Write a function to find tuples which have all elements divisible by k from the given list of tuples.
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]
"""

def find_tuples(list_of_tuples, k):
    return [tuple for tuple in list_of_tuples if all(element % k == 0 for element in tuple)]

print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6))/Python/Python_Basics/03_Strings/02_String_Slicing.py
"""
String Slicing
"""

# Slicing a string

string = "Hello World"

print(string[0])
print(string[1])
print(string[2])
print(string[3])
print(string[4])
print(string[5])
print(string[6])
print(string[7])
print(string[8])
print(string[9])
print(string[10])
print(string[11])

# Slicing a string with a range

print(string[0:5])
print(string[6:11])
print(string[11:12])

# Slicing a string with a step

print(string[0:12:2])
print(string[0:12:3])

# Slicing a string with a negative step

print(string[::-1])
print(string[::-2])

# Slicing a string with a negative step and a range

print(string[::-1][0:5])
print(string[::-1][6:11])
print(string[::-1][11:12])

# Slicing a string with a negative step and a range with a step

print(string[::-1][0:12:2])
print(string[::-1][0:12:3])

# Slicing a string with a negative step and a range with a negative step

print(string[::-1][::-1])
print(string[::-1][::-2])

# Slicing a string with a negative step and a range with a negative step and a step

print(string[::-1][::-1][0:5])
print(string[::-1][::-1][6:11])
print(string[::-1][::-1][11:12])

print(string[::-1][::-1][0:12:2])
print(string[::-1][::-1][0:12:3])

# Slicing a string with a negative step and a range with a negative step and a negative step

print(string[::-1][::-1][::-1])
print(string[::-1][::-1][::-2])

# Slicing a string with a negative step and a range with a negative step and a negative step and a step

print(string[::-1][::-1][::-1][0:5])
print(string[::-1][::-1][::-1][6:11])
print(string[::-1][::-1][::-1][11:12])

print(string[::-1][::-1][::-1][0:12:2])
print(string[::-1][::-1][::-1][0:12:3])

# Slicing a string with a negative step and a range with a negative step and a negative step and a negative step

print(string[::-1][::-1][::-1][::-1])
print(string[::-1][::-1][::-1][::-2])

# Slicing a string with a negative step and a range with a negative step and a negative step and a negative step and a step

print(string[::-1][::-1][::-1][::-1][0:5])
print(string[::-1][::-1][::-1][::-1][6:11])
print(string[::-1][::-1][::-1][::-1][11:12])

print(string[::-1][::-1][::-1][::-1][0:12:2])
print(string[::-1][::-1][::-1][::-1][0: