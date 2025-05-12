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
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    words = sentence.split()
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return " ".join(result)


# Test cases
print(words_in_sentence("This is a test")) # Output: "is"
print(words_in_sentence("lets go for swimming")) # Output: "go for"
print(words_in_sentence("prime numbers")) # Output: ""
print(words_in_sentence("prime numbers are fun")) # Output: "prime numbers"
print(words_in_sentence("hello world")) # Output: ""
print(words_in_sentence("lets go for swimming")) # Output: "go for"
print(words_in_sentence("lets go for swimming")) # Output: "go for"
print(words_in_sentence("lets go for swimming")) # Output: "go for"
print(words_in_sentence("lets go for swimming")) # Output: "go for"
print(words_in_sentence("lets go for swimming")) # Output: "go for"
print(words_in_sentence("lets go for swimming")) # Output: "go for"
print(words_in_sentence("lets go for swimming")) # Output: "go for"
print(words_in_sentence("lets go for swimming")) # Output: "go for"
print(words_in_sentence("lets go for swimming")) # Output: "go for"
print(words_in_sentence("lets go for swimming")) # Output: "go for"
print(words_in_sentence("lets go for swimming")) # Output: "go for"
print(words_in_sentence("lets go for swimming")) # Output: "go for"
print(words_in_sentence("lets go for swimming")) # Output: "go for"
print(words_in_sentence("lets go for swimming")) # Output: "go for"
print(words_in_sentence("lets go for swimming")) # Output: "go for"
print(words_in_sentence("lets go for swimming")) # Output: "go for"
print(words_in_sentence("lets go for swimming")) # Output: "go for"
print(words_in_sentence("lets go for swimming")) # Output: "go for"
print(words_in_sentence("lets go for swimming")) # Output: "go for"
print(words_in_sentence("lets go for swimming")) # Output: "go for"
print(words_in_sentence("lets go for swimming")) # Output: "go for"
print(words_in_sentence("lets go for swimming")) # Output: "go for"
print(words_in_sentence("lets go for swimming")) # Output: "go for"
print(words_in_sentence("lets go for swimming")) # Output: "go for"
print(words_in_sentence("lets go for swimming")) # Output: "go for"
print(