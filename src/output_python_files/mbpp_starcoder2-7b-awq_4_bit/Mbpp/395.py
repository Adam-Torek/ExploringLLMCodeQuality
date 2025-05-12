"""
Write a python function to find the first non-repeated character in a given string.
assert first_non_repeating_character("abcabc") == None
"""

def first_non_repeating_character(string):
    """
    :param string:
    :return:
    """
    if not string:
        return None
    char_dict = {}
    for char in string:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    for char in string:
        if char_dict[char] == 1:
            return char
    return None

if __name__ == "__main__":
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abc"))
    print(first_non_repeating_character("aabb"))
    print(first_non_repeating_character("aabbcc"))
    print(first_non_repeating_character("aabbccdd"))
    print(first_non_repeating_character("aabbccddff"))
    print(first_non_repeating_character("aabbccddffgg"))
    print(first_non_repeating_character("aabbccddffgghh"))
    print(first_non_repeating_character("aabbccddffgghhii"))
    print(first_non_repeating_character("aabbccddffgghhiijj"))
    print(first_non_repeating_character("aabbccddffgghhiijjkk"))
    print(first_non_repeating_character("aabbccddffgghhiijjkkll"))
    print(first_non_repeating_character("aabbccddffgghhiijjkkllmm"))
    print(first_non_repeating_character("aabbccddffgghhiijjkkllmmnn"))
    print(first_non_repeating_character("aabbccddffgghhiijjkkllmmnnoo"))
    print(first_non_repeating_character("aabbccddffgghhiijjkkllmmnnoopp"))
    print(first_non_repeating_character("aabbccddffgghhiijjkkllmmnnooppqq"))
    print(first_non_repeating_character("aabbccddffgghhiijjkkllmmnnooppqqrr"))
    print(first_non_repeating_character("aabbccddffgghhiijjkkllmmnnooppqqrrss"))
    print(first_non_repeating_character("aabbccddffgghhiijjkkllmmnnooppqqrrssuu"))
    print(first_non_repeating_character("aabbccddffgghhiijjkkllmmnnooppqqrrssuuww"))
    print(first_non_repeating_character("aabbccddffgghhiijjkkllmmnnooppqqrrssuuwwxx"))
    print(first_non_repeating_character("aabbccddffgghhiijjkkllmmnnooppqqrrssuuwwxxyy"))
    print(first_non_repeating_character("aabbccddffgghhiijjkkllmmnnooppqqrrssuuwwxxyyzz"))
    print(first_non_repeating_character("aabbccddffgghhiijjkkllmmnnooppqqrrssuuwwxxyyzzaa"))
    print(first_non_repeating_character("aabbccddffgghhiijjkkllmmnnooppqqrrssuuwwxxyyzzaaab"))
    print(first_non_repeating_character("aabbccddffgghhiijjkkllmmnnooppqqrrssuuwwxxyyzzaaabbb"))
    print(first_non_repeating_character("aabbccddffgghhiijjkkllmmnnooppqqrrssuuwwxxyyzzaaabbbcc"))
    print(first_non_repeating_character("aabbccddffgghhiijjkkllmmnnooppqqrrssuuwwxxyyzzaaab