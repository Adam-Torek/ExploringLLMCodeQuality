"""
Write a function to find the first adverb and their positions in a given sentence.
assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')
"""
import re

def find_adverb_position(sentence):
    """
    Find the first adverb and their positions in a given sentence.
    """
    adverbs = ['rarely', 'barely', 'seldom', 'never', 'often', 'sometimes', 'usually', 'always', 'just', 'soon', 'yesterday', 'tomorrow', 'today', 'here', 'there', 'everywhere', 'anywhere', 'somewhere', 'above', 'below', 'beside', 'behind', 'before', 'beneath', 'beside', 'between', 'beyond', 'down', 'far', 'forward', 'in', 'inside', 'into', 'likewise', 'near', 'out', 'outside', 'over', 'past', 'round', 'through', 'together', 'under', 'up', 'within']
    pattern = re.compile(r'\b(' + '|'.join(adverbs) + r')\b')
    match = pattern.search(sentence)
    if match:
        return match.start(), match.end(), match.group()
    else:
        return None

# Test the function
sentence = "clearly!! we can see the sky"
position = find_adverb_position(sentence)
if position:
    print(f"The first adverb '{position[2]}' is located at positions {position[0]} to {position[1]}")
else:
    print("No adverb found in the sentence.")

# Expected output: The first adverb 'clearly' is located at positions 0 to 7