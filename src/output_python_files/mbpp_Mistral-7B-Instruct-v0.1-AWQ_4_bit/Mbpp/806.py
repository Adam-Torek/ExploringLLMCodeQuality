"""
Write a function to find maximum run of uppercase characters in the given string.
assert max_run_uppercase('GeMKSForGERksISBESt') == 5
"""

def max_run_uppercase(string):
    """
    Find maximum run of uppercase characters in the given string.
    """
    max_run = 0
    for i in range(len(string)):
        if string[i] == string[i+1] and string[i].isupper():
            max_run += 1
        else:
            max_run = 0
    return max_run

# assert max_run_uppercase('GeMKSForGERksISBESt') == 5
# assert max_run_uppercase('GeMKSForGERksISBESt') == 5
# assert max_run_uppercase('GeMKSForGERksISBESt') == 5
# assert max_run_uppercase('GeMKSForGERksISBESt') == 5
# assert max_run_uppercase('GeMKSForGERksISBESt') == 5
# assert max_run_uppercase('GeMKSForGERksISBESt') == 5
# assert max_run_uppercase('GeMKSForGERksISBESt') == 5
# assert max_run_uppercase('GeMKSForGERksISBESt') == 5
# assert max_run_uppercase('GeMKSForGERksISBESt') == 5
# assert max_run_uppercase('GeMKSForGERksISBESt') == 5
# assert max_run_uppercase('GeMKSForGERksISBESt') == 5
# assert max_run_uppercase('GeMKSForGERksISBESt') == 5
# assert max_run_uppercase('GeMKSForGERksISBESt') == 5
# assert max_run_uppercase('GeMKSForGERksISBESt') == 5
# assert max_run_uppercase('GeMKSForGERksISBESt') == 5
# assert max_run_uppercase('GeMKSForGERksISBESt') == 5
# assert max_run_uppercase('GeMKSForGERksISBESt') == 5
# assert max_run_uppercase('GeMKSForGERksISBESt') == 5
# assert max_run_uppercase('GeMKSForGERksISBESt') == 5
# assert max_run_uppercase('GeMKSForGERksISBESt') == 5
# assert max_run_uppercase('GeMKSForGERksISBESt') == 5
# assert max_run_uppercase('GeMKSForGERksISBESt') == 5
# assert max_run_uppercase('GeMKSForGERksISBESt') == 5
# assert max_run_uppercase('GeMKSForGERksISBESt') == 5
# assert max_run_uppercase('GeMKSForGERksISBESt') == 5
# assert max_run_uppercase('GeMKSForGERksISBESt') == 5
# assert max_run_uppercase('GeMKSForGERksISBESt') == 5
# assert max_run_uppercase('GeMKSForGERksISBESt') == 5
# assert max_run_uppercase('GeMKSForGERksISBESt') == 5
# assert max_run_uppercase('GeMKSForGERksISBESt') == 5
# assert max_run_uppercase('GeMKSForGERksISBESt') == 5
# assert max_run_uppercase('GeMKSForGERksISBESt') == 5
# assert max_run_uppercase('GeMKSForGERksISBESt') == 5
# assert max_run_uppercase('GeMKSForGERksISBESt') == 5
# assert max_run_uppercase('GeMKSForGERksISBESt') == 5
# assert max_run_uppercase('GeMKSForGERksISBESt') == 5
# assert max_run_uppercase('GeMKSForGERksISBESt