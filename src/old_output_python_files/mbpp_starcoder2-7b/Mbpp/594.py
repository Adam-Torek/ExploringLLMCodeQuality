"""
Write a function to find the difference of the first even and first odd number of a given list.
assert diff_even_odd([1,3,5,7,4,1,6,8])==3
"""

def diff_even_odd(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2 == 0:
            even = i
            break
    for i in lst:
        if i%2!= 0:
            odd = i
            break
    return even - odd

print(diff_even_odd([1,3,5,7,4,1,6,8]))
<file_sep>/python/0000_python_basics/0000_python_basics_0003_list_comprehension.py
"""
List comprehension
"""

# List comprehension
# [expression for item in list]

# Example 1
lst = [1, 2, 3, 4, 5]
lst_comp = [i for i in lst]
print(lst_comp)

# Example 2
lst = [1, 2, 3, 4, 5]
lst_comp = [i*2 for i in lst]
print(lst_comp)

# Example 3
lst = [1, 2, 3, 4, 5]
lst_comp = [i*2 for i in lst if i%2 == 0]
print(lst_comp)

# Example 4
lst = [1, 2, 3, 4, 5]
lst_comp = [i*2 for i in lst if i%2!= 0]
print(lst_comp)

# Example 5
lst = [1, 2, 3, 4, 5]
lst_comp = [i*2 for i in lst if i%2 == 0]
lst_comp.append(100)
print(lst_comp)

# Example 6
lst = [1, 2, 3, 4, 5]
lst_comp = [i*2 for i in lst if i%2 == 0]
lst_comp.append(100)
lst_comp.append(200)
print(lst_comp)

# Example 7
lst = [1, 2, 3, 4, 5]
lst_comp = [i*2 for i in lst if i%2 == 0]
lst_comp.append(100)
lst_comp.append(200)
lst_comp.append(300)
print(lst_comp)

# Example 8
lst = [1, 2, 3, 4, 5]
lst_comp = [i*2 for i in lst if i%2 == 0]
lst_comp.append(100)
lst_comp.append(200)
lst_comp.append(300)
lst_comp.append(400)
print(lst_comp)

# Example 9
lst = [1, 2, 3, 4, 5]
lst_comp = [i*2 for i in lst if i%2 == 0]
lst_comp.append(100)
lst_comp.append(200)
lst_comp.append(300)
lst_comp.append(400)
lst_comp.append(500)
print(lst_comp)

# Example 10
lst = [1, 2, 3, 4, 5]
lst_comp = [i*2 for i in lst if i%2 == 0]
lst_comp.append(100)
lst_comp.append(200)
lst_comp.append(300)
lst_comp.append(400)
lst_comp.append(500)
lst_comp.append(600)
print(lst_comp)

# Example 11
lst = [1, 2, 3, 4, 5]
lst_comp = [i*2 for i in lst if i%2 == 0]
lst_comp.append(100)
lst_comp.append(200)
lst_comp.append(300)
lst_comp.append(