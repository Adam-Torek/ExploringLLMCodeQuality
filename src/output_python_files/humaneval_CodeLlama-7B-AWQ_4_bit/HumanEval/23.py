def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)


def strlen_recursive(string: str) -> int:
    """ Return length of given string
    >>> strlen_recursive('')
    0
    >>> strlen_recursive('abc')
    3
    """
    if string == '':
        return 0
    else:
        return 1 + strlen_recursive(string[1:])


def strlen_recursive_memo(string: str, memo: dict) -> int:
    """ Return length of given string
    >>> strlen_recursive_memo('', {})
    0
    >>> strlen_recursive_memo('abc', {})
    3
    """
    if string in memo:
        return memo[string]
    else:
        if string == '':
            return 0
        else:
            memo[string] = 1 + strlen_recursive_memo(string[1:], memo)
            return memo[string]


def strlen_recursive_memo_lambda(string: str, memo: dict) -> int:
    """ Return length of given string
    >>> strlen_recursive_memo_lambda('', {})
    0
    >>> strlen_recursive_memo_lambda('abc', {})
    3
    """
    if string in memo:
        return memo[string]
    else:
        if string == '':
            return 0
        else:
            memo[string] = 1 + strlen_recursive_memo_lambda(string[1:], memo)
            return memo[string]


def strlen_recursive_memo_lambda_tco(string: str, memo: dict) -> int:
    """ Return length of given string
    >>> strlen_recursive_memo_lambda_tco('', {})
    0
    >>> strlen_recursive_memo_lambda_tco('abc', {})
    3
    """
    if string in memo:
        return memo[string]
    else:
        if string == '':
            return 0
        else:
            memo[string] = 1 + strlen_recursive_memo_lambda_tco(string[1:], memo)
            return memo[string]


def strlen_recursive_memo_lambda_tco_memo(string: str, memo: dict) -> int:
    """ Return length of given string
    >>> strlen_recursive_memo_lambda_tco_memo('', {})
    0
    >>> strlen_recursive_memo_lambda_tco_memo('abc', {})
    3
    """
    if string in memo:
        return memo[string]
    else:
        if string == '':
            return 0
        else:
            memo[string] = 1 + strlen_recursive_memo_lambda_tco_memo(string[1:], memo)
            return memo[string]


def strlen_recursive_memo_lambda_tco_memo_tco(string: str, memo: dict) -> int:
    """ Return length of given string
    >>> strlen_recursive_memo_lambda_tco_memo_tco('', {})
    0
    >>> strlen_recursive_memo_lambda_tco_memo_tco('abc', {})
    3
    """
    if