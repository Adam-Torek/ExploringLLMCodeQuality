"""
Write a python function to check whether the length of the word is odd or not.
assert word_len("Hadoop") == False
"""

def word_len(word):
    if len(word) % 2 == 0:
        return False
    else:
        return True

# Test cases
assert word_len("Hadoop") == False
assert word_len("Python") == False
assert word_len("Java") == False
assert word_len("C++") == False
assert word_len("Dart") == True
assert word_len("Ruby") == True
assert word_len("Swift") == True