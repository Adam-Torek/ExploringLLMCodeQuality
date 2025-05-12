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
    result = ""
    for word in words:
        if len(word) > 1 and is_prime(len(word)):
            result += word + " "
    return result.strip()

def is_prime(n):
    """
    Check if n is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test cases
sentence1 = "This is a test"
print(words_in_sentence(sentence1))

sentence2 = "lets go for swimming"
print(words_in_sentence(sentence2))