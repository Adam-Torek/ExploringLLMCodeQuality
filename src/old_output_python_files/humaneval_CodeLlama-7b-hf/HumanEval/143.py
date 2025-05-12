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
        return ""

    # Main logic
    words = sentence.split()
    result = []
    for word in words:
        if len(word) > 1 and all(i % 2 != 0 for i in range(len(word))):
            result.append(word)

    return " ".join(result)


if __name__ == "__main__":
    print(words_in_sentence("This is a test"))
    print(words_in_sentence("lets go for swimming"))
    print(words_in_sentence(""))
    print(words_in_sentence("a"))
    print(words_in_sentence("a b c"))
    print(words_in_sentence("a b c d"))
    print(words_in_sentence("a b c d e"))
    print(words_in_sentence("a b c d e f"))
    print(words_in_sentence("a b c d e f g"))
    print(words_in_sentence("a b c d e f g h"))
    print(words_in_sentence("a b c d e f g h i"))
    print(words_in_sentence("a b c d e f g h i j"))
    print(words_in_sentence("a b c d e f g h i j k"))
    print(words_in_sentence("a b c d e f g h i j k l"))
    print(words_in_sentence("a b c d e f g h i j k l m"))
    print(words_in_sentence("a b c d e f g h i j k l m n"))
    print(words_in_sentence("a b c d e f g h i j k l m n o"))
    print(words_in_sentence("a b c d e f g h i j k l m n o p"))
    print(words_in_sentence("a b c d e f g h i j k l m n o p q"))
    print(words_in_sentence("a b c d e f g h i j k l m n o p q r"))
    print(words_in_sentence("a b c d e f g h i j k l m n o p q r s"))
    print(words_in_sentence("a b c d e f g h i j k l m n o p q r s t"))
    print(words_in_sentence("a b c d e f g h i j k l m n o p q r s t u"))
    print(words_in_sentence("a b c d e f g h i j k l m n o p q r s t u v"))
    print(words_in_sentence("a b c d e f g h i j k l m n o p q r s t u v w"))
    print(words_in_sentence("a b c d e f g h i j k l m n o p q r s t u v w x"))
    print(words_in_sentence("a b c d e f g h i j k l m n o p q r s t u v w x y"))
    print(words_in_sentence("a b c d e f g h i j k l m n o p q r s t u v w x y z"))
    print(words_in_sentence("a b c d e f g h i j k l m n o p q r s t u v w x y z a"))
    print(words_in_sentence("a b c d e