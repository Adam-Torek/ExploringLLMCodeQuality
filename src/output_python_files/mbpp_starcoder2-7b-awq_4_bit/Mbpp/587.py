"""
Write a function to convert a list to a tuple.
assert list_tuple([5, 10, 7, 4, 15, 3])==(5, 10, 7, 4, 15, 3)
"""
def list_tuple(lst):
    return tuple(lst)

print(list_tuple([5, 10, 7, 4, 15, 3]))

"""
Write a function to convert a tuple to a list.
assert tuple_list((5, 10, 7, 4, 15, 3))==[5, 10, 7, 4, 15, 3]
"""
def tuple_list(tup):
    return list(tup)

print(tuple_list((5, 10, 7, 4, 15, 3)))

"""
Write a function to convert a list to a set.
assert list_set([5, 10, 7, 4, 15, 3])=={3, 4, 5, 7, 10, 15}
"""
def list_set(lst):
    return set(lst)

print(list_set([5, 10, 7, 4, 15, 3]))

"""
Write a function to convert a set to a list.
assert set_list({3, 4, 5, 7, 10, 15})==[3, 4, 5, 7, 10, 15]
"""
def set_list(st):
    return list(st)

print(set_list({3, 4, 5, 7, 10, 15}))

"""
Write a function to convert a list to a dictionary.
assert list_dict([5, 10, 7, 4, 15, 3])=={3: 5, 4: 10, 5: 7, 7: 4, 10: 15, 15: 3}
"""
def list_dict(lst):
    return dict(zip(lst, lst))

print(list_dict([5, 10, 7, 4, 15, 3]))

"""
Write a function to convert a dictionary to a list.
assert dict_list({3: 5, 4: 10, 5: 7, 7: 4, 10: 15, 15: 3})==[3, 5, 4, 10, 7, 15, 3]
"""
def dict_list(dct):
    return list(dct.values())

print(dict_list({3: 5, 4: 10, 5: 7, 7: 4, 10: 15, 15: 3}))

"""
Write a function to convert a list to a string.
assert list_string([5, 10, 7, 4, 15, 3])=='51074153'
"""
def list_string(lst):
    return ''.join(map(str, lst))

print(list_string([5, 10, 7, 4, 15, 3]))

"""
Write a function to convert a string to a list.
assert string_list('51074153')==[5, 10, 7, 4, 15, 3]
"""
def string_list(st):
    return list(map(int, st))

print(string_list('51074153'))

"""
Write a function to convert a list to a tuple.
assert list_tuple([5, 10, 7, 4, 15, 3])==(5, 10, 7, 4, 15, 3)
"""
def list_tuple(lst):
    return tuple(lst)

print(list_tuple([5, 10, 7, 4, 15, 3]))

"""
Write a function to convert a tuple to a list.
assert tuple_list((