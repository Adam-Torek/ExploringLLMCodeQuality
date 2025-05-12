"""
Write a function to reverse words seperated by spaces in a given string.
assert reverse_words("python program")==("program python")
"""
def reverse_words(string):
    """
    This function takes a string as an input and returns the reversed string
    where words are separated by spaces.
    """
    words = string.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words

# Test the function
string = "python program"
assert reverse_words(string) == "program python"