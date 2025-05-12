"""
Write a function to find maximum run of uppercase characters in the given string.
assert max_run_uppercase('GeMKSForGERksISBESt') == 5
"""


def max_run_uppercase(string):
    """
    :param string: string
    :return: int
    """
    max_run = 0
    run = 0
    for i in range(len(string)):
        if string[i].isupper():
            run += 1
        else:
            if run > max_run:
                max_run = run
            run = 0
    if run > max_run:
        max_run = run
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
    print(max_run_uppercase('GeMKSForGERksISBE