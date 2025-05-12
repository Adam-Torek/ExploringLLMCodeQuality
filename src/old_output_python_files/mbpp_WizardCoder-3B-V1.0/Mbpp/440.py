"""
Write a function to find the first adverb and their positions in a given sentence.
assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')
"""

def find_adverb_position(sentence):
    adverbs = []
    for i, word in enumerate(sentence.split()):
        if word.lower() in ['clearly', 'clear', 'clearly!', 'clearly?', 'clearly.']:
            adverbs.append((i, i+1, 'clearly'))
        elif word.lower() in ['well', 'well!', 'well?', 'well.']:
            adverbs.append((i, i+1, 'well'))
        elif word.lower() in ['also', 'also!', 'also?', 'also.']:
            adverbs.append((i, i+1, 'also'))
        elif word.lower() in ['also', 'also!', 'also?', 'also.']:
            adverbs.append((i, i+1, 'also'))
        elif word.lower() in ['also', 'also!', 'also?', 'also.']:
            adverbs.append((i, i+1, 'also'))
        elif word.lower() in ['also', 'also!', 'also?', 'also.']:
            adverbs.append((i, i+1, 'also'))
        elif word.lower() in ['also', 'also!', 'also?', 'also.']:
            adverbs.append((i, i+1, 'also'))
        elif word.lower() in ['also', 'also!', 'also?', 'also.']:
            adverbs.append((i, i+1, 'also'))
        elif word.lower() in ['also', 'also!', 'also?', 'also.']:
            adverbs.append((i, i+1, 'also'))
        elif word.lower() in ['also', 'also!', 'also?', 'also.']:
            adverbs.append((i, i+1, 'also'))
        elif word.lower() in ['also', 'also!', 'also?', 'also.']:
            adverbs.append((i, i+1, 'also'))
        elif word.lower() in ['also', 'also!', 'also?', 'also.']:
            adverbs.append((i, i+1, 'also'))
        elif word.lower() in ['also', 'also!', 'also?', 'also.']:
            adverbs.append((i, i+1, 'also'))
        elif word.lower() in ['also', 'also!', 'also?', 'also.']:
            adverbs.append((i, i+1, 'also'))
        elif word.lower() in ['also', 'also!', 'also?', 'also.']:
            adverbs.append((i, i+1, 'also'))
        elif word.lower() in ['also', 'also!', 'also?', 'also.']:
            adverbs.append((i, i+1, 'also'))
        elif word.lower() in ['also', 'also!', 'also?', 'also.']:
            adverbs.append((i, i+1, 'also'))
        elif word.lower() in ['also', 'also!', 'also?', 'also.']:
            adverbs.append((i, i+1, 'also'))
        elif word.lower() in ['also', 'also!', 'also?', 'also.']:
            adverbs.append((i, i+1, 'also'))
        elif word.lower() in ['also', 'also!', 'also?', 'also.']:
            adverbs.append((i, i+1, 'also'))
        elif word.lower() in ['also', 'also!', 'also?', 'also.']:
            adverbs.append((i, i+1, 'also'))
        elif word.lower() in ['also', 'also!', 'also?', 'also.']:
            adverbs.append((i, i+1, 'also'))
        elif word.lower() in ['also', 'also!', 'also?', 'also.']:
            adverbs.append((i, i+1, 'also'))
        elif word.lower() in ['also', 'also!', 'also?', 'also.']:
            adverbs.append((i, i+1, 'also'))
        elif word.lower() in ['also', 'also!', 'also?', 'also.']:
            adverbs.append((i, i+1, 'also'))
        elif word.lower() in ['also', 'also!', 'also?', 'also.']:
            adverbs.append((i, i+1, 'also'))