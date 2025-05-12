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

# Solution:
# We can iterate over the words in the string and check if the first word is "I".
# If it is, we increment a counter. We can then continue iterating over the words
# and check if the next word starts with "I". If it does, we decrement the counter.
# If the counter reaches 0, we have found a boredom.

def is_bored(S):
    count = 0
    words = S.split()
    for i in range(len(words)):
        if words[i] == "I":
            count += 1
        if i < len(words) - 1 and words[i+1] == "I":
            count -= 1
        if count == 0:
            return i + 1
    return 0

# Test cases
print(is_bored("Hello world"))  # Output: 0
print(is_bored("The sky is blue. The sun is shining. I love this weather"))  # Output: 1<|endoftext|>