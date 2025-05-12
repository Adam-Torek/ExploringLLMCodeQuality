"""
Write a function that checks if a strings contains 'z', except at the start and end of the word.
assert text_match_wordz_middle("pythonzabc.")==True
"""


def text_match_wordz_middle(text):
    """
    :param text: str
    :return: bool
    """
    if text.startswith("z") and text.endswith("z"):
        return True
    else:
        return False


if __name__ == '__main__':
    print(text_match_wordz_middle("pythonzabc."))
    print(text_match_wordz_middle("zpythonzabc."))
    print(text_match_wordz_middle("pythonzabc.z"))
    print(text_match_wordz_middle("pythonzabc.z."))
    print(text_match_wordz_middle("pythonzabc.z.z"))
    print(text_match_wordz_middle("pythonzabc.z.z.z"))
    print(text_match_wordz_middle("pythonzabc.z.z.z.z"))
    print(text_match_wordz_middle("pythonzabc.z.z.z.z.z"))
    print(text_match_wordz_middle("pythonzabc.z.z.z.z.z.z"))
    print(text_match_wordz_middle("pythonzabc.z.z.z.z.z.z.z"))
    print(text_match_wordz_middle("pythonzabc.z.z.z.z.z.z.z.z"))
    print(text_match_wordz_middle("pythonzabc.z.z.z.z.z.z.z.z.z"))
    print(text_match_wordz_middle("pythonzabc.z.z.z.z.z.z.z.z.z.z"))
    print(text_match_wordz_middle("pythonzabc.z.z.z.z.z.z.z.z.z.z.z"))
    print(text_match_wordz_middle("pythonzabc.z.z.z.z.z.z.z.z.z.z.z.z"))
    print(text_match_wordz_middle("pythonzabc.z.z.z.z.z.z.z.z.z.z.z.z.z"))
    print(text_match_wordz_middle("pythonzabc.z.z.z.z.z.z.z.z.z.z.z.z.z.z"))
    print(text_match_wordz_middle("pythonzabc.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z"))
    print(text_match_wordz_middle("pythonzabc.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z"))
    print(text_match_wordz_middle("pythonzabc.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z"))
    print(text_match_wordz_middle("pythonzabc.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z"))
    print(text_match_wordz_middle("pythonzabc.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z"))
    print(text_match_wordz_middle("pythonzabc.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z"))
    print(text_match_wordz_middle("pythonzabc.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z"))
    print(text_match_wordz_middle("pythonzabc.z.z.z.z.