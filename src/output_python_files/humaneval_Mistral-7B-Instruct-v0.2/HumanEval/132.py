def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if not stack or stack.pop() != '[':
                return False
    return not stack

# Test Cases
print(is_nested('[[]]')) # True
print(is_nested('[]]]]]]][[[[[]')) # False
print(is_nested('[][]')) # False
print(is_nested('[]')) # False
print(is_nested('[[][]]')) # True
print(is_nested('[[]][[')) # True