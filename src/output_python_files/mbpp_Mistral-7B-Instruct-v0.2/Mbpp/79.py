"""
Write a python function to check whether the length of the word is odd or not.
assert word_len("Hadoop") == False
"""
def word_len(word):
    """
    This function takes a single argument which is a string and returns a boolean value indicating whether the length of the string is odd or not.
    """
    return len(word) % 2 != 0