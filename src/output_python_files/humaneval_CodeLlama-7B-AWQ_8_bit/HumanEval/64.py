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
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    count = 0
    for i in s:
        if i in vowels:
            count += 1
    return count


def test_vowels_count():
    """Test cases for vowels_count."""
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("A") == 1
    assert vowels_count("") == 0
    assert vowels_count("AaAaAaA") == 4
    assert vowels_count("AaAaAaAa") == 5
    assert vowels_count("AaAaAaAaA") == 6
    assert vowels_count("AaAaAaAaAa") == 7
    assert vowels_count("AaAaAaAaAaA") == 8
    assert vowels_count("AaAaAaAaAaAa") == 9
    assert vowels_count("AaAaAaAaAaAaA") == 10
    assert vowels_count("AaAaAaAaAaAaAa") == 11
    assert vowels_count("AaAaAaAaAaAaAaA") == 12
    assert vowels_count("AaAaAaAaAaAaAaAa") == 13
    assert vowels_count("AaAaAaAaAaAaAaAaA") == 14
    assert vowels_count("AaAaAaAaAaAaAaAaAa") == 15
    assert vowels_count("AaAaAaAaAaAaAaAaAaA") == 16
    assert vowels_count("AaAaAaAaAaAaAaAaAaAa") == 17
    assert vowels_count("AaAaAaAaAaAaAaAaAaAaA") == 18
    assert vowels_count("AaAaAaAaAaAaAaAaAaAaAa") == 19
    assert vowels_count("AaAaAaAaAaAaAaAaAaAaAaA") == 20
    assert vowels_count("AaAaAaAaAaAaAaAaAaAaAaAa") == 21
    assert vowels_count("AaAaAaAaAaAaAaAaAaAaAaAaA") == 22
    assert vowels_count("AaAaAaAaAaAaAaAaAaAaAaAaAa") == 23
    assert vowels_count("AaAaAaAaAaAaAaAaAaAaAaAaAaA") == 24
    assert vowels_count("AaAaAaAaAaAaAaAaAaAaAaAaAaAa") == 25
    assert vowels_count("AaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == 26
    assert vowels