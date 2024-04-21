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
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in s:
        if i in vowels:
            count += 1
    return count


def test_vowels_count():
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("a") == 1
    assert vowels_count("A") == 1
    assert vowels_count("") == 0
    assert vowels_count("y") == 1
    assert vowels_count("Y") == 1
    assert vowels_count("Yy") == 2
    assert vowels_count("YyY") == 3
    assert vowels_count("YyYy") == 4
    assert vowels_count("YyYyY") == 5
    assert vowels_count("YyYyYy") == 6
    assert vowels_count("YyYyYyY") == 7
    assert vowels_count("YyYyYyYy") == 8
    assert vowels_count("YyYyYyYyY") == 9
    assert vowels_count("YyYyYyYyYy") == 10
    assert vowels_count("YyYyYyYyYyY") == 11
    assert vowels_count("YyYyYyYyYyYy") == 12
    assert vowels_count("YyYyYyYyYyYyY") == 13
    assert vowels_count("YyYyYyYyYyYyYy") == 14
    assert vowels_count("YyYyYyYyYyYyYyY") == 15
    assert vowels_count("YyYyYyYyYyYyYyYy") == 16
    assert vowels_count("YyYyYyYyYyYyYyYyY") == 17
    assert vowels_count("YyYyYyYyYyYyYyYyYy") == 18
    assert vowels_count("YyYyYyYyYyYyYyYyYyY") == 19
    assert vowels_count("YyYyYyYyYyYyYyYyYyYy") == 20
    assert vowels_count("YyYyYyYyYyYyYyYyYyYyY") == 21
    assert vowels_count("YyYyYyYyYyYyYyYyYyYyYy") == 22
    assert vowels_count("YyYyYyYyYyYyYyYyYyYyYyY") == 23
    assert vowels_count("YyYyYyYyYyYyYyYyYyYyYyYy") == 24
    assert vowels_count("YyYyYyYyYyYyYyYyYyYyYyYyY") == 25
    assert vowels_count("YyYyYyYyYyYyYyYyYyYyYyYyYy") == 26
    assert vowels_count("YyYyYyYyY