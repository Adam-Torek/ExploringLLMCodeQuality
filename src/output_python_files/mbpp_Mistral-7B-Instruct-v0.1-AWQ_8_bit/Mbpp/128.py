"""
Write a function to find words that are longer than n characters from a given list of words.
assert long_words(3,"python is a programming language")==['python','programming','language']
"""
def long_words(n,words):
    """
    This function takes in a list of words and an integer n and returns a list of words that are longer than n characters.
    """
    result = []
    for word in words:
        if len(word)>n:
            result.append(word)
    return result

# Test the function
print(long_words(3,"python is a programming language"))