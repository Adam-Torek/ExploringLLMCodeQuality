"""
Write a function to check if the given expression is balanced or not. https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/
assert check_expression("{()}[{}]") == True
"""


def check_expression(expression):
    stack = []
    for char in expression:
        if char == "(" or char == "{" or char == "[":
            stack.append(char)
        elif char == ")":
            if stack[-1] == "(":
                stack.pop()
            else:
                return False
        elif char == "}":
            if stack[-1] == "{":
                stack.pop()
            else:
                return False
        elif char == "]":
            if stack[-1] == "[":
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    assert check_expression("{()}[{}]") == True
    assert check_expression("{()}[{]") == False
    assert check_expression("{()}[") == False
    assert check_expression("{()}[}") == False
    assert check_expression("{()}[}