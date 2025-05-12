"""
Write a function to check if the given expression is balanced or not. https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/
assert check_expression("{()}[{}]") == True
"""

def check_expression(expression):
    stack = []
    for char in expression:
        if char in ["(", "[", "{"]:
            stack.append(char)
        elif char in [")", "]", "}"]:
            if len(stack) == 0:
                return False
            if char == ")" and stack.pop()!= "(":
                return False
            if char == "]" and stack.pop()!= "[":
                return False
            if char == "}" and stack.pop()!= "{":
                return False
    return len(stack) == 0

assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{}]") == True