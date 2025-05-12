"""
Write a function to check if the given expression is balanced or not. https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/
assert check_expression("{()}[{}]") == True
"""


def check_expression(expression):
    stack = []
    for char in expression:
        if char == '(' or char == '[' or char == '{':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0 or stack.pop() != '(':
                return False
        elif char == ']':
            if len(stack) == 0 or stack.pop() != '[':
                return False
        elif char == '}':
            if len(stack) == 0 or stack.pop() != '{':
                return False
    return len(stack) == 0


if __name__ == '__main__':
    print(check_expression("{()}[{}]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))
    print(check_expression("{()}[{]"))