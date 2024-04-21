"""
Write a python function to check whether the length of the word is odd or not.
assert word_len("Hadoop") == False
"""

def word_len(word):
    if len(word) % 2 == 0:
        return False
    else:
        return True<|endoftext|>