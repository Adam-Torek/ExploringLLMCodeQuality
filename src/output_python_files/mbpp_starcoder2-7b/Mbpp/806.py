"""
Write a function to find maximum run of uppercase characters in the given string.
assert max_run_uppercase('GeMKSForGERksISBESt') == 5
"""

def max_run_uppercase(string):
    """
    >>> max_run_uppercase('GeMKSForGERksISBESt')
    5
    """
    max_run = 0
    current_run = 0
    for char in string:
        if char.isupper():
            current_run += 1
        else:
            if current_run > max_run:
                max_run = current_run
            current_run = 0
    return max_run

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/week_02/day_01/01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_