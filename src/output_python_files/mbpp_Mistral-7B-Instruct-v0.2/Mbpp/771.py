"""
Write a function to check if the given expression is balanced or not. https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/
assert check_expression("{()}[{}]") == True
"""
from collections import deque


def check_expression(expression):
    stack = deque()
    opening_brackets = "([{"
    closing_brackets = ")]}"
    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack.pop() != opening_brackets[closing_brackets.index(char)]:
                return False
    return not stack


if __name__ == "__main__":
    assert check_expression("{()}[{}]") == True
    assert check_expression("{[()]}") == True
    assert check_expression("{[(])}") == False
    assert check_expression("{[()]}()") == True
    assert check_expression("{[()]}()()") == True
    assert check_expression("{[()]}()()()") == True
    assert check_expression("{[()]}()()()()") == True
    assert check_expression("{[()]}()()()()()") == True
    assert check_expression("{[()]}()()()()()()") == True
    assert check_expression("{[()]}()()()()()()()") == True
    assert check_expression("{[()]}()()()()()()()()") == True
    assert check_expression("{[()]}()()()()()()()()()") == True
    assert check_expression("{[()]}()()()()()()()()()()") == True
    assert check_expression("{[()]}()()()()()()()()()()()") == True
    assert check_expression("{[()]}()()()()()()()()()()()()") == True
    assert check_expression("{[()]}()()()()()()()()()()()()()") == True
    assert check_expression("{[()]}()()()()()()()()()()()()()()") == True
    assert check_expression("{[()]}()()()()()()()()()()()()()()()") == True
    assert check_expression("{[()]}()()()()()()()()()()()()()()()()") == True
    assert check_expression("{[()]}()()()()()()()()()()()()()()()()()") == True
    assert check_expression("{[()]}()()()()()()()()()()()()()()()()()()") == True
    assert check_expression("{[()]}()()()()()()()()()()()()()()()()()()()") == True
    assert check_expression("{[()]}()()()()()()()()()()()()()()()()()()()()") == True
    assert check_expression("{[()]}()()()()()()()()()()()()()()()()()()()()()") == True
    assert check_expression("{[()]}()()()()()()()()()()()()()()()()()()()()()()") == True
    assert check_expression("{[()]}()()()()()()()()()()()()()()()()()()()()()()()") == True
    assert check_expression("{[()]}()()()()()()()()()()()()()()()()()()()()()()()()") == True
    assert check_expression("{[()]}()()()()()()()()()()()()()()()()()()()()()()()()()") == True
    assert check_expression("{[()]}()()()()()()()()()()()()()()()()()()()()()()()()()()") == True
    assert check_expression("{[()]}()()()()()()()()()()()()()()()()()()()()()()()()()()()") == True
    assert check_expression("{[()]}()()()()()()()()()()()()()()()()()()()()