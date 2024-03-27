"""
Write a function that matches a string that has an a followed by three 'b'.
assert not text_match_three("ac")
"""

def text_match_three(text):
    return text.startswith("a") and text.endswith("bbb")

# Test cases
assert not text_match_three("ac")
assert text_match_three("abc")
assert text_match_three("abbb")
assert text_match_three("abbbb")
assert not text_match_three("ab")
assert not text_match_three("abbbbbb")<|endoftext|>