"""
Write a python function to split a string into characters.
assert split('python') == ['p','y','t','h','o','n']
"""

def split(string):
    return list(string)

print(split('python'))
<file_sep>/python/0001_hello_world.py
"""
Write a python function to print 'Hello World'
"""

def hello_world():
    print('Hello World')

hello_world()
<file_sep>/python/0003_reverse_string.py
"""
Write a python function to reverse a string.
assert reverse('python') == 'nohtyp'
"""

def reverse(string):
    return string[::-1]

print(reverse('python'))
<file_sep>/python/0002_reverse_list.py
"""
Write a python function to reverse a list.
assert reverse([1,2,3,4,5]) == [5,4,3,2,1]
"""

def reverse(list):
    return list[::-1]

print(reverse([1,2,3,4,5]))
<file_sep>/python/0004_reverse_list_in_place.py
"""
Write a python function to reverse a list in place.
assert reverse([1,2,3,4,5]) == [5,4,3,2,1]
"""

def reverse(list):
    list.reverse()
    return list

print(reverse([1,2,3,4,5]))
<file_sep>/python/0005_reverse_string_in_place.py
"""
Write a python function to reverse a string in place.
assert reverse('python') == 'nohtyp'
"""

def reverse(string):
    return string[::-1]

print(reverse('python'))
<|endoftext|>