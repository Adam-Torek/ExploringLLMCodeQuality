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
    boredom_count = 0
    for sentence in S.split('.'):
        if sentence.startswith('I'):
            boredom_count += 1
    return boredom_count


def main():
    """
    Test the is_bored function with some sample inputs.
    """
    for sample in [
            "I am bored",
            "I am not bored",
            "I am really bored",
            "I am so bored",
            "I am extremely bored",
            "I am absolutely bored",
            "I am totally bored",
            "I am completely bored",
            "I am utterly bored",
            "I am totally and completely bored",
            "I am totally and utterly bored",
            "I am totally and completely and utterly bored",
            "I am totally and completely and utterly and absolutely bored",
            "I am totally and completely and utterly and absolutely and completely bored",
            "I am totally and completely and utterly and absolutely and completely and utterly bored",
            "I am totally and completely and utterly and absolutely and completely and utterly and utterly bored",
            "I am totally and completely and utterly and absolutely and completely and utterly and utterly and completely bored",
            "I am totally and completely and utterly and absolutely and completely and utterly and utterly and completely and utterly bored",
            "I am totally and completely and utterly and absolutely and completely and utterly and utterly and completely and completely and utterly bored",
            "I am totally and completely and utterly and absolutely and completely and utterly and utterly and completely and completely and utterly bored",
            "I am totally and completely and utterly and absolutely and completely and utterly and utterly and completely and completely and utterly bored",
            "I am totally and completely and utterly and absolutely and completely and utterly and utterly and completely and completely and utterly bored",
            "I am totally and completely and utterly and absolutely and completely and utterly and utterly and completely and completely and utterly bored",
            "I am totally and completely and utterly and absolutely and completely and utterly and utterly and completely and completely and utterly bored",
            "I am totally and completely and utterly and absolutely and completely and utterly and utterly and completely and completely and utterly bored",
            "I am totally and completely and utterly and absolutely and completely and utterly and utterly and completely and completely and utterly bored",
            "I am totally and completely and utterly and absolutely and completely and utterly and utterly and completely and completely and utterly bored",
            "I am totally and completely and utterly and absolutely and completely and utterly and utterly and completely and completely and utterly bored",
            "I am totally and completely and utterly and absolutely and completely and utterly and utterly and completely and completely and utterly bored",
            "I am totally and completely and utterly and absolutely and completely and utterly and utterly and completely and completely and utterly bored",
            "I am totally and completely and utterly and absolutely and completely and utterly and utterly and completely and completely and utterly bored",
            "I am totally and completely and utterly and absolutely and completely and utterly and utterly and completely and completely and utterly bored",
            "I am totally and completely and utterly and absolutely and completely and utterly and utterly and completely and completely and utterly bored",
            "I am totally and completely and utterly and absolutely and completely and utterly and utterly and completely and completely and utterly bored",
            "I am totally and completely and utterly and absolutely and completely and utterly and utterly and completely and completely and utterly bored",
            "I am totally and completely and utterly and absolutely and completely and utterly and utterly and completely and completely and utterly bored",
            "I am totally and completely and utterly and absolutely and completely and utterly and utterly and completely and completely and utterly bored",
            "I am totally and completely