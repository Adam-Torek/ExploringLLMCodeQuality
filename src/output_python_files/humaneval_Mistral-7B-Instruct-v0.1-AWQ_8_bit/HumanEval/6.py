from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    max_level = 0
    levels = []
    for paren in paren_string.split():
        if paren == '(':
            levels.append(1)
        elif paren == ')':
            if levels.pop() == 1:
                max_level = max(max_level, levels[-1])
            else:
                raise ValueError("Invalid parens string")
    return levels


def parse_nested_parens_with_depth(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens_with_depth('(((()))')
    [3]
    >>> parse_nested_parens_with_depth('((()))')
    [2]
    >>> parse_nested_parens_with_depth('()')
    [1]
    >>> parse_nested_parens_with_depth('()((()))')
    [2, 3]
    >>> parse_nested_parens_with_depth('()((()))()')
    [2, 3, 1]
    """
    max_level = 0
    levels = []
    for paren in paren_string.split():
        if paren == '(':
            levels.append(1)
        elif paren == ')':
            if levels.pop() == 1:
                max_level = max(max_level, levels[-1])
            else:
                raise ValueError("Invalid parens string")
    return levels