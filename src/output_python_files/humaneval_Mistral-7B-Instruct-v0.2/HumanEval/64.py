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
    vowels = "aeiouAEIOUy"
    return sum(1 for char in s if char in vowels)

def test_vowels_count():
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("Apple") == 3
    assert vowels_count("banana") == 5
    assert vowels_count("Python") == 3
    assert vowels_count("Hello") == 3
    assert vowels_count("Elephant") == 4
    assert vowels_count("") == 0
    assert vowels_count("12345") == 0
    assert vowels_count("12345a") == 1
    assert vowels_count("a12345") == 1
    assert vowels_count("Apple pie") == 5
    assert vowels_count("Apple pie with cherries") == 8
    assert vowels_count("Apple pie with cherries and cream") == 11
    assert vowels_count("Apple pie with cherries and cream on a plate") == 15
    assert vowels_count("Apple pie with cherries and cream on a plate in the kitchen") == 19
    assert vowels_count("Apple pie with cherries and cream on a plate in the kitchen in Paris") == 23
    assert vowels_count("Apple pie with cherries and cream on a plate in the kitchen in Paris France") == 27
    assert vowels_count("Apple pie with cherries and cream on a plate in the kitchen in Paris France during the summer") == 32
    assert vowels_count("Apple pie with cherries and cream on a plate in the kitchen in Paris France during the summer of 2018") == 36
    assert vowels_count("Apple pie with cherries and cream on a plate in the kitchen in Paris France during the summer of 2018 in the morning") == 40
    assert vowels_count("Apple pie with cherries and cream on a plate in the kitchen in Paris France during the summer of 2018 in the morning at 10:30") == 43
    assert vowels_count("Apple pie with cherries and cream on a plate in the kitchen in Paris France during the summer of 2018 in the morning at 10:30 am") == 46
    assert vowels_count("Apple pie with cherries and cream on a plate in the kitchen in Paris France during the summer of 2018 in the morning at 10:30 am ET") == 49
    assert vowels_count("Apple pie with cherries and cream on a plate in the kitchen in Paris France during the summer of 2018 in the morning at 10:30 am ET in the USA") == 52
    assert vowels_count("Apple pie with cherries and cream on a plate in the kitchen in Paris France during the summer of 2018 in the morning at 10:30 am ET in the USA E