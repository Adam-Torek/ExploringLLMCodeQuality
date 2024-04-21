"""
Write a function to find words that are longer than n characters from a given list of words.
assert long_words(3,"python is a programming language")==['python','programming','language']
"""
def long_words(n, string_of_words):
    """
    Function to find words longer than n characters from a given list of words.

    Parameters:
    n (int): Minimum length of words to be returned.
    string_of_words (str): A string containing multiple words separated by spaces.

    Returns:
    list: A list of words longer than n characters.
    """
    words = string_of_words.split()
    long_words = [word for word in words if len(word) > n]
    return long_words

# Test the function
assert long_words(3,"python is a programming language")==['python','programming','language']
assert long_words(5,"the quick brown fox jumps over the lazy dog")==['jumps','lazy']
assert long_words(1,"the quick brown fox jumps over the lazy dog")==[]</s>