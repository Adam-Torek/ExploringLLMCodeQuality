def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """

def mini_roman_to_int(roman):
    """
    Given a roman numeral string, return its integer equivalent.
    Restrictions: roman is a string of lowercase letters.

    Examples:
    >>> mini_roman_to_int('xix') == 19
    >>> mini_roman_to_int('clii') == 152
    >>> mini_roman_to_int('cdxxvi') == 426
    """

def main():
    """
    The main function for this program.
    """
    pass

if __name__ == '__main__':
    main()
/README.md
# Python-Practice

This is a repository for my Python practice.

## Contents

### 1. [Roman Numerals](https://github.com/joshua-chang/Python-Practice/tree/master/Roman%20Numerals)

This is a program that converts between Roman numerals and integers.

### 2. [Tic-Tac-Toe](https://github.com/joshua-chang/Python-Practice/tree/master/Tic-Tac-Toe)

This is a program that plays Tic-Tac-Toe.

### 3. [Word Count](https://github.com/joshua-chang/Python-Practice/tree/master/Word%20Count)

This is a program that counts the number of words in a text file.

### 4. [Word Frequency](https://github.com/joshua-chang/Python-Practice/tree/master/Word%20Frequency)

This is a program that counts the number of times each word appears in a text file.
/Word Count/word_count.py
"""
This is a program that counts the number of words in a text file.
"""

def word_count(filename):
    """
    Given a filename, return the number of words in the file.
    Restrictions: filename is a string.

    Examples:
    >>> word_count('example.txt') == 10
    """

def main():
    """
    The main function for this program.
    """
    pass

if __name__ == '__main__':
    main()
/Word Frequency/word_frequency.py
"""
This is a program that counts the number of times each word appears in a text file.
"""

def word_frequency(filename):
    """
    Given a filename, return a dictionary mapping each word to the number of times
    it appears in the file.
    Restrictions: filename is a string.

    Examples:
    >>> word_frequency('example.txt') == {'the': 2, 'cat': 1,'sat': 1, 'on': 1,'mat': 1}
    """

def main():
    """
    The main function for this program.
    """
    pass

if __name__ == '__main__':
    main()
/Tic-Tac-Toe/tic_tac_toe.py
"""
This is a program that plays Tic-Tac-Toe.
"""

def print_board(board):
    """