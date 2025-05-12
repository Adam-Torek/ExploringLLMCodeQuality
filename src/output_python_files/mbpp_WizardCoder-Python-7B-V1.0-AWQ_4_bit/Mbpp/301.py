"""
Write a function to find the depth of a dictionary.
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
"""

def dict_depth(d):
    if not isinstance(d, dict):
        return 0
    elif not d:
        return 1
    else:
        return 1 + max(dict_depth(v) for v in d.values())

# Test cases
print(dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4) # True
print(dict_depth({'a':1, 'b': {'c': {'d': {'e': {'f': {}}}})==5) # True
print(dict_depth({'a':1, 'b': {'c': {'d': {'e': {'f': {'g': {'h': {}}}})==6) # True
print(dict_depth({'a':1, 'b': {'c': {'d': {'e': {'f': {'g': {'h': {'i': {}}}})==7) # True
print(dict_depth({'a':1, 'b': {'c': {'d': {'e': {'f': {'g': {'h': {'i': {'j': {}}}})==8) # True
print(dict_depth({'a':1, 'b': {'c': {'d': {'e': {'f': {'g': {'h': {'i': {'j': {'k': {}}})==9) # True
print(dict_depth({'a':1, 'b': {'c': {'d': {'e': {'f': {'g': {'h': {'i': {'j': {'k': {'l': {}}})==10) # True
print(dict_depth({'a':1, 'b': {'c': {'d': {'e': {'f': {'g': {'h': {'i': {'j': {'k': {'l': {'m': {}}})==11) # True
print(dict_depth({'a':1, 'b': {'c': {'d': {'e': {'f': {'g': {'h': {'i': {'j': {'k': {'l': {'m': {'n': {}}})==12) # True
print(dict_depth({'a':1, 'b': {'c': {'d': {'e': {'f': {'g': {'h': {'i': {'j': {'k': {'l': {'m': {'n': {'o': {}}})==13) # True
print(dict_depth({'a':1, 'b': {'c': {'d': {'e': {'f': {'g': {'h': {'i': {'j': {'k': {'l': {'m': {'n': {'o': {'p': {}}})==14) # True
print(dict_depth({'a':1, 'b': {'c': {'d': {'e': {'f': {'g': {'h': {'i': {'j': {'k': {'l': {'m': {'n': {'o': {'p': {'q': {}}})==15) # True
print(dict_depth({'a':1, 'b': {'c': {'d': {'e': {'f': {'g': {'h': {'i': {'j': {'k': {'l': {'m': {'n': {'o': {'p': {'q': {'r': {}}})==16) # True
print(dict_depth({'a':1, 'b': {'c': {'d': {'e': {'f': {'g': {'h': {'i': {'j': {'k': {'l': {'m': {'n': {'o': {'p': {'q': {'r': {'s': {}}})==17) # True
print(dict_depth({'a':1, 'b': {'c': {'d': {'e': {'f': {'g': {'h': {'i': {'j': {'k': {'l': {'m': {'n': {'o': {'p': {'q': {'r': {'s': {'t': {}}})==18) # True
print(dict_depth({'a':1, 'b': {'c': {'d': {'e