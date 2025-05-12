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
    # Your code here
    if string == '':
        return False
    if string[0] == ']':
        return False
    if string[-1] == '[':
        return False
    if string.count('[') == string.count(']'):
        return False
    if string.count('[') == 0:
        return False
    if string.count(']') == 0:
        return False
    if string.count('[') == 1 and string.count(']') == 1:
        return False
    if string.count('[') == 1 and string.count(']') == 2:
        return False
    if string.count('[') == 2 and string.count(']') == 1:
        return False
    if string.count('[') == 2 and string.count(']') == 2:
        return False
    if string.count('[') == 3 and string.count(']') == 1:
        return False
    if string.count('[') == 3 and string.count(']') == 2:
        return False
    if string.count('[') == 4 and string.count(']') == 1:
        return False
    if string.count('[') == 4 and string.count(']') == 2:
        return False
    if string.count('[') == 5 and string.count(']') == 1:
        return False
    if string.count('[') == 5 and string.count(']') == 2:
        return False
    if string.count('[') == 6 and string.count(']') == 1:
        return False
    if string.count('[') == 6 and string.count(']') == 2:
        return False
    if string.count('[') == 7 and string.count(']') == 1:
        return False
    if string.count('[') == 7 and string.count(']') == 2:
        return False
    if string.count('[') == 8 and string.count(']') == 1:
        return False
    if string.count('[') == 8 and string.count(']') == 2:
        return False
    if string.count('[') == 9 and string.count(']') == 1:
        return False
    if string.count('[') == 9 and string.count(']') == 2:
        return False
    if string.count('[') == 10 and string.count(']') == 1:
        return False
    if string.count('[') == 10 and string.count(']') == 2:
        return False
    if string.count('[') == 11 and string.count(']') == 1:
        return False
    if string.count('[') == 11 and string.count(']') == 2:
        return False
    if string.count('[') == 12 and string.count(']') == 1:
        return False
    if string.count('[') == 12 and string.count(']') == 2:
        return False
    if string.count('[') == 13 and string.count(']') == 1:
        return False
    if string.count('[') == 13 and string.count(']') == 2:
        return False
    if string.count('[') == 14 and string.count(']') == 1:
        return False
    if string.count('[') == 14 and string.count(']') ==