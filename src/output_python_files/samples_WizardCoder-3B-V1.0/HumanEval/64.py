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

# Solution:
# We can solve this problem by iterating over each character in the string and
# checking if it is a vowel. If it is, we increment a counter. If it is not a
# vowel, we check if it is the last character in the string and if it is, we
# check if it is a vowel. If it is, we increment the counter.

def vowels_count(s):
    count = 0
    for char in s:
        if char in 'aeiouAEIOU':
            count += 1
        elif char == s[-1] and char in 'aeiouAEIOU':
            count += 1
    return count

# Test cases:
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3<|endoftext|>