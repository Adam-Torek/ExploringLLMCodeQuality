"""
Write a function to check if the given expression is balanced or not. https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/
assert check_expression("{()}[{}]") == True
"""

def check_expression(expression):
    stack = []
    for token in expression.split():
        if token == '(':
            stack.append(token)
        elif token == ')':
            if not stack or stack.pop() != '(':
                return False
        elif token == '[':
            stack.append(token)
        elif token == ']':
            if not stack or stack.pop() != '[':
                return False
        elif token == '{' or token == '}':
            if not stack or stack.pop() != token:
                return False
        else:
            return False
    return not stack


if __name__ == '__main__':
    print(check_expression("{()}[{}]"))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))
    print(check_expression("{()}[{}]("))