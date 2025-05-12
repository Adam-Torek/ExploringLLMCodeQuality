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
    for key in dict:
        if not isinstance(key, str) or not key.isalpha():
            return False
        if key.islower() != dict[key].islower():
            return False
    return True


def check_dict_case_test():
    """
    Test the check_dict_case function
    """
    print(check_dict_case({"a":"apple", "b":"banana"}))
    print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}))
    print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}))
    print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}))
    print(check_dict_case({"STATE":"NC", "ZIP":"12345"}))
    print(check_dict_case({"a":"apple", "b":"banana", "c":"apple"}))
    print(check_dict_case({"a":"apple", "b":"banana", "c":"apple", "d":"banana"}))
    print(check_dict_case({"a":"apple", "b":"banana", "c":"apple", "d":"Banana"}))
    print(check_dict_case({"a":"apple", "b":"banana", "c":"apple", "d":"BaNana"}))
    print(check_dict_case({"a":"apple", "b":"banana", "c":"apple", "d":"BaNana", "e":"banana"}))
    print(check_dict_case({"a":"apple", "b":"banana", "c":"apple", "d":"BaNana", "e":"banana", "f":"12345"}))
    print(check_dict_case({"a":"apple", "b":"banana", "c":"apple", "d":"BaNana", "e":"banana", "f":"12345", "g":"12345"}))
    print(check_dict_case({"a":"apple", "b":"banana", "c":"apple", "d":"BaNana", "e":"banana", "f":"12345", "g":"12345", "h":"12345"}))
    print(check_dict_case({"a":"apple", "b":"banana", "c":"apple", "d":"BaNana", "e":"banana", "f":"12345", "g":"12345", "h":"12345", "i":"12345"}))
    print(check_dict_case({"a":"apple", "b":"banana", "c":"apple", "d":"BaNana", "e":"banana", "f":"12345", "g":"12345", "h":"12345", "i":"12345", "j":"12345"}))
    print(check_dict_case({"a":"apple", "b":"banana", "c":"apple", "d":"BaNana", "e":"banana", "f":"12345", "g":"12345", "h":"12345", "i":"12345", "j":"1