"""
Write a function to check if the given expression is balanced or not. https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/
assert check_expression("{()}[{}]") == True
"""

def check_expression(expr):
    stack = []
    for char in expr:
        if char in ["(", "{", "["]:
            stack.append(char)
        elif char in [")", "}", "]"]:
            if not stack:
                return False
            else:
                open_char = stack.pop()
            if (char == ")" and open_char != "(") or (char == "}" and open_char != "{") or (char == "]" and open_char != "["):
                return False
    return not stack

# Test cases
print(check_expression("{()}")) # True
print(check_expression("{[()]}")) # True
print(check_expression("{[(])}")) # False
print(check_expression("{()}")) # True
print(check_expression("{[()]}")) # True
print(check_expression("{[(])}")) # False
print(check_expression("{[()]")) # False
print(check_expression("")) # True
print(check_expression(")")) # False
print(check_expression("{")) # False
print(check_expression("{()}")) # True
print(check_expression("{[()]}")) # True
print(check_expression("{[(])}")) # False
print(check_expression("{[()]")) # False
print(check_expression("")) # True
print(check_expression(")")) # False
print(check_expression("{")) # False
print(check_expression("{()}")) # True
print(check_expression("{[()]}")) # True
print(check_expression("{[(])}")) # False
print(check_expression("{[()]")) # False