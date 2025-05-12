def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    word = word.lower()
    if len(word) < 2:
        return ""
    for i in range(len(word) - 1):
        if word[i] in consonants and word[i + 1] in consonants:
            return ""
        if word[i] in vowels and word[i + 1] in consonants:
            return word[i]
        if word[i] in consonants and word[i + 1] in vowels:
            return word[i + 1]
    return ""


def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    word = word.lower()
    if len(word) < 2:
        return ""
    for i in range(len(word) - 1):
        if word[i] in consonants and word[i + 1] in consonants:
            return ""
        if word[i] in vowels and word[i + 1] in consonants:
            return word[i]
        if word[i] in consonants and word[i + 1] in vowels:
            return word[i + 1]
    return ""


def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    word = word.lower()
    if len(word) < 2:
        return ""
    for i in range(len(word) - 1):
        if word[i] in consonants and word[i + 1] in consonants:
            return ""
        if word[i] in vowels and word[i + 1] in consonants:
            return word[i]