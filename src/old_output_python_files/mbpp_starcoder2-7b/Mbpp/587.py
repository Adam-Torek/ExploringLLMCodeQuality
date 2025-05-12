"""
Write a function to convert a list to a tuple.
assert list_tuple([5, 10, 7, 4, 15, 3])==(5, 10, 7, 4, 15, 3)
"""
def list_tuple(l):
    return tuple(l)

assert list_tuple([5, 10, 7, 4, 15, 3])==(5, 10, 7, 4, 15, 3)

"""
Write a function to convert a tuple to a list.
assert tuple_list((5, 10, 7, 4, 15, 3))==[5, 10, 7, 4, 15, 3]
"""
def tuple_list(t):
    return list(t)

assert tuple_list((5, 10, 7, 4, 15, 3))==[5, 10, 7, 4, 15, 3]

"""
Write a function to convert a tuple to a dictionary.
assert tuple_dict((5, 10, 7, 4, 15, 3))=={5: 10, 7: 4, 15: 3}
"""
def tuple_dict(t):
    return dict(t)

assert tuple_dict((5, 10, 7, 4, 15, 3))=={5: 10, 7: 4, 15: 3}

"""
Write a function to convert a dictionary to a tuple.
assert dict_tuple({5: 10, 7: 4, 15: 3})==((5, 10), (7, 4), (15, 3))
"""
def dict_tuple(d):
    return tuple(d.items())

assert dict_tuple({5: 10, 7: 4, 15: 3})==((5, 10), (7, 4), (15, 3))

"""
Write a function to convert a dictionary to a list.
assert dict_list({5: 10, 7: 4, 15: 3})==[(5, 10), (7, 4), (15, 3)]
"""
def dict_list(d):
    return list(d.items())

assert dict_list({5: 10, 7: 4, 15: 3})==[(5, 10), (7, 4), (15, 3)]

"""
Write a function to convert a dictionary to a set.
assert dict_set({5: 10, 7: 4, 15: 3})=={(5, 10), (7, 4), (15, 3)}
"""
def dict_set(d):
    return set(d.items())

assert dict_set({5: 10, 7: 4, 15: 3})=={(5, 10), (7, 4), (15, 3)}

"""
Write a function to convert a set to a dictionary.
assert set_dict({(5, 10), (7, 4), (15, 3)})=={5: 10, 7: 4, 15: 3}
"""
def set_dict(s):
    return dict(s)

assert set_dict({(5, 10), (7, 4), (15, 3)})=={5: 10, 7: 4, 15: 3}

"""
Write a function to convert a set to a list.
assert set_list({(5, 10), (7, 4), (15, 3)})==[(5, 10), (7, 4), (15, 3)]
"""
def set_list(s):
    return list(s)

assert set_list({(5, 10), (7, 4), (15, 3)})==[(5, 10), (7, 4), (15, 3)]

"""
Write a function to convert a set to a tuple.
assert set_tuple({(5, 1