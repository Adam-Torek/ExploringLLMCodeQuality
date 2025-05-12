"""
Write a function to find the first adverb and their positions in a given sentence.
assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')
"""
import re

def find_adverb_position(sentence):
    """
    Find the first adverb and their positions in a given sentence.
    """
    pattern = r'\b\w+\b\s\w+\s\w+\.'
    match = re.search(pattern, sentence)
    if match:
        return match.start(), match.end(), match.group()
    else:
        return None


if __name__ == '__main__':
    sentence = "clearly!! we can see the sky"
    print(find_adverb_position(sentence))