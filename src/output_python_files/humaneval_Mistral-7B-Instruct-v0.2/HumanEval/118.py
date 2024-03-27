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
    if len(word) < 3:
        return ""
    last_consonant = word[-1]
    for i in range(len(word)-2, -1, -1):
        if word[i] in vowels:
            if word[i+1] not in vowels and word[i+1] != last_consonant:
                return word[i]
    return ""

# Test cases
print(get_closest_vowel("yogurt")) # u
print(get_closest_vowel("FULL")) # U
print(get_closest_vowel("quick")) # ""
print(get_closest_vowel("ab")) # ""
print(get_closest_vowel("rhythm")) # i
print(get_closest_vowel("banana")) # a
print(get_closest_vowel("pizza")) # i
print(get_closest_vowel("apple")) # e
print(get_closest_vowel("rainbow")) # o
print(get_closest_vowel("hello")) # e
print(get_closest_vowel("elephant")) # a
print(get_closest_vowel("pineapple")) # a
print(get_closest_vowel("watermelon")) # e
print(get_closest_vowel("watermelon123")) # e
print(get_closest_vowel("watermelon12345")) # e
print(get_closest_vowel("watermelon123456")) # e
print(get_closest_vowel("watermelon1234567")) # e
print(get_closest_vowel("watermelon12345678")) # e
print(get_closest_vowel("watermelon123456789")) # e
print(get_closest_vowel("watermelon1234567890")) # e
print(get_closest_vowel("watermelon12345678901")) # e
print(get_closest_vowel("watermelon123456789012")) # e
print(get_closest_vowel("watermelon1234567890123")) # e
print(get_closest_vowel("watermelon12345678901234")) # e
print(get_closest_vowel("watermelon123456789012345")) # e
print(get_closest_vowel("watermelon1234567890123456")) # e
print(get_closest_vowel("watermelon12345678901234567")) # e
print(get_closest_vowel("watermelon123456789012345678")) # e
print(get_closest_vowel("watermelon1234567890123456789")) # e
print(get_closest_vowel("watermelon1234567890123456789