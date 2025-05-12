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

# Test cases for edge cases
print(check_dict_case({"a":1, "B":2, "c":3})) # False
print(check_dict_case({"a":1, "B":2, "C":3})) # False
print(check_dict_case({"a":1, "A":2, "C":3})) # False
print(check_dict_case({"a":1, "B":2, "C":3, "d":4})) # False
print(check_dict_case({"a":1, "A":2, "C":3, "D":4})) # False
print(check_dict_case({"a":1, "A":2, "C":3, "D":4, "e":5})) # False
print(check_dict_case({"A":1, "B":2, "C":3, "D":4, "E":5})) # False
print(check_dict_case({"A":1, "B":2, "C":3, "D":4, "E":5, "F":6})) # False
print(check_dict_case({"a":1, "B":2, "C":3, "D":4, "E":5, "F":6})) # False
print(check_dict_case({"A":1, "B":2, "C":3, "D":4, "E":5, "F":6})) # False
print(check_dict_case({"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7})) # False
print(check_dict_case({"a":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7})) # False
print(check_dict_case({"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7})) # False
print(check_dict_case({"a":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8})) # False
print(check_dict_case({"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8})) # False
print(check_dict_case({"a":1, "B