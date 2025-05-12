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

# Solution:
# We can solve this problem by using dynamic programming. We will create a 2D
# array dp where dp[i][j] represents whether it is possible to concatenate
# the first i strings with the last j strings to form a valid string.
#
# We will fill in the dp array in a bottom-up manner. For each position i,
# we will check if it is possible to concatenate the first i-1 strings with the
# last j strings to form a valid string. If it is, we will set dp[i][j] to
# True. Otherwise, we will set dp[i][j] to False.
#
# Then, we will check if it is possible to concatenate the first i strings with
# the last j-1 strings to form a valid string. If it is, we will set dp[i][j] to
# True. Otherwise, we will set dp[i][j] to False.
#
# Finally, we will check if it is possible to concatenate the first i-1 strings
# with the last j-1 strings to form a valid string. If it is, we will set
# dp[i][j] to True. Otherwise, we will set dp[i][j] to False.
#
# If dp[i][j] is True, it means it is possible to concatenate the first i
# strings with the last j strings to form a valid string. We will check if it
# is a good string by checking if all parentheses in the resulting string are
# balanced. If it is, we will return 'Yes'. Otherwise, we will return 'No'.

def match_parens(lst):
    n = len(lst)
    dp = [[False] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if lst[i-1] == '(':
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if lst[i-1] == '(':
                dp[i][j] = dp[i][j] or dp[i-1][j-1]
            else:
                dp[i][j] = dp[i][j] or dp[i-1][j]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if lst[i-1] == '(':
                dp[i][j] = dp[i][j] or dp[i-1][j-1]
            else:
                dp[i][j] = dp[i][j] or dp[i-1][j]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if lst[i-1] == '(':
                dp[i][j] = dp[i][j] or dp[i-1][j-1]
            else:
                dp[i][j] = dp[i][j] or dp[i-1][j]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if lst[i-1] == '(':
                dp[i][j] = dp[i][j] or dp[i-1][j-1]
            else:
                dp[i][j] = dp[i][j] or dp[i-1][j]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if lst[i-1] == '(':
                dp[i][j] = dp[i][j] or