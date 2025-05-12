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
    vowels = "AEIOU"
    consonants = "BCDFGHJKLMNPQRSTVWXYZ"
    word = word.upper()
    if len(word) == 1:
        return ""
    if len(word) == 2:
        if word[0] in vowels:
            return word[1]
        elif word[1] in vowels:
            return word[0]
        else:
            return ""
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels and word[i+1] in consonants and word[i+2] in consonants:
            return word[i]
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
    vowels = "AEIOU"
    consonants = "BCDFGHJKLMNPQRSTVWXYZ"
    word = word.upper()
    if len(word) == 1:
        return ""
    if len(word) == 2:
        if word[0] in vowels:
            return word[1]
        elif word[1] in vowels:
            return word[0]
        else:
            return ""
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels and word[i+1] in consonants and word[i+2] in consonants:
            return word[i]
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
    vowels = "AEIOU"
    consonants = "BCDFGHJKLMNPQRSTVWXYZ"
    word = word.upper()
    if len(word) == 1:
        return ""
    if len(word) == 2:
        if word[0] in vowels:
            return word[1]
        elif word[1] in vowels:
            return word[0]
        else:
            return ""
    for i in range(len(word)-2, 0, -1):
        if word[i]