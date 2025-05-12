"""
Write a function that returns the list in a list of lists whose sum of elements is the highest.
assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]
"""

def max_sum_list(lst):
    max_sum = 0
    max_list = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if sum(lst[i]) > max_sum:
                max_sum = sum(lst[i])
                max_list = lst[i]
    return max_list

print(max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]]))
/week02/day02/04_count_letters.py
"""
Write a function that takes a string and counts the number of different characters in it.
"""

def count_letters(string):
    count = 0
    for i in string:
        if i not in count:
            count += 1
    return count

print(count_letters("This is a string"))
/week02/day02/05_count_letters_2.py
"""
Write a function that takes a string and counts the number of different characters in it.
"""

def count_letters(string):
    count = 0
    for i in string:
        if i not in count:
            count += 1
    return count

print(count_letters("This is a string"))

def count_letters_2(string):
    count = 0
    for i in string:
        if i not in count:
            count += 1
    return count

print(count_letters_2("This is a string"))
/week02/day02/02_sum_digits.py
"""
Write a function that takes a number and returns the sum of its digits.
"""

def sum_digits(number):
    sum = 0
    for i in str(number):
        sum += int(i)
    return sum

print(sum_digits(123))
/week02/day02/03_factorial.py
"""
Write a function that takes a number and returns one if it's a factor of 100.
"""

def factorial(number):
    if number == 100:
        return 1
    else:
        return 0

print(factorial(100))
/week02/day02/01_sum_digits.py
"""
Write a function that takes a number and returns the sum of its digits.
"""

def sum_digits(number):
    sum = 0
    for i in str(number):
        sum += int(i)
    return sum

print(sum_digits(123))
/week02/day02/06_palindrome_2.py
"""
Write a function that checks whether a string is a palindrome.
"""

def palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

print(palindrome("racecar"))
/week02/day02/07_palindrome_2.py
"""
Write a function that checks whether a string is a palindrome.
"""

def palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

print(palindrome("racecar"))

def palindrome_2(string):
    if string == string[::-1]:
        return True
    else:
        return False

print(palindrome_2("racecar"))
/week02/day02/08_palindrome_2.py
"""
Write a function that checks whether a string is a palindrome.
"""

def palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

print(palindrome("racecar"))

def palindrome_2(string):
    if string == string[::-1]:
        return True
    else:
        return False

print(palindrome_2("racecar"))

def palindrome_3(string):
    if string == string[::-1]:
        return True
    else:
        return False

print(palindrome_3("racecar"))