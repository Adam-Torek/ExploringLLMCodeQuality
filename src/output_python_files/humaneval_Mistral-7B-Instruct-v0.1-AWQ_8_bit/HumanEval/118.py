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
    vowels = "aeiouAEIOU"
    result = ""
    for i in range(len(word)-2):
        if word[i] in vowels and word[i+1] in vowels:
            result = word[i]
            break
        elif word[i] not in vowels and word[i+1] in vowels:
            result = word[i+1]
            break
    return result

# test
print(get_closest_vowel("yogurt"))
print(get_closest_vowel("FULL"))
print(get_closest_vowel("quick"))
print(get_closest_vowel("ab"))