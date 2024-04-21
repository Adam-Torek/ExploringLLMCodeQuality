"""
Write a function that matches a string that has an 'a' followed by anything, ending in 'b'.
assert text_starta_endb("aabbbb")
"""

def text_starta_endb(text):
    if text.startswith("a") and text.endswith("b"):
        return True
    else:
        return False

# Test the function
print(text_starta_endb("aabbbb")) # True
print(text_starta_endb("abbbba")) # False<|endoftext|>