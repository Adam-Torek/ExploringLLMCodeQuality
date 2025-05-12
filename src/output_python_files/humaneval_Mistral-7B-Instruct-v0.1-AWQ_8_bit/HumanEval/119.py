def match_parens(lst):
    '''
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['()(', ')']) == 'Yes'
    match_parens([')', ')']) == 'No'
    '''
    def is_good(s):
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if not stack or stack.pop() != '(':
                    return False
        return not stack

    for i in range(len(lst)):
        for j in range(i+1, len(lst)+1):
            if is_good(lst[i] + lst[j-1:j]):
                return 'Yes'
    return 'No'


# test
print(match_parens(['()(', ')']))
print(match_parens([')', ')']))