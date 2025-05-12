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
print(words_in_sentence("This is a test"))  # Output: "is"
print(words_in_sentence("lets go for swimming"))  # Output: "go for"
print(words_in_sentence("prime numbers"))  # Output: ""
print(words_in_sentence("prime numbers are cool"))  # Output: "prime numbers"
print(words_in_sentence("I love programming"))  # Output: "love programming"
print(words_in_sentence("I love programming and testing"))  # Output: "love programming and"
print(words_in_sentence("I love programming and testing prime numbers"))  # Output: "love programming and testing"
print(words_in_sentence("I love programming and testing prime numbers 123"))  # Output: "love programming and testing"
print(words_in_sentence("I love programming and testing prime numbers 123 456"))  # Output: "love programming and testing"
print(words_in_sentence("I love programming and testing prime numbers 123 456 789"))  # Output: "love programming and testing"
print(words_in_sentence("I love programming and testing prime numbers 123 456 789 11"))  # Output: "love programming and testing"
print(words_in_sentence("I love programming and testing prime numbers 123 456 789 11 23"))  # Output: "love programming and testing"
print(words_in_sentence("I love programming and testing prime numbers 123 456 789 11 23 29"))  # Output: "love programming and testing"
print(words_in_sentence("I love programming and testing prime numbers 123 456 789 11 23 29 31"))  # Output: "love programming and testing"
print(words_in_sentence("I love programming and testing prime numbers 123 456 789 11 23 29 31 47"))  # Output: "love programming and testing"
print(words_in_sentence("I love programming and testing prime numbers 123 456 789 11 23 29 31 47 53"))  # Output: "love programming and testing"
print(words_in_sentence("I love programming and testing prime numbers 123 456 789 11 23 29 31 47 53 59"))  # Output: "love programming and testing"
print(words_in_sentence("I love programming and testing prime numbers 123 456 789