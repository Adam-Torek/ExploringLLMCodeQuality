"""
Write a function that matches a word containing 'z'.
assert text_match_wordz("pythonz.")==True
"""


def text_match_wordz(text):
    """
    :param text: str
    :return: bool
    """
    return 'z' in text


if __name__ == '__main__':
    print("Example:")
    print(text_match_wordz("pythonz."))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert text_match_wordz("pythonz.") == True
    assert text_match_wordz("python.") == False
    assert text_match_wordz("pythonz") == False
    assert text_match_wordz("pythonz!") == False
    assert text_match_wordz("pythonz?") == False
    assert text_match_wordz("pythonz:") == False
    assert text_match_wordz("pythonz;") == False
    assert text_match_wordz("pythonz]") == False
    assert text_match_wordz("pythonz[") == False
    assert text_match_wordz("pythonz}") == False
    assert text_match_wordz("pythonz{") == False
    assert text_match_wordz("pythonz=") == False
    assert text_match_wordz("pythonz<") == False
    assert text_match_wordz("pythonz>") == False
    assert text_match_wordz("pythonz(") == False
    assert text_match_wordz("pythonz)") == False
    assert text_match_wordz("pythonz*") == False
    assert text_match_wordz("pythonz+") == False
    assert text_match_wordz("pythonz-") == False
    assert text_match_wordz("pythonz/") == False
    assert text_match_wordz("pythonz\\") == False
    assert text_match_wordz("pythonz|") == False
    assert text_match_wordz("pythonz%") == False
    assert text_match_wordz("pythonz$") == False
    assert text_match_wordz("pythonz#") == False
    assert text_match_wordz("pythonz'") == False
    assert text_match_wordz("pythonz\"") == False
    assert text_match_wordz("pythonz`") == False
    assert text_match_wordz("pythonz~") == False
    assert text_match_wordz("pythonz!") == False
    assert text_match_wordz("pythonz?") == False
    assert text_match_wordz("pythonz:") == False
    assert text_match_wordz("pythonz;") == False
    assert text_match_wordz("pythonz]") == False
    assert text_match_wordz("pythonz[") == False
    assert text_match_wordz("pythonz}") == False
    assert text_match_wordz("pythonz{") == False
    assert text_match_wordz("pythonz=") == False
    assert text_match_wordz("pythonz<") == False
    assert text_match_wordz("pythonz>") == False
    assert text_match_wordz("pythonz(") == False
    assert text_match_wordz("pythonz)") == False
    assert text_match_wordz("pythonz*") == False
    assert text_match_wordz("pythonz+") == False
    assert text_match_wordz("pythonz-") == False
    assert text_match_wordz("pythonz/") == False
    assert text_match_wordz("pythonz\\") == False
    assert text_match_wordz("pythonz|") == False
    assert text_match_wordz("pythonz%") == False
    assert text_match_wordz("pythonz$") == False
    assert text_match_wordz("pythonz#") == False
    assert text_match_wordz("pythonz'") == False
    assert text_match_wordz("pythonz\"") == False
    assert text_match_wordz("pythonz`") == False
    assert text_match_wordz("pythonz~") == False
    assert text_match_wordz("pythonz!") == False
    assert text_match_