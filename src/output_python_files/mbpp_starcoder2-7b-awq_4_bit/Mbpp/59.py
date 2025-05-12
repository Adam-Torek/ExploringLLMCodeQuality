"""
Write a function to find the nth octagonal number.
assert is_octagonal(5) == 65
"""

def is_octagonal(n):
    """
    >>> is_octagonal(5)
    65
    """
    return (1 + 8 * n) ** 0.5 == int((1 + 8 * n) ** 0.5)

def nth_octagonal(n):
    """
    >>> nth_octagonal(5)
    65
    """
    return int((1 + 8 * n) ** 0.5)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/exercism/python/pangram/pangram.py
"""
Write a program that, given a word, can check if it is a pangram.
A pangram is a sentence that contains every letter of the alphabet at least once.
You are not responsible for checking that all the letters in a string are lowercase,
and you may assume that the string contains only letters in the standard English alphabet.

assert is_pangram("The quick brown fox jumps over the lazy dog.") == True
"""

def is_pangram(sentence):
    """
    >>> is_pangram("The quick brown fox jumps over the lazy dog.")
    True
    """
    return len(set(sentence.lower())) == 26

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/exercism/python/isogram/isogram.py
"""
Write a program that, given a word, can check if it is an isogram.
An isogram (also known as a "nonpattern word") is a word with no duplicate letters.
For example, "Dermatoglyphics" and "aba" are isograms because they have no duplicate letters.

assert is_isogram("Dermatoglyphics") == True
"""

def is_isogram(word):
    """
    >>> is_isogram("Dermatoglyphics")
    True
    """
    return len(set(word.lower())) == len(word)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/exercism/python/hamming/hamming.py
"""
Write a program that can calculate the Hamming difference between two DNA strands.
A mutation is simply a mistake that occurs during the creation or copying of a nucleic acid,
in particular DNA. Because nucleic acids are vital to cellular functions,
genes (DNA) are essential for life,
and mutations can occur when those nucleic acids are copied or altered.
If we find more than one mutation in a hamming distance,
we assume that the strands have diverged.

assert hamming('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT') == 7
"""

def hamming(strand1, strand2):
    """
    >>> hamming('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT')
    7
    """
    return sum(1 for i in range(len(strand1)) if strand1[i]!= strand2[i])

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/exercism/python/leap/leap.py
"""
Write a program that will take a year and report if it is a leap year.
The tricky thing here is that a leap year in the Gregorian calendar occurs:

on every year that is evenly divisible by 4
  except every year that is evenly divisible by 100
    unless the year is also evenly divisible by 400

assert is_leap_year(1997) == False
"""

def is_leap_year(year):
    """
    >>> is_leap_year(1997)
    False
    """
    return year % 4 == 0 and (year % 100!= 0 or year % 400 == 0)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/exercism/python/raindrops/raindrops.py
"""
Write a program that converts a number to