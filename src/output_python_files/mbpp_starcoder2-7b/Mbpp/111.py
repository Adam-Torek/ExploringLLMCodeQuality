"""
Write a function to find the common elements in given nested lists.
assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
"""

def common_in_nested_lists(nested_lists):
    common_list = []
    for i in nested_lists:
        for j in i:
            if j in common_list:
                continue
            else:
                common_list.append(j)
    return common_list

print(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))
<file_sep>/python_basics/list_comprehension.py
"""
List comprehension is a way to create a list in a single line.
"""

# Example 1

# Without list comprehension

list_1 = []
for i in range(1, 11):
    list_1.append(i)
print(list_1)

# With list comprehension

list_2 = [i for i in range(1, 11)]
print(list_2)

# Example 2

# Without list comprehension

list_3 = []
for i in range(1, 11):
    if i % 2 == 0:
        list_3.append(i)
print(list_3)

# With list comprehension

list_4 = [i for i in range(1, 11) if i % 2 == 0]
print(list_4)

# Example 3

# Without list comprehension

list_5 = []
for i in range(1, 11):
    if i % 2 == 0:
        list_5.append(i)
    else:
        list_5.append(i * 2)
print(list_5)

# With list comprehension

list_6 = [i if i % 2 == 0 else i * 2 for i in range(1, 11)]
print(list_6)

# Example 4

# Without list comprehension

list_7 = []
for i in range(1, 11):
    if i % 2 == 0:
        list_7.append(i)
    else:
        list_7.append(i * 2)
print(list_7)

# With list comprehension

list_8 = [i if i % 2 == 0 else i * 2 for i in range(1, 11)]
print(list_8)

# Example 5

# Without list comprehension

list_9 = []
for i in range(1, 11):
    if i % 2 == 0:
        list_9.append(i)
    else:
        list_9.append(i * 2)
print(list_9)

# With list comprehension

list_10 = [i if i % 2 == 0 else i * 2 for i in range(1, 11)]
print(list_10)

# Example 6

# Without list comprehension

list_11 = []
for i in range(1, 11):
    if i % 2 == 0:
        list_11.append(i)
    else:
        list_11.append(i * 2)
print(list_11)

# With list comprehension

list_12 = [i if i % 2 == 0 else i * 2 for i in range(1, 11)]
print(list_12)

# Example 7

# Without list comprehension

list_13 = []
for i in range(1, 11):
    if i % 2 == 0:
        list_13.append(i)
    else:
        list_13.append(i * 2)
print(list_13)

# With list comprehension