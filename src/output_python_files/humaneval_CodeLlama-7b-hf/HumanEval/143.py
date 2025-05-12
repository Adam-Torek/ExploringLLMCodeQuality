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
    # Edge case
    if not sentence:
        return ''

    # Main logic
    words = sentence.split(' ')
    result = ''
    for word in words:
        if len(word) > 1 and all(i % 2 != 0 for i in range(len(word))):
            result += word + ' '

    return result.strip()


if __name__ == '__main__':
    print(words_in_sentence('This is a test'))
    print(words_in_sentence('lets go for swimming'))
    print(words_in_sentence('This is a test sentence'))
    print(words_in_sentence('This is a test sentence with a lot of words'))
    print(words_in_sentence('This is a test sentence with a lot of words and numbers'))
    print(words_in_sentence('This is a test sentence with a lot of words and numbers 1234567890'))
    print(words_in_sentence('This is a test sentence with a lot of words and numbers 1234567890 1234567890'))
    print(words_in_sentence('This is a test sentence with a lot of words and numbers 1234567890 1234567890 1234567890'))
    print(words_in_sentence('This is a test sentence with a lot of words and numbers 1234567890 1234567890 1234567890 1234567890'))
    print(words_in_sentence('This is a test sentence with a lot of words and numbers 1234567890 1234567890 1234567890 1234567890 1234567890'))
    print(words_in_sentence('This is a test sentence with a lot of words and numbers 1234567890 1234567890 1234567890 1234567890 1234567890 1234567890'))
    print(words_in_sentence('This is a test sentence with a lot of words and numbers 1234567890 1234567890 1234567890 1234567890 1234567890 1234567890 1234567890'))
    print(words_in_sentence('This is a test sentence with a lot of words and numbers 1234567890 1234567890 1234567890 1234567890 1234567890 1234567890 1234567890 123456789