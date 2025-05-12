"""
Write a function that takes as input a tuple of numbers (t_1,...,t_{N+1}) and returns a tuple of length N where the i-th element of the tuple is equal to t_i * t_{i+1}.
assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)
"""

def multiply_elements(t):
    return tuple(t[i] * t[i+1] for i in range(len(t)-1))

print(multiply_elements((1, 5, 7, 8, 10)))
<file_sep>/week_02/day_01/04_list_to_dict.py
"""
Write a function that takes a list of strings and returns a dictionary where the keys are the strings and the values are the lengths of the strings.
assert list_to_dict(["a", "abc", "xyz"]) == {"a": 1, "abc": 3, "xyz": 3}
"""

def list_to_dict(l):
    return {i: len(i) for i in l}

print(list_to_dict(["a", "abc", "xyz"]))
<file_sep>/week_02/day_01/02_list_to_dict.py
"""
Write a function that takes a list of strings and returns a dictionary where the keys are the strings and the values are the lengths of the strings.
assert list_to_dict(["a", "abc", "xyz"]) == {"a": 1, "abc": 3, "xyz": 3}
"""

def list_to_dict(l):
    d = {}
    for i in l:
        d[i] = len(i)
    return d

print(list_to_dict(["a", "abc", "xyz"]))
<file_sep>/week_02/day_01/03_list_to_dict.py
"""
Write a function that takes a list of strings and returns a dictionary where the keys are the strings and the values are the lengths of the strings.
assert list_to_dict(["a", "abc", "xyz"]) == {"a": 1, "abc": 3, "xyz": 3}
"""

def list_to_dict(l):
    d = {}
    for i in l:
        d[i] = len(i)
    return d

print(list_to_dict(["a", "abc", "xyz"]))

def list_to_dict(l):
    return {i: len(i) for i in l}

print(list_to_dict(["a", "abc", "xyz"]))
<file_sep>/week_02/day_01/01_list_to_dict.py
"""
Write a function that takes a list of strings and returns a dictionary where the keys are the strings and the values are the lengths of the strings.
assert list_to_dict(["a", "abc", "xyz"]) == {"a": 1, "abc": 3, "xyz": 3}
"""

def list_to_dict(l):
    d = {}
    for i in l:
        d[i] = len(i)
    return d

print(list_to_dict(["a", "abc", "xyz"]))
<file_sep>/week_02/day_01/05_list_to_dict.py
"""
Write a function that takes a list of strings and returns a dictionary where the keys are the strings and the values are the lengths of the strings.
assert list_to_dict(["a", "abc", "xyz"]) == {"a": 1, "abc": 3, "xyz": 3}
"""

def list_to_dict(l):
    return {i: len(i) for i in l}

print(list_to_dict(["a", "abc", "xyz"]))

def list_to_dict(l):
    d = {}
    for i in l:
        d[i] = len(i)
    return d

print(list_to_dict(["a", "abc", "xyz"]))
<file_sep>/week_02/day_01/06_list_to_dict.py
"""
Write a function that takes a list of strings and returns a dictionary where the keys are the strings and the values are the lengths of the strings.
assert list_to_dict(["a", "abc", "xyz"]) == {"a":