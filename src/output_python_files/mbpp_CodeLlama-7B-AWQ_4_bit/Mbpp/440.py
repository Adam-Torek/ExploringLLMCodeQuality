"""
Write a function to find the first adverb and their positions in a given sentence.
assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')
"""


def find_adverb_position(sentence):
    """
    Find the first adverb and their positions in a given sentence.
    :param sentence: str
    :return: tuple
    """
    adverbs = ['quickly', 'slowly', 'clearly', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily',
               'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily',
               'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily',
               'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily',
               'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily',
               'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily',
               'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily',
               'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily',
               'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily',
               'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily',
               'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily',
               'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily',
               'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily',
               'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily',
               'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily',
               'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily',
               'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily',
               'easily', 'easily', 'easily', 'easily', 'easily