"""
Write a function to put spaces between words starting with capital letters in a given string.
assert capital_words_spaces("Python") == 'Python'
"""
def capital_words_spaces(string):
    """
    Function to put spaces between words starting with capital letters in a given string.
    :param string: string to be processed
    :return: string with spaces between words starting with capital letters
    """
    words = string.split()
    result = []
    for word in words:
        if word and word[0].isupper():
            result.append(word.capitalize())
            result.append(" ")
        else:
            result.append(word)
    return "".join(result)

# Test cases
assert capital_words_spaces("Python") == "Python"
assert capital_words_spaces("JavaScript") == "JavaScript"
assert capital_words_spaces("ThisIsAString") == "This Is A String"
assert capital_words_spaces("") == ""
assert capital_words_spaces("hello world") == "hello world"
assert capital_words_spaces("12345") == "12345"
assert capital_words_spaces("12345 Hello World") == "12345 Hello World"
assert capital_words_spaces("12345 Hello World 12345") == "12345 Hello World 12345"
assert capital_words_spaces("12345 Hello World 12345 Hello World") == "12345 Hello World 12345 Hello World"</s>