from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # TODO: Write your code here
    return [max(len(x) for x in group.split(')(')) for group in paren_string.split()]


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)