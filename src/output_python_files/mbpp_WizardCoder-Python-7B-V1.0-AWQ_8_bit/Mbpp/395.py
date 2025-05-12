"""
Write a python function to find the first non-repeated character in a given string.
assert first_non_repeating_character("abcabc") == None
"""

def first_non_repeating_character(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in s:
        if char_count[char] == 1:
            return char

    return None

# Test cases
print(first_non_repeating_character("abcabc")) # None
print(first_non_repeating_character("geeksforgeeks")) # 'f'
print(first_non_repeating_character("abba")) # None
print(first_non_repeating_character("")) # None
print(first_non_repeating_character("a")) # 'a'
print(first_non_repeating_character("aabcbcd")) # 'b'
print(first_non_repeating_character("aabbcdd")) # 'c'
print(first_non_repeating_character("aabbcddd")) # 'd'
print(first_non_repeating_character("aabbccdde")) # 'e'
print(first_non_repeating_character("aabbccddee")) # 'e'
print(first_non_repeating_character("aabbccddeeff")) # 'f'
print(first_non_repeating_character("aabbccddeeffg")) # 'g'
print(first_non_repeating_character("aabbccddeeffg")) # 'g'
print(first_non_repeating_character("aabbccddeeffgg")) # None
print(first_non_repeating_character("aabbccddeeffggh")) # 'h'
print(first_non_repeating_character("aabbccddeeffgghhi")) # 'i'
print(first_non_repeating_character("aabbccddeeffgghhii")) # 'i'
print(first_non_repeating_character("aabbccddeeffgghhiij")) # 'j'
print(first_non_repeating_character("aabbccddeeffgghhiijj")) # 'j'
print(first_non_repeating_character("aabbccddeeffgghhiijjj")) # None
print(first_non_repeating_character("aabbccddeeffgghhiijjjj")) # None
print(first_non_repeating_character("aabbccddeeffgghhiijjjjkk")) # 'k'
print(first_non_repeating_character("aabbccddeeffgghhiijjjjkkl")) # 'l'
print(first_non_repeating_character("aabbccddeeffgghhiijjjjkkll")) # 'l'
print(first_non_repeating_character("aabbccddeeffgghhiijjjjkkllm")) # 'm'
print(first_non_repeating_character("aabbccddeeffgghhiijjjjkkllmm")) # 'm'
print(first_non_repeating_character("aabbccddeeffgghhiijjjjkkllmmn")) # 'n'
print(first_non_repeating_character("aabbccddeeffgghhiijjjjkkllmnn")) # 'n'
print(first_non_repeating_character("aabbccddeeffgghhiijjjjkkllmnnop")) # 'o'
print(first_non_repeating_character("aabbccddeeffgghhiijjjjkkllmnnopq")) # 'p'
print(first_non_repeating_character("aabbccddeeffgghhiijjjjkkllmnnopqr")) # 'r'
print(first_non_repeating_character("aabbccddeeffgghhiijjjjkkllmnnopqrs")) # 's'