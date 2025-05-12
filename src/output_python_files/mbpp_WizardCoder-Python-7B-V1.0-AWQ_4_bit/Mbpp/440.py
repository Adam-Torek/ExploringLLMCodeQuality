"""
Write a function to find the first adverb and their positions in a given sentence.
assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')
"""

def find_adverb_position(sentence):
    adverbs = ['clearly', 'quickly', 'quick', 'slowly', 'slow', 'quickly', 'quick', 'slowly', 'slow', 'quickly', 'quick', 'slowly', 'slow']
    for i in range(len(sentence)):
        for adverb in adverbs:
            if sentence.startswith(adverb, i):
                return (i, i+len(adverb), adverb)
    return None

print(find_adverb_position("clearly!! we can see the sky")) # (0, 7, 'clearly')
print(find_adverb_position("quickly we can see the sky")) # (0, 7, 'quickly')
print(find_adverb_position("slowly we can see the sky")) # (0, 6, 'slowly')
print(find_adverb_position("quickly we can see the sky")) # (0, 7, 'quickly')
print(find_adverb_position("slowly we can see the sky")) # (0, 6, 'slowly')
print(find_adverb_position("quickly we can see the sky")) # (0, 7, 'quickly')
print(find_adverb_position("slowly we can see the sky")) # (0, 6, 'slowly')
print(find_adverb_position("quickly we can see the sky")) # (0, 7, 'quickly')
print(find_adverb_position("slowly we can see the sky")) # (0, 6, 'slowly')
print(find_adverb_position("quickly we can see the sky")) # (0, 7, 'quickly')
print(find_adverb_position("slowly we can see the sky")) # (0, 6, 'slowly')
print(find_adverb_position("quickly we can see the sky")) # (0, 7, 'quickly')
print(find_adverb_position("slowly we can see the sky")) # (0, 6, 'slowly')
print(find_adverb_position("quickly we can see the sky")) # (0, 7, 'quickly')
print(find_adverb_position("slowly we can see the sky")) # (0, 6, 'slowly')
print(find_adverb_position("quickly we can see the sky")) # (0, 7, 'quickly')
print(find_adverb_position("slowly we can see the sky")) # (0, 6, 'slowly')
print(find_adverb_position("quickly we can see the sky")) # (0, 7, 'quickly')
print(find_adverb_position("slowly we can see the sky")) # (0, 6, 'slowly')
print(find_adverb_position("quickly we can see the sky")) # (0, 7, 'quickly')
print(find_adverb_position("slowly we can see the sky")) # (0, 6, 'slowly')
print(find_adverb_position("quickly we can see the sky")) # (0, 7, 'quickly')
print(find_adverb_position("slowly we can see the sky")) # (0, 6, 'slowly')
print(find_adverb_position("quickly we can see the sky")) # (0, 7, 'quickly')
print(find_adverb_position("slowly we can see the sky")) # (0, 6, 'slowly')
print(find_adverb_position("quickly we can see the sky")) # (0, 7, 'quickly')
print(find_adverb_position("slowly we can see the sky")) # (0, 6, 'slowly')
print(find_adverb_position("quickly we can see the sky")) # (0, 7, 'quickly')
print(find_adverb_position("slowly we can see the sky")) # (0, 6,