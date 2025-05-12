def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
    """
    if not dict:
        return False
    return all(isinstance(key, str) and key.islower() for key in dict.keys()) or all(isinstance(key, str) and key.isupper() for key in dict.keys())


# Test cases
print(check_dict_case({"a":"apple", "b":"banana"})) # True
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"})) # False
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"})) # False
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"})) # False
print(check_dict_case({"STATE":"NC", "ZIP":"12345" })) # True
print(check_dict_case({})) # False

# Test case for empty dictionary
print(check_dict_case({})) # False

# Test case for dictionary with mixed keys
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"})) # False

# Test case for dictionary with mixed keys
print(check_dict_case({"a":"apple", "A":"banana", "b":"banana"})) # False

# Test case for dictionary with mixed keys
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana", "c":"cherry"})) # False

# Test case for dictionary with mixed keys
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana", "C":"cherry"})) # False

# Test case for dictionary with mixed keys
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana", "c":"cherry", "d":"date"})) # False

# Test case for dictionary with mixed keys
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana", "c":"cherry", "D":"date"})) # False

# Test case for dictionary with mixed keys
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana", "c":"cherry", "D":"date", "e":"elderberry"})) # False

# Test case for dictionary with mixed keys
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana", "c":"cherry", "D":"date", "E":"elderberry"})) # False

# Test case for dictionary with mixed keys
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana", "c":"cherry", "D":"date", "e":"elderberry", "F":"fig"})) # False

# Test case for dictionary with mixed keys
print(check