"""
Write a function that matches a word containing 'z'.
assert text_match_wordz("pythonz.")==True
"""

def text_match_wordz(text):
    return "z" in text


def test_text_match_wordz():
    assert text_match_wordz("pythonz.")==True
    assert text_match_wordz("pythonz")==True
    assert text_match_wordz("pythonz.z")==True
    assert text_match_wordz("pythonz.z.z")==True
    assert text_match_wordz("pythonz.z.z.z")==True
    assert text_match_wordz("pythonz.z.z.z.z")==True
    assert text_match_wordz("pythonz.z.z.z.z.z")==True
    assert text_match_wordz("pythonz.z.z.z.z.z.z")==True
    assert text_match_wordz("pythonz.z.z.z.z.z.z.z")==True
    assert text_match_wordz("pythonz.z.z.z.z.z.z.z.z")==True
    assert text_match_wordz("pythonz.z.z.z.z.z.z.z.z.z")==True
    assert text_match_wordz("pythonz.z.z.z.z.z.z.z.z.z.z")==True
    assert text_match_wordz("pythonz.z.z.z.z.z.z.z.z.z.z.z")==True
    assert text_match_wordz("pythonz.z.z.z.z.z.z.z.z.z.z.z.z")==True
    assert text_match_wordz("pythonz.z.z.z.z.z.z.z.z.z.z.z.z.z")==True
    assert text_match_wordz("pythonz.z.z.z.z.z.z.z.z.z.z.z.z.z.z")==True
    assert text_match_wordz("pythonz.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z")==True
    assert text_match_wordz("pythonz.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z")==True
    assert text_match_wordz("pythonz.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z")==True
    assert text_match_wordz("pythonz.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z")==True
    assert text_match_wordz("pythonz.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z")==True
    assert text_match_wordz("pythonz.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z")==True
    assert text_match_wordz("pythonz.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z")==True
    assert text_match_wordz("pythonz.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z")==True
    assert text_match_wordz("pythonz.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.