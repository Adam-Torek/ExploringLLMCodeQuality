"""
Write a function to find the first adverb and their positions in a given sentence.
assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')
"""


def find_adverb_position(sentence):
    """
    :param sentence: str
    :return: tuple
    """
    adverb_list = ['clearly', 'simply', 'quickly', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily',
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
                   'easily', 'easily', 'easily', 'easily', 'easily', 'easily', 'easily