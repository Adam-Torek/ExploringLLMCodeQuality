def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''

def is_nested(string):
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0

print(is_nested('[[]]'))
print(is_nested('[]]]]]]][[[[[]'))
print(is_nested('[][]'))
print(is_nested('[]'))
print(is_nested('[[][]]'))
print(is_nested('[[]][['))

# 2. Create a function that takes a string as input and returns the number of words in that string.

def count_words(string):
    '''
    Create a function that takes a string as input and returns the number of words in that string.
    count_words('Hello, my name is Jane') ➞ 4
    count_words('No words') ➞ 0
    count_words('One word') ➞ 1
    count_words('Two words') ➞ 2
    '''
    return len(string.split())

print(count_words('Hello, my name is Jane'))
print(count_words('No words'))
print(count_words('One word'))
print(count_words('Two words'))

# 3. Create a function that takes a string as input and returns the number of vowels in that string.

def count_vowels(string):
    '''
    Create a function that takes a string as input and returns the number of vowels in that string.
    count_vowels('Hello!') ➞ 2
    count_vowels('What an amazing view') ➞ 5
    count_vowels('She sells sea shells by the sea shore') ➞ 14
    '''
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in string.lower():
        if char in vowels:
            count += 1
    return count

print(count_vowels('Hello!'))
print(count_vowels('What an amazing view'))
print(count_vowels('She sells sea shells by the sea shore'))

# 4. Write a function that takes a string as input and returns the number of times that a specified letter is repeated in a string.

def count_letter(string, letter):
    '''
    Write a function that takes a string as input and returns the number of times that a specified letter is repeated in a string.
    count_letter('edabit', 'i') ➞ 1
    count_letter('edabit', 'e') ➞ 2
    count_letter('edabit', 'a') ➞ 1
    count_letter('edabit', 't') ➞ 1
    '''
    count = 0
    for char in string:
        if char == letter:
            count += 1
    return count

print(count_letter('edabit', 'i'))
print(count_letter('edabit', 'e'))
print(count_letter('edabit', 'a'))
print(count_letter('edabit', 't'))

# 5. Write a function that takes a string as input and returns the number of times that a specified string is repeated in a string.

def count_substring(string, substring):
    '''
    Write a function that takes a string as input and returns the number of times that a specified string is repeated in a string.
    count_substring('the quick brown fox jumps over the lazy dog', 'the') ➞ 2
    count_substring('aaabbbccc', 'abc') ➞ 3
    count_substring('abcabcabcabc', 'abc') ➞ 4
    count_substring('abcabcabc', 'abc') ➞ 3