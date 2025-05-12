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
    if len(lst) == 0:
        return 'Yes'
    if len(lst) == 1:
        return 'No'
    if len(lst) == 2:
        if lst[0] == lst[1]:
            return 'Yes'
        else:
            return 'No'
    if len(lst) == 3:
        if lst[0] == lst[1] and lst[1] == lst[2]:
            return 'Yes'
        else:
            return 'No'
    if len(lst) == 4:
        if lst[0] == lst[1] and lst[1] == lst[2] and lst[2] == lst[3]:
            return 'Yes'
        else:
            return 'No'
    if len(lst) == 5:
        if lst[0] == lst[1] and lst[1] == lst[2] and lst[2] == lst[3] and lst[3] == lst[4]:
            return 'Yes'
        else:
            return 'No'
    if len(lst) == 6:
        if lst[0] == lst[1] and lst[1] == lst[2] and lst[2] == lst[3] and lst[3] == lst[4] and lst[4] == lst[5]:
            return 'Yes'
        else:
            return 'No'
    if len(lst) == 7:
        if lst[0] == lst[1] and lst[1] == lst[2] and lst[2] == lst[3] and lst[3] == lst[4] and lst[4] == lst[5] and lst[5] == lst[6]:
            return 'Yes'
        else:
            return 'No'
    if len(lst) == 8:
        if lst[0] == lst[1] and lst[1] == lst[2] and lst[2] == lst[3] and lst[3] == lst[4] and lst[4] == lst[5] and lst[5] == lst[6] and lst[6] == lst[7]:
            return 'Yes'
        else:
            return 'No'
    if len(lst) == 9:
        if lst[0] == lst[1] and lst[1] == lst[2] and lst[2] == lst[3] and lst[3] == lst[4] and lst[4] == lst[5] and lst[5] == lst[6] and lst[6] == lst[7] and lst[7] == lst[8]:
            return 'Yes'
        else:
            return 'No'
    if len(lst) == 10:
        if lst[0] == lst[1] and lst[1] == lst[2] and lst[2] == lst[3] and lst[3] == lst[4] and lst[4] == lst[5] and lst[5] == lst[6] and lst[6] == lst[7] and lst[7] == lst[8] and lst