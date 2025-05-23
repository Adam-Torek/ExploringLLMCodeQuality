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
    count = 0
    for word in S.split('.'):
        if word.strip().startswith('I'):
            count += 1
    return count

# Testing
print(is_bored("Hello world"))
print(is_bored("The sky is blue. The sun is shining. I love this weather"))
print(is_bored("I'm bored"))
print(is_bored("I'm not bored"))
print(is_bored("I'm just a little bored"))
print(is_bored("I'm extremely bored"))
print(is_bored("I'm extremely excited"))
print(is_bored("I'm extremely excited. I can't wait to go to the party"))
print(is_bored("I'm extremely excited. I can't wait to go to the party. I'll see you there"))
print(is_bored("I'm extremely excited. I can't wait to go to the party. I'll see you there. What a great day!"))