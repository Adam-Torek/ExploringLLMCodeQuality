"""
Write a function to put spaces between words starting with capital letters in a given string.
assert capital_words_spaces("Python") == 'Python'
"""


def capital_words_spaces(string):
    """
    Write a function to put spaces between words starting with capital letters in a given string.
    assert capital_words_spaces("Python") == 'Python'
    """
    words = string.split()
    new_words = []
    for word in words:
        if word[0].isupper():
            new_words.append(word[0] + ' ' + word[1:])
        else:
            new_words.append(word)
    return ' '.join(new_words)


if __name__ == '__main__':
    print(capital_words_spaces("Python"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming language"))
    print(capital_words_spaces("Python is a programming