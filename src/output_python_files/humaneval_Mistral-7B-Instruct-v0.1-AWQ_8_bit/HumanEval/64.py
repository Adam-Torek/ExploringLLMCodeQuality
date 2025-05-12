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
    vowels = "aeiouAEIOUY"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def test_vowels_count():
    """Test cases for vowels_count function."""
    assert vowels_count("") == 0
    assert vowels_count("a") == 1
    assert vowels_count("hello") == 2
    assert vowels_count("world") == 2
    assert vowels_count("acd") == 1
    assert vowels_count("acde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("YOU") == 2
    assert vowels_count("pypi") == 2
    assert vowels_count("PyPI") == 2
    assert vowels_count("pYPi") == 2
    assert vowels_count("pYpI") == 2
    assert vowels_count("pYPi") == 2
    assert vowels_count("pYpI") == 2
    assert vowels_count("pYPi") == 2
    assert vowels_count("pYpI") == 2
    assert vowels_count("pYPi") == 2
    assert vowels_count("pYpI") == 2
    assert vowels_count("pYPi") == 2
    assert vowels_count("pYpI") == 2
    assert vowels_count("pYPi") == 2
    assert vowels_count("pYpI") == 2
    assert vowels_count("pYPi") == 2
    assert vowels_count("pYpI") == 2
    assert vowels_count("pYPi") == 2
    assert vowels_count("pYpI") == 2
    assert vowels_count("pYPi") == 2
    assert vowels_count("pYpI") == 2
    assert vowels_count("pYPi") == 2
    assert vowels_count("pYpI") == 2
    assert vowels_count("pYPi") == 2
    assert vowels_count("pYpI") == 2
    assert vowels_count("pYPi") == 2
    assert vowels_count("pYpI") == 2
    assert vowels_count("pYPi") == 2
    assert vowels_count("pYpI") == 2
    assert vowels_count("pYPi") == 2
    assert vowels_count("pYpI") == 2
    assert vowels_count("pYPi") == 2
    assert vowels_count("pYpI") == 2
    assert vowels_count("pYPi") == 2
    assert vowels_count("pYpI") == 2
    assert vowels_count("pYPi") == 2
    assert vowels_count("pYpI") == 2
    assert vowels_count("pYPi") == 2
    assert vowels_count("pYpI") == 2
    assert vowels_count("pYPi") == 2
    assert vowels_count("pYpI") == 2
    assert vowels_count("pYPi") == 2
    assert vowels_count("pYpI