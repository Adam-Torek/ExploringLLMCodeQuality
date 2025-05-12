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
            if not stack:
                return False
            if char == ")" and stack[-1] == "(":
                stack.pop()
            elif char == "]" and stack[-1] == "[":
                stack.pop()
            elif char == "}" and stack[-1] == "{":
                stack.pop()
            else:
                return False
    return len(stack) == 0

# Test cases
print(check_expression("{()}[{}]")) # True
print(check_expression("{[}]")) # False
print(check_expression("(())")) # True
print(check_expression("({[)]")) # False
print(check_expression("([]{})")) # True
print(check_expression("()")) # True
print(check_expression("()[]{}")) # True
print(check_expression("(({[]}){})")) # True
print(check_expression("(({[]}){})")) # True
print(check_expression("({[)]")) # False
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(check_expression("({[({})]})")) # True
print(