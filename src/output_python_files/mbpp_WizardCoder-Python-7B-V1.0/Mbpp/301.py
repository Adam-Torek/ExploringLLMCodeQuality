"""
Write a function to find the depth of a dictionary.
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
"""

def dict_depth(d):
    if type(d) != dict:
        return 0
    if not d:
        return 1
    return 1 + max(dict_depth(v) for v in d.values() if type(v) == dict)

# Test cases
print(dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4) # True
print(dict_depth({'a':1, 'b': {'c': {'d': {'e': {'f': {}}}})==5) # True
print(dict_depth({'a':1, 'b': {'c': {'d': {'e': {'f': 2}})==4) # True
print(dict_depth({'a':1, 'b': {'c': {'d': {'e': {'f': [1, 2, {'g': {}}})==5) # True
print(dict_depth({'a':1, 'b': {'c': {'d': {'e': {'f': [1, 2, {'g': {'h': {}}})==6) # True
print(dict_depth({'a':1, 'b': {'c': {'d': {'e': {'f': [1, 2, {'g': {'h': {'i': {}}})==7) # True
print(dict_depth({'a':1, 'b': {'c': {'d': {'e': {'f': [1, 2, {'g': {'h': {'i': {'j': {}}})==7) # True
print(dict_depth({'a':1, 'b': {'c': {'d': {'e': {'f': [1, 2, {'g': {'h': {'i': {'j': {'k': {}}})==8) # True
print(dict_depth({'a':1, 'b': {'c': {'d': {'e': {'f': [1, 2, {'g': {'h': {'i': {'j': {'k': {'l': {}}})==9) # True
print(dict_depth({'a':1, 'b': {'c': {'d': {'e': {'f': [1, 2, {'g': {'h': {'i': {'j': {'k': {'l': {'m': {}}})==10) # True
print(dict_depth({'a':1, 'b': {'c': {'d': {'e': {'f': [1, 2, {'g': {'h': {'i': {'j': {'k': {'l': {'m': {'n': {}}})==11) # True
print(dict_depth({'a':1, 'b': {'c': {'d': {'e': {'f': [1, 2, {'g': {'h': {'i': {'j': {'k': {'l': {'m': {'n': {'o': {}}})==12) # True
print(dict_depth({'a':1, 'b': {'c': {'d': {'e': {'f': [1, 2, {'g': {'h': {'i': {'j': {'k': {'l': {'m': {'n': {'o': {'p': {}}})==13) # True
print(dict_depth({'a':1, 'b': {'c': {'d': {'e': {'f': [1, 2, {'g': {'h': {'i': {'j': {'k': {'l': {'m': {'n': {'o': {'p': {'q': {}}})==14) # True
print(dict_depth({'a':1, 'b': {'c': {'d': {'e': {'f': [1, 2, {'g': {'h': {'i': {'j': {'k': {'l': {'m': {'n': {'o': {'p': {'q': {'r': {}}})==15) # True
print(dict_depth({'a':1, 'b': {'c': {'d': {'e': {'f': [1