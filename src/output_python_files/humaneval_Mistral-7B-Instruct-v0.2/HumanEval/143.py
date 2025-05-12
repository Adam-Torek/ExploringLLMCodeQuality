def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """
    words = sentence.split()
    primes = [2, 3, 5]
    prime_words = []
    for word in words:
        if len(word) in primes:
            prime_words.append(word)
    return " ".join(prime_words)

# Test cases
print(words_in_sentence("This is a test"))
print(words_in_sentence("lets go for swimming"))
print(words_in_sentence("hello world"))
print(words_in_sentence("the quick brown fox jumps over the lazy dog"))