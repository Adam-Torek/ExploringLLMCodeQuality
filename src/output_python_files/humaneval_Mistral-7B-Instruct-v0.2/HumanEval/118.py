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
print(get_closest_vowel("hello")) # e
print(get_closest_vowel("rainbow")) # o
print(get_closest_vowel("elephant")) # a
print(get_closest_vowel("watermelon")) # e
print(get_closest_vowel("pineapple")) # a
print(get_closest_vowel("orange")) # a
print(get_closest_vowel("grapefruit")) # a
print(get_closest_vowel("kiwi")) # i
print(get_closest_vowel("mango")) # o
print(get_closest_vowel("papaya")) # a
print(get_closest_vowel("dragonfruit")) # a
print(get_closest_vowel("guava")) # a
print(get_closest_vowel("lychee")) # e
print(get_closest_vowel("starfruit")) # a
print(get_closest_vowel("pomegranate")) # a
print(get_closest_vowel("cherry")) # e
print(get_closest_vowel("blueberry")) # e
print(get_closest_vowel("raspberry")) # a
print(get_closest_vowel("blackberry")) # a
print(get_closest_vowel("strawberry")) # a
print(get_closest_vowel("watermelon")) # e
print(get_closest_vowel("pineapple")) # a
print(get_closest_vowel("grapefruit")) # a
print(get_closest_vowel("kiwi")) # i
print(get_closest_vowel("mango")) # o
print(get_closest_vowel("papaya")) # a
print(get_closest_vowel("dragonfruit")) # a
print(get_closest_vowel("guava")) # a
print(get_closest_vowel("lychee")) # e
print(get_closest_vowel("starfruit")) # a
print(get_closest_vowel("pomegranate")) # a
print(get_closest_vowel("cherry"))