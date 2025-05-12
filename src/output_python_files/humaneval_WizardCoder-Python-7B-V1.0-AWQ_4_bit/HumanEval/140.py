def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    return re.sub(r'\s+', lambda x: '-' if len(x.group(0)) > 1 else '_', text)


def fix_spaces_in_dict(d):
    """
    Given a dictionary d, recursively replace all spaces in keys and values with underscores
    """
    if isinstance(d, dict):
        return {fix_spaces(k): fix_spaces_in_dict(v) for k, v in d.items()}
    elif isinstance(d, (list, tuple)):
        return [fix_spaces_in_dict(x) for x in d]
    else:
        return d

def fix_spaces_in_dict_recursive(d):
    """
    Given a dictionary d, recursively replace all spaces in keys and values with underscores
    """
    if isinstance(d, dict):
        return {fix_spaces(k): fix_spaces_in_dict_recursive(v) for k, v in d.items()}
    elif isinstance(d, (list, tuple)):
        return [fix_spaces_in_dict_recursive(x) for x in d]
    else:
        return d

def fix_spaces_in_dict_recursive_inplace(d):
    """
    Given a dictionary d, recursively replace all spaces in keys and values with underscores
    """
    if isinstance(d, dict):
        for k, v in d.items():
            d[fix_spaces(k)] = fix_spaces_in_dict_recursive_inplace(v)
        return d
    elif isinstance(d, (list, tuple)):
        return [fix_spaces_in_dict_recursive_inplace(x) for x in d]
    else:
        return d

def fix_spaces_in_dict_recursive_inplace_2(d):
    """
    Given a dictionary d, recursively replace all spaces in keys and values with underscores
    """
    if isinstance(d, dict):
        for k, v in list(d.items()):
            if isinstance(v, (dict, list, tuple):
                fix_spaces_in_dict_recursive_inplace_2(v)
            d[fix_spaces(k)] = fix_spaces_in_dict_recursive_inplace_2(v)
        return d
    elif isinstance(d, (list, tuple):
        for i, x in enumerate(d):
            if isinstance(x, (dict, list, tuple):
                fix_spaces_in_dict_recursive_inplace_2(x)
            d[i] = fix_spaces_in_dict_recursive_inplace_2(x)
        return d
    else:
        return d

def fix_spaces_in_dict_recursive_inplace_3(d):
    """
    Given a dictionary d, recursively replace all spaces in keys and values with underscores
    """
    if isinstance(d, dict):
        for k, v in list(d.items()):
            if isinstance(v, (dict, list, tuple):
                fix_spaces_in_dict_recursive_inplace_3(v)
            d[fix_spaces(k)] = fix_spaces_in_dict_