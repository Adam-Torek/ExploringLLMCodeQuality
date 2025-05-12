"""
Write a function to remove the parenthesis and what is inbetween them from a string.
assert remove_parenthesis(["python (chrome)"])==("python")
"""

def remove_parenthesis(lst):
    """
    This function removes the parenthesis and what is inbetween them from a list
    :param lst: list
    :return: list
    """
    new_lst = []
    for item in lst:
        if item.count("()") == 0:
            new_lst.append(item)
        else:
            new_item = item.replace("()", "")
            new_lst.append(new_item)
    return new_lst


#assert remove_parenthesis(["python (chrome)"])==("python")
#assert remove_parenthesis(["python (chrome) (firefox)"])==("python chrome firefox")
#assert remove_parenthesis(["python (chrome) (firefox) (safari)"])==("python chrome firefox safari")