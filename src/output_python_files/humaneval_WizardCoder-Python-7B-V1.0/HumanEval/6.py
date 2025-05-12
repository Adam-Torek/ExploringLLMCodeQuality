from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    max_level = 0
    result = []
    level = 0
    for char in paren_string:
        if char == '(':
            level += 1
            max_level = max(level, max_level)
        elif char == ')':
            level -= 1
        if level == 0:
            result.append(max_level)
            max_level = 0
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()