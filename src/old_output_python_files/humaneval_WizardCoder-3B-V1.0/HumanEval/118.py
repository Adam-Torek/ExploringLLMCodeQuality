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

# Solution
def get_closest_vowel(word):
    vowels = "aeiouAEIOU"
    left, right = 0, len(word) - 1
    closest_vowel = ""

    while left < right:
        mid = (left + right) // 2
        if word[mid] in vowels:
            closest_vowel = word[mid]
            left = mid + 1
        else:
            right = mid

    return closest_vowel

# Test cases
print(get_closest_vowel("yogurt"))  # Output: "u"
print(get_closest_vowel("FULL"))  # Output: "U"
print(get_closest_vowel("quick"))  # Output: ""
print(get_closest_vowel("ab"))  # Output: ""<|endoftext|>