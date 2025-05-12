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

def get_closest_vowel(word):
    vowels = "aeiou"
    vowels_list = []
    for i in range(len(word)):
        if word[i] in vowels:
            vowels_list.append(i)
    if len(vowels_list) == 0:
        return ""
    elif len(vowels_list) == 1:
        return word[vowels_list[0]]
    else:
        for i in range(len(vowels_list)):
            if vowels_list[i] == 0:
                vowels_list.pop(i)
                break
        for i in range(len(vowels_list)):
            if vowels_list[i] == len(word) - 1:
                vowels_list.pop(i)
                break
        if len(vowels_list) == 0:
            return ""
        else:
            return word[vowels_list[0]]

def get_closest_vowel(word):
    vowels = "aeiou"
    vowels_list = []
    for i in range(len(word)):
        if word[i] in vowels:
            vowels_list.append(i)
    if len(vowels_list) == 0:
        return ""
    elif len(vowels_list) == 1:
        return word[vowels_list[0]]
    else:
        for i in range(len(vowels_list)):
            if vowels_list[i] == 0:
                vowels_list.pop(i)
                break
        for i in range(len(vowels_list)):
            if vowels_list[i] == len(word) - 1:
                vowels_list.pop(i)
                break
        if len(vowels_list) == 0:
            return ""
        else:
            return word[vowels_list[0]]

def get_closest_vowel(word):
    vowels = "aeiou"
    vowels_list = []
    for i in range(len(word)):
        if word[i] in vowels:
            vowels_list.append(i)
    if len(vowels_list) == 0:
        return ""
    elif len(vowels_list) == 1:
        return word[vowels_list[0]]
    else:
        for i in range(len(vowels_list)):
            if vowels_list[i] == 0:
                vowels_list.pop(i)
                break
        for i in range(len(vowels_list)):
            if vowels_list[i] == len(word) - 1:
                vowels_list.pop(i)
                break
        if len(vowels_list) == 0:
            return ""
        else:
            return word[vowels_list[0]]

def get_closest_vowel(word):
    vowels = "aeiou"
    vowels_list = []
    for i in range(len(word)):
        if word[i] in vowels:
            vowels_list.append(i)
    if len(vowels_list) == 0:
        return ""
    elif len(vowels_list) == 1:
        return word[vowels_list[0]]
    else:
        for i in range(len(vowels_list)):
            if vowels_list[i] == 0:
                vowels_list.pop(i)
                break
        for i in range(len(vowels_list