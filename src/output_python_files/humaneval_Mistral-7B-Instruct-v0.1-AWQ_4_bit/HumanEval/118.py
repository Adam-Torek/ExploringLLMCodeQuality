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


def main():
    word1 = input("Enter first word: ")
    word2 = input("Enter second word: ")
    closest_vowel1 = get_closest_vowel(word1)
    closest_vowel2 = get_closest_vowel(word2)
    print("Closest vowel between two consonants from the right side of the word of", word1, "is", closest_vowel1)
    print("Closest vowel between two consonants from the right side of the word of", word2, "is", closest_vowel2)


main()