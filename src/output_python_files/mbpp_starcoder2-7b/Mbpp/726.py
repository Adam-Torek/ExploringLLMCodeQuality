"""
Write a function that takes as input a tuple of numbers (t_1,...,t_{N+1}) and returns a tuple of length N where the i-th element of the tuple is equal to t_i * t_{i+1}.
assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)
"""

def multiply_elements(t):
    return tuple(t[i] * t[i+1] for i in range(len(t)-1))

print(multiply_elements((1, 5, 7, 8, 10)))
/week02/day03/02_list_to_dict.py
"""
Write a function that takes a list of strings and returns a dictionary where the keys are the strings and the values are the lengths of the strings.
assert list_to_dict(["a", "bb", "ccc"]) == {"a": 1, "bb": 2, "ccc": 3}
"""

def list_to_dict(l):
    return {i: len(i) for i in l}

print(list_to_dict(["a", "bb", "ccc"]))
/week02/day03/01_list_to_dict.py
"""
Write a function that takes a list of strings and returns a dictionary where the keys are the strings and the values are the indices of the strings.
assert list_to_dict(["a", "bb", "ccc"]) == {"a": 0, "bb": 1, "ccc": 2}
"""

def list_to_dict(l):
    return {i: l.index(i) for i in l}

print(list_to_dict(["a", "bb", "ccc"]))
/week02/day03/03_list_to_dict.py
"""
Write a function that takes a list of strings and returns a dictionary where the keys are the strings and the values are the first letters of the strings.
assert list_to_dict(["a", "bb", "ccc"]) == {"a": "a", "bb": "b", "ccc": "c"}
"""

def list_to_dict(l):
    return {i: i[0] for i in l}

print(list_to_dict(["a", "bb", "ccc"]))
/week02/day03/04_list_to_dict.py
"""
Write a function that takes a list of strings and returns a dictionary where the keys are the strings and the values are the last letters of the strings.
assert list_to_dict(["a", "bb", "ccc"]) == {"a": "a", "bb": "b", "ccc": "c"}
"""

def list_to_dict(l):
    return {i: i[-1] for i in l}

print(list_to_dict(["a", "bb", "ccc"]))
/week02/day03/05_list_to_dict.py
"""
Write a function that takes a list of strings and returns a dictionary where the keys are the strings and the values are the lengths of the strings.
assert list_to_dict(["a", "bb", "ccc"]) == {"a": 1, "bb": 2, "ccc": 3}
"""

def list_to_dict(l):
    return {i: len(i) for i in l}

print(list_to_dict(["a", "bb", "ccc"]))
/week02/day03/06_list_to_dict.py
"""
Write a function that takes a list of strings and returns a dictionary where the keys are the strings and the values are the first and last letters of the strings.
assert list_to_dict(["a", "bb", "ccc"]) == {"a": "aa", "bb": "bb", "ccc": "cc"}
"""

def list_to_dict(l):
    return {i: i[0] + i[-1] for i in l}

print(list_to_dict(["a", "bb", "ccc"]))
/week02/day03/07_list_to_dict.py
"""
Write a function that takes a list of strings and returns a dictionary where the keys are the strings and the values are the first and last letters of