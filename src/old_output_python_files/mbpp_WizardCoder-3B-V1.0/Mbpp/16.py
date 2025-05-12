"""
Write a function to that returns true if the input string contains sequences of lowercase letters joined with an underscore and false otherwise.
assert text_lowercase_underscore("aab_cbbbc")==(True)
"""
def text_lowercase_underscore(text):
    if text.islower() and text.replace("_", "").islower():
        return True
    else:
        return False<|endoftext|>