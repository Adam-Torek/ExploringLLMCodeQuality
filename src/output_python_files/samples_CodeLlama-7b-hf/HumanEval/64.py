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
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("a") == 1
    assert vowels_count("") == 0
    assert vowels_count("A") == 1
    assert vowels_count("Aa") == 2
    assert vowels_count("AaA") == 3
    assert vowels_count("AaAa") == 4
    assert vowels_count("AaAaA") == 5
    assert vowels_count("AaAaAa") == 6
    assert vowels_count("AaAaAaA") == 7
    assert vowels_count("AaAaAaAa") == 8
    assert vowels_count("AaAaAaAaA") == 9
    assert vowels_count("AaAaAaAaAa") == 10
    assert vowels_count("AaAaAaAaAaA") == 11
    assert vowels_count("AaAaAaAaAaAa") == 12
    assert vowels_count("AaAaAaAaAaAaA") == 13
    assert vowels_count("AaAaAaAaAaAaAa") == 14
    assert vowels_count("AaAaAaAaAaAaAaA") == 15
    assert vowels_count("AaAaAaAaAaAaAaAa") == 16
    assert vowels_count("AaAaAaAaAaAaAaAaA") == 17
    assert vowels_count("AaAaAaAaAaAaAaAaAa") == 18
    assert vowels_count("AaAaAaAaAaAaAaAaAaA") == 19
    assert vowels_count("AaAaAaAaAaAaAaAaAaAa") == 20
    assert vowels_count("AaAaAaAaAaAaAaAaAaAaA") == 21
    assert vowels_count("AaAaAaAaAaAaAaAaAaAaAa") == 22
    assert vowels_count("AaAaAaAaAaAaAaAaAaAaAaA") == 23
    assert vowels_count("AaAaAaAaAaAaAaAaAaAaAaAa") == 24
    assert vowels_count("AaAaAaAaAaAaAaAaAaAaAaAaA") == 25
    assert vowels_count("AaAaAaAaAaAaAaAaAaAaAaAaAa") == 26
    assert vowels_count("AaAaAaAaAaAaAaAaAaAaAaAaAaA") == 27
    assert