FIX = """
Add more test cases.
"""

def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    count = 0
    for char in s:
        if char.lower() in vowels:
            count += 1
        elif char.lower() == 'y' and s[-1] == char:
            count += 1
    return count

def test_vowels_count():
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("Python") == 2
    assert vowels_count("Hello") == 2
    assert vowels_count("World") == 2
    assert vowels_count("PythonWorld") == 5
    assert vowels_count("PythonWorldY") == 6
    assert vowels_count("PythonWorldYe") == 7
    assert vowels_count("PythonWorldYeah") == 8
    assert vowels_count("PythonWorldYea") == 7
    assert vowels_count("PythonWorldYea!") == 7
    assert vowels_count("PythonWorldYeah!") == 8
    assert vowels_count("PythonWorldYeah!Y") == 9
    assert vowels_count("PythonWorldYeah!Ye") == 10
    assert vowels_count("PythonWorldYeah!Yea") == 11
    assert vowels_count("PythonWorldYeah!Yea!") == 12
    assert vowels_count("PythonWorldYeah!Yea!Y") == 13
    assert vowels_count("PythonWorldYeah!Yea!Ye") == 14
    assert vowels_count("PythonWorldYeah!Yea!Yea") == 15
    assert vowels_count("PythonWorldYeah!Yea!Yea!") == 16
    assert vowels_count("PythonWorldYeah!Yea!Yea!Y") == 17
    assert vowels_count("PythonWorldYeah!Yea!Yea!Ye") == 18
    assert vowels_count("PythonWorldYeah!Yea!Yea!Yea") == 19
    assert vowels_count("PythonWorldYeah!Yea!Yea!Yea!") == 20
    assert vowels_count("PythonWorldYeah!Yea!Yea!Yea!Y") == 21
    assert vowels_count("PythonWorldYeah!Yea!Yea!Yea!Ye") == 22
    assert vowels_count("PythonWorldYeah!Yea!Yea!Yea!Yea") == 23
    assert vowels_count("PythonWorldYeah!Yea!Yea!Yea!Yea!") == 24
    assert vowels_count("PythonWorldYeah!Yea!Yea!Yea!Yea!Y") == 25
    assert vowels_count("PythonWorldYeah!Yea!Yea!Yea!Y