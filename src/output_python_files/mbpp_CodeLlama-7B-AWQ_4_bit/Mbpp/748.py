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
    for i in range(len(words)):
        if words[i][0].isupper():
            words[i] = ' ' + words[i]
    return ''.join(words)


if __name__ == '__main__':
    print(capital_words_spaces("Python"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print(capital_words_spaces("Python is a great language"))
    print