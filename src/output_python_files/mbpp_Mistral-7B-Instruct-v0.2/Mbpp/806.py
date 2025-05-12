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
        if char.isupper() and current_char.isupper():
            current_run += 1
            if current_run > max_run:
                max_run = current_run
        elif char.isupper():
            current_run = 1
            current_char = char
    return max_run

if __name__ == "__main__":
    assert max_run_uppercase('GeMKSForGERksISBESt') == 5
    assert max_run_uppercase('') == 0
    assert max_run_uppercase('aBc') == 1
    assert max_run_uppercase('ABC') == 3
    assert max_run_uppercase('123') == 0
    assert max_run_uppercase('1A1B1C1') == 2
    assert max_run_uppercase('1A1B1C1A1B1C1') == 3
    assert max_run_uppercase('1A1B1C1A1B1C1A1B1C1') == 4
    assert max_run_uppercase('1A1B1C1A1B1C1A1B1C1A1B1C1') == 5
    assert max_run_uppercase('1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1') == 6
    assert max_run_uppercase('1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1') == 14
    assert max_run_uppercase('1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B1C1A1B