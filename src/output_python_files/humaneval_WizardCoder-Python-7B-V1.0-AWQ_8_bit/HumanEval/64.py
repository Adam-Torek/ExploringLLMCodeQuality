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
    vowels = set("aeiouy")
    count = 0
    for char in s:
        if char.lower() in vowels:
            count += 1
    return count


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(vowels_count("abcde"))
    print(vowels_count("ACEDY"))
    print(vowels_count("hello"))
    print(vowels_count("world"))
    print(vowels_count("python"))
    print(vowels_count("programming"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count("programming language"))
    print(vowels_count