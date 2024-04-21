"""
Write a function to find maximum run of uppercase characters in the given string.
assert max_run_uppercase('GeMKSForGERksISBESt') == 5
"""
def max_run_uppercase(string):
    """
    :param string: string
    :return: int
    """
    if len(string) == 0:
        return 0
    max_run = 1
    current_run = 1
    current_char = string[0]
    for char in string[1:]:
        if char.isupper() and current_char.islower():
            current_run = 1
            current_char = char
        elif char.isupper():
            current_run += 1
            max_run = max(max_run, current_run)
        elif char.islower():
            current_run = 1
    return max_run

if __name__ == "__main__":
    assert max_run_uppercase('GeMKSForGERksISBESt') == 5
    assert max_run_uppercase('') == 0
    assert max_run_uppercase('abc') == 0
    assert max_run_uppercase('ABC') == 1
    assert max_run_uppercase('ABCABC') == 2
    assert max_run_uppercase('ABCABCABC') == 3
    assert max_run_uppercase('ABCABCABCABC') == 4
    assert max_run_uppercase('ABCABCABCABCABC') == 5
    assert max_run_uppercase('ABCABCABCABCABCABC') == 5
    assert max_run_uppercase('ABCABCABCABCABCABCABC') == 5
    assert max_run_uppercase('ABCABCABCABCABCABCABCABC') == 5
    assert max_run_uppercase('ABCABCABCABCABCABCABCABCABC') == 5
    assert max_run_uppercase('ABCABCABCABCABCABCABCABCABCABC') == 5
    assert max_run_uppercase('ABCABCABCABCABCABCABCABCABCABCABC') == 5
    assert max_run_uppercase('ABCABCABCABCABCABCABCABCABCABCABCABC') == 5
    assert max_run_uppercase('ABCABCABCABCABCABCABCABCABCABCABCABC') == 5
    assert max_run_uppercase('ABCABCABCABCABCABCABCABCABCABCABCABC') == 5
    assert max_run_uppercase('ABCABCABCABCABCABCABCABCABCABCABCABC') == 5
    assert max_run_uppercase('ABCABCABCABCABCABCABCABCABCABCABCABC') == 5
    assert max_run_uppercase('ABCABCABCABCABCABCABCABCABCABCABCABC') == 5
    assert max_run_uppercase('ABCABCABCABCABCABCABCABCABCABCABCABC') == 5
    assert max_run_uppercase('ABCABCABCABCABCABCABCABCABCABCABCABC') == 5
    assert max_run_uppercase('ABCABCABCABCABCABCABCABCABCABCABCABC') == 5
    assert max_run_uppercase('ABCABCABCABCABCABCABCABCABCABCABCABC') == 5
    assert max_run_uppercase('ABCABCABCABCABCABCABCABCABCABCABCABC') == 5
    assert max_run_uppercase('ABCABCABCABCABCABCABCABCABCABCABCABC') == 5
    assert max_run_uppercase