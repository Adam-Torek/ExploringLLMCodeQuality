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
    vowels = "aeiouyAEIOUY"
    return sum(1 for char in s if char in vowels)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Test cases
assert vowels_count("") == 0
assert vowels_count("abcde") == 2
assert vowels_count("ACEDY") == 3
assert vowels_count("Apple") == 3
assert vowels_count("banana") == 5
assert vowels_count("Hello") == 3
assert vowels_count("Python") == 3
assert vowels_count("Elephant") == 4
assert vowels_count("QWERTY") == 1
assert vowels_count("12345") == 0
assert vowels_count("12345a") == 1
assert vowels_count("12345aB") == 2
assert vowels_count("12345aBC") == 3
assert vowels_count("12345aBCd") == 4
assert vowels_count("12345aBCde") == 5
assert vowels_count("12345aBCdef") == 6
assert vowels_count("12345aBCdefg") == 7
assert vowels_count("12345aBCdefgh") == 8
assert vowels_count("12345aBCdefghi") == 9
assert vowels_count("12345aBCdefghij") == 10
assert vowels_count("12345aBCdefghijk") == 11
assert vowels_count("12345aBCdefghijkl") == 12
assert vowels_count("12345aBCdefghijklm") == 13
assert vowels_count("12345aBCdefghijklmn") == 14
assert vowels_count("12345aBCdefghijklmno") == 15
assert vowels_count("12345aBCdefghijklmnop") == 16
assert vowels_count("12345aBCdefghijklmnoq") == 17
assert vowels_count("12345aBCdefghijklmnoqr") == 18
assert vowels_count("12345aBCdefghijklmnoqrs") == 19
assert vowels_count("12345aBCdefghijklmnoqrst") == 20
assert vowels_count("12345aBCdefghijklmnoqrstu") == 21
assert vowels_count("12345aBCdefghijklmnoqrstuv") == 22
assert vowels_count("12345aBCdefghijklmnoqrstuvw") == 23
assert vowels_count("12345aBCdefghijklmnoqrstuvwxy") == 24
assert vowels_count("12345aBCdefghijklmnoqrstuvwxyz") == 25
assert vowels_count("12345aBCdefghijklmnoqrstuvwxyzA") == 26
assert vowels_count("12345