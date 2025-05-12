"""
Write a function to find the list of maximum length in a list of lists.
assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])
"""

def max_length(lst):
    max_len = 0
    max_list = []
    for i in lst:
        if len(i) > max_len:
            max_len = len(i)
            max_list = i
    return max_len, max_list

print(max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]))
/python_basics/02_data_types/02_01_numbers.py
"""
Numbers
"""

# Integer
print(1)
print(1000)
print(-1000)

# Float
print(1.0)
print(1.1)
print(-1.1)

# Complex
print(1j)
print(1 + 1j)
print(1j * 1j)

# Boolean
print(True)
print(False)

# None
print(None)
/python_basics/02_data_types/02_02_strings.py
"""
Strings
"""

# String
print("Hello World")
print('Hello World')
print("""Hello World""")
print('''Hello World''')

# String concatenation
print("Hello" + " World")

# String repetition
print("Hello" * 3)

# String indexing
print("Hello"[0])
print("Hello"[1])
print("Hello"[2])
print("Hello"[3])
print("Hello"[4])

# String slicing
print("Hello"[0:2])
print("Hello"[0:3])
print("Hello"[0:4])
print("Hello"[0:5])
print("Hello"[0:6])

# String slicing with step
print("Hello"[0:5:2])
print("Hello"[0:5:3])
print("Hello"[0:5:4])
print("Hello"[0:5:5])
print("Hello"[0:5:6])

# String slicing with negative step
print("Hello"[-1:-6:-1])
print("Hello"[-1:-6:-2])
print("Hello"[-1:-6:-3])
print("Hello"[-1:-6:-4])
print("Hello"[-1:-6:-5])
print("Hello"[-1:-6:-6])

# String slicing with negative step
print("Hello"[-1:-6:-1])
print("Hello"[-1:-6:-2])
print("Hello"[-1:-6:-3])
print("Hello"[-1:-6:-4])
print("Hello"[-1:-6:-5])
print("Hello"[-1:-6:-6])

# String slicing with negative step
print("Hello"[-1:-6:-1])
print("Hello"[-1:-6:-2])
print("Hello"[-1:-6:-3])
print("Hello"[-1:-6:-4])
print("Hello"[-1:-6:-5])
print("Hello"[-1:-6:-6])

# String slicing with negative step
print("Hello"[-1:-6:-1])
print("Hello"[-1:-6:-2])
print("Hello"[-1:-6:-3])
print("Hello"[-1:-6:-4])
print("Hello"[-1:-6:-5])
print("Hello"[-1:-6:-6])

# String slicing with negative step
print("Hello"[-1:-6:-1])
print("Hello"[-1:-6:-2])
print("Hello"[-1:-6:-3])
print("Hello"[-1:-6:-4])
print("Hello"[-1:-6:-5])
print("Hello"[-1:-6:-6])

# String slicing with negative step
print("Hello"[-1:-6:-1])
print("Hello"[-1:-6:-2])
print("Hello"[-1:-6:-3])
print("Hello"[-1:-6:-4])
print("Hello"[-1:-6:-5