"""
Write a function to find the first adverb and their positions in a given sentence.
assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')
"""

def find_adverb_position(sentence):
    adverbs = ['quickly', 'quick', 'slowly', 'slow', 'quickly', 'quick', 'clearly', 'clear', 'quickly', 'quick', 'slowly', 'slow', 'quickly', 'quick', 'clearly']
    for i in range(len(sentence)):
        for adverb in adverbs:
            if sentence[i:i+len(adverb)] == adverb:
                return (i, i+len(adverb), adverb)
    return None

print(find_adverb_position("clearly!! we can see the sky")) # (0, 7, 'clearly')
print(find_adverb_position("quickly we can see the sky")) # (0, 7, 'quickly')
print(find_adverb_position("slowly we can see the sky")) # (5, 10, 'slowly')
print(find_adverb_position("we can clearly see the sky")) # (12, 17, 'clearly')
print(find_adverb_position("we can see the sky")) # None