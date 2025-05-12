"""
Write a function that matches a string that has an a followed by three 'b'.
assert not text_match_three("ac")
"""
import re


def text_match_three(text: str):
    pattern = r"a(.{0,1}b{3})?"
    match = re.search(pattern, text)
    if match:
        return True
    else:
        return False


if __name__ == "__main__":
    assert not text_match_three("ac")
    assert text_match_three("abbbb")
    assert text_match_three("abbbba")
    assert text_match_three("abbbbbb")
    assert text_match_three("abbbbbbbb")
    assert text_match_three("abbbbbbbbbb")
    assert text_match_three("abbbbbbbbbbbb")
    assert text_match_three("abbbbbbbbbbbbbb")
    assert text_match_three("abbbbbbbbbbbbbbb")
    assert text_match_three("abbbbbbbbbbbbbbbb")
    assert text_match_three("abbbbbbbbbbbbbbbbb")
    assert text_match_three("abbbbbbbbbbbbbbbbbb")
    assert text_match_three("abbbbbbbbbbbbbbbbbbb")
    assert text_match_three("abbbbbbbbbbbbbbbbbbbb")
    assert text_match_three("abbbbbbbbbbbbbbbbbbbbb")
    assert text_match_three("abbbbbbbbbbbbbbbbbbbbbb")
    assert text_match_three("abbbbbbbbbbbbbbbbbbbbbbb")
    assert text_match_three("abbbbbbbbbbbbbbbbbbbbbbbb")
    assert text_match_three("abbbbbbbbbbbbbbbbbbbbbbbbb")
    assert text_match_three("abbbbbbbbbbbbbbbbbbbbbbbbbb")
    assert text_match_three("abbbbbbbbbbbbbbbbbbbbbbbbbbb")
    assert text_match_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbb")
    assert text_match_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
    assert text_match_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
    assert text_match_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
    assert text_match_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
    assert text_match_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
    assert text_match_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
    assert text_match_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
    assert text_match_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
    assert text_match_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
    assert text_match_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
    assert text_match_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
    assert text_match_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
    assert text_match_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
    assert text_match_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
    assert text_match_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
    assert text_match_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
    assert text_match_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb