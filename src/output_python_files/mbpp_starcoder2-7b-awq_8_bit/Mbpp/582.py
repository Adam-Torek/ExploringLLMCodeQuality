"""
Write a function to check if a dictionary is empty
assert my_dict({10})==False
"""

def is_empty(my_dict):
    if len(my_dict) == 0:
        return True
    else:
        return False

assert is_empty({10})==False
assert is_empty({})==True

"""
Write a function to check if a dictionary contains a key
assert my_dict({10})==False
"""

def contains_key(my_dict, key):
    if key in my_dict:
        return True
    else:
        return False

assert contains_key({10:10}, 10)==True
assert contains_key({10:10}, 11)==False

"""
Write a function to check if a dictionary contains a value
assert my_dict({10})==False
"""

def contains_value(my_dict, value):
    if value in my_dict.values():
        return True
    else:
        return False

assert contains_value({10:10}, 10)==True
assert contains_value({10:10}, 11)==False

"""
Write a function to check if a dictionary contains a key-value pair
assert my_dict({10})==False
"""

def contains_key_value_pair(my_dict, key, value):
    if key in my_dict and value in my_dict.values():
        return True
    else:
        return False

assert contains_key_value_pair({10:10}, 10, 10)==True
assert contains_key_value_pair({10:10}, 10, 11)==False

"""
Write a function to check if a dictionary contains a key-value pair
assert my_dict({10})==False
"""

def contains_key_value_pair(my_dict, key, value):
    if key in my_dict and value in my_dict.values():
        return True
    else:
        return False

assert contains_key_value_pair({10:10}, 10, 10)==True
assert contains_key_value_pair({10:10}, 10, 11)==False

"""
Write a function to check if a dictionary contains a key-value pair
assert my_dict({10})==False
"""

def contains_key_value_pair(my_dict, key, value):
    if key in my_dict and value in my_dict.values():
        return True
    else:
        return False

assert contains_key_value_pair({10:10}, 10, 10)==True
assert contains_key_value_pair({10:10}, 10, 11)==False

"""
Write a function to check if a dictionary contains a key-value pair
assert my_dict({10})==False
"""

def contains_key_value_pair(my_dict, key, value):
    if key in my_dict and value in my_dict.values():
        return True
    else:
        return False

assert contains_key_value_pair({10:10}, 10, 10)==True
assert contains_key_value_pair({10:10}, 10, 11)==False

"""
Write a function to check if a dictionary contains a key-value pair
assert my_dict({10})==False
"""

def contains_key_value_pair(my_dict, key, value):
    if key in my_dict and value in my_dict.values():
        return True
    else:
        return False

assert contains_key_value_pair({10:10}, 10, 10)==True
assert contains_key_value_pair({10:10}, 10, 11)==False

"""
Write a function to check if a dictionary contains a key-value pair
assert my_dict({10})==False
"""

def contains_key_value_pair(my_dict, key, value):
    if key in my_dict and value in my_dict.values():
        return True
    else:
        return False

assert contains_key_value_pair({10:10}, 10, 10)==True
assert contains_key_value_pair({10:10}, 10, 11)==False

"""