from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # TODO: Write your code here
    return []


if __name__ == '__main__':
    print("Example:")
    print(parse_nested_parens('(()()) ((())) () ((())()())'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested_parens('()') == [0]
    assert parse_nested_parens('((()))') == [2]
    assert parse_nested_parens('((()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested_parens('((()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested_parens('((()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested_parens('((()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested_parens('((()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested_parens('((()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested_parens('((()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested_parens('((()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested_parens('((()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested_parens('((()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested_parens('((()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested_parens('((()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested_parens('((()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested_parens('((()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested_parens('((()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested_parens('((()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested_parens('((()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested_parens('((()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested_parens('((()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested_parens('((()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested_parens('((()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested_parens('((()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested