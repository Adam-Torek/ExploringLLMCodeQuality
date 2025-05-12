"""
Write a function to count the number of occurence of the string'std' in a given string.
assert count_occurance("letstdlenstdporstd") == 3
"""

def count_occurance(string):
    count = 0
    for i in range(len(string)):
        if string[i:i+3] == "std":
            count += 1
    return count

print(count_occurance("letstdlenstdporstd"))
/python_basics/list_comprehension.py
"""
List comprehension is a way to create a list in a single line of code.
"""

# Example 1

# Without list comprehension

# list1 = []
# for i in range(10):
#     list1.append(i)

# print(list1)

# With list comprehension

# list2 = [i for i in range(10)]
# print(list2)

# Example 2

# Without list comprehension

# list1 = []
# for i in range(10):
#     if i % 2 == 0:
#         list1.append(i)

# print(list1)

# With list comprehension

# list2 = [i for i in range(10) if i % 2 == 0]
# print(list2)

# Example 3

# Without list comprehension

# list1 = []
# for i in range(10):
#     if i % 2 == 0:
#         list1.append(i)
#     else:
#         list1.append(i*2)

# print(list1)

# With list comprehension

# list2 = [i if i % 2 == 0 else i*2 for i in range(10)]
# print(list2)

# Example 4

# Without list comprehension

# list1 = []
# for i in range(10):
#     if i % 2 == 0:
#         list1.append(i)
#     else:
#         list1.append(i*2)
#     if i % 3 == 0:
#         list1.append(i*3)

# print(list1)

# With list comprehension

# list2 = [i if i % 2 == 0 else i*2 if i % 3 == 0 else i*3 for i in range(10)]
# print(list2)

# Example 5

# Without list comprehension

# list1 = []
# for i in range(10):
#     if i % 2 == 0:
#         list1.append(i)
#     else:
#         list1.append(i*2)
#     if i % 3 == 0:
#         list1.append(i*3)
#     if i % 5 == 0:
#         list1.append(i*5)

# print(list1)

# With list comprehension

# list2 = [i if i % 2 == 0 else i*2 if i % 3 == 0 else i*3 if i % 5 == 0 else i*5 for i in range(10)]
# print(list2)

# Example 6

# Without list comprehension

# list1 = []
# for i in range(10):
#     if i % 2 == 0:
#         list1.append(i)
#     else:
#         list1.append(i*2)
#     if i % 3 == 0:
#         list1.append(i*3)
#     if i % 5 == 0:
#         list1.append(i*5)
#     if i % 7 == 0:
#         list1.append(i*7)

# print(list1)

# With list comprehension

# list2 = [i if i % 2 == 0 else i*2 if i % 3 == 0 else i*3 if i % 5 == 0 else i*5 if i % 7 == 0 else i*7 for i in range(10)]
# print(list2)

# Example 7

# Without