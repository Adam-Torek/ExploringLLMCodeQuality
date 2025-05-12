def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    sentences = S.split(".") + S.split("?") + S.split("!")
    return sum(1 for sentence in sentences if sentence.strip().startswith("I"))


if __name__ == "__main__":
    import doctest
    doctest.testmod()