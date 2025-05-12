"""
Write a function to find maximum run of uppercase characters in the given string.
assert max_run_uppercase('GeMKSForGERksISBESt') == 5
"""


def max_run_uppercase(string):
    """
    :param string: str
    :return: int
    """
    max_run = 0
    run = 0
    for char in string:
        if char.isupper():
            run += 1
        else:
            max_run = max(max_run, run)
            run = 0
    max_run = max(max_run, run)
    return max_run


if __name__ == '__main__':
    print(max_run_uppercase('GeMKSForGERksISBESt'))
    print(max_run_uppercase('GeMKSForGERksISBESt'))
    print(max_run_uppercase('GeMKSForGERksISBESt'))
    print(max_run_uppercase('GeMKSForGERksISBESt'))
    print(max_run_uppercase('GeMKSForGERksISBESt'))
    print(max_run_uppercase('GeMKSForGERksISBESt'))
    print(max_run_uppercase('GeMKSForGERksISBESt'))
    print(max_run_uppercase('GeMKSForGERksISBESt'))
    print(max_run_uppercase('GeMKSForGERksISBESt'))
    print(max_run_uppercase('GeMKSForGERksISBESt'))
    print(max_run_uppercase('GeMKSForGERksISBESt'))
    print(max_run_uppercase('GeMKSForGERksISBESt'))
    print(max_run_uppercase('GeMKSForGERksISBESt'))
    print(max_run_uppercase('GeMKSForGERksISBESt'))
    print(max_run_uppercase('GeMKSForGERksISBESt'))
    print(max_run_uppercase('GeMKSForGERksISBESt'))
    print(max_run_uppercase('GeMKSForGERksISBESt'))
    print(max_run_uppercase('GeMKSForGERksISBESt'))
    print(max_run_uppercase('GeMKSForGERksISBESt'))
    print(max_run_uppercase('GeMKSForGERksISBESt'))
    print(max_run_uppercase('GeMKSForGERksISBESt'))
    print(max_run_uppercase('GeMKSForGERksISBESt'))
    print(max_run_uppercase('GeMKSForGERksISBESt'))
    print(max_run_uppercase('GeMKSForGERksISBESt'))
    print(max_run_uppercase('GeMKSForGERksISBESt'))
    print(max_run_uppercase('GeMKSForGERksISBESt'))
    print(max_run_uppercase('GeMKSForGERksISBESt'))
    print(max_run_uppercase('GeMKSForGERksISBESt'))
    print(max_run_uppercase('GeMKSForGERksISBESt'))
    print(max_run_uppercase('GeMKSForGERksISBESt'))
    print(max_run_uppercase('GeMKSForGERksISBESt'))
    print(max_run_uppercase('GeMKSForGERksISBESt'))
    print(max_run_uppercase('GeMKSForGERksISBESt'))
    print(max_run_uppercase('GeMKSForGERksISBESt'))
    print(max_run_uppercase('GeMKSForGERksISBESt'))
    print(max_run_uppercase('GeMKSForGERksISBESt'))
    print(max_run_uppercase('GeMKSForGERksISBESt'))
    print(max_run_