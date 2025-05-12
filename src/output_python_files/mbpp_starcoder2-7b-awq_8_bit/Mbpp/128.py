"""
Write a function to find words that are longer than n characters from a given list of words.
assert long_words(3,"python is a programming language")==['python','programming','language']
"""
def long_words(n,words):
    return [word for word in words if len(word)>n]

print(long_words(3,"python is a programming language"))
/python_basics/list_comprehension.py
"""
List comprehension is a way to create a list based on existing lists.
"""

# Example 1
# Create a list of numbers from 0 to 9
numbers = [number for number in range(10)]
print(numbers)

# Example 2
# Create a list of numbers from 0 to 9 that are even
even_numbers = [number for number in range(10) if number % 2 == 0]
print(even_numbers)

# Example 3
# Create a list of numbers from 0 to 9 that are odd
odd_numbers = [number for number in range(10) if number % 2!= 0]
print(odd_numbers)

# Example 4
# Create a list of numbers from 0 to 9 that are divisible by 3
divisible_by_3 = [number for number in range(10) if number % 3 == 0]
print(divisible_by_3)

# Example 5
# Create a list of numbers from 0 to 9 that are divisible by 3 and even
divisible_by_3_and_even = [number for number in range(10) if number % 3 == 0 and number % 2 == 0]
print(divisible_by_3_and_even)

# Example 6
# Create a list of numbers from 0 to 9 that are divisible by 3 or even
divisible_by_3_or_even = [number for number in range(10) if number % 3 == 0 or number % 2 == 0]
print(divisible_by_3_or_even)

# Example 7
# Create a list of numbers from 0 to 9 that are divisible by 3 or even but not both
divisible_by_3_or_even_not_both = [number for number in range(10) if (number % 3 == 0 or number % 2 == 0) and not (number % 3 == 0 and number % 2 == 0)]
print(divisible_by_3_or_even_not_both)

# Example 8
# Create a list of numbers from 0 to 9 that are divisible by 3 or even but not both
divisible_by_3_or_even_not_both = [number for number in range(10) if (number % 3 == 0 or number % 2 == 0) and not (number % 3 == 0 and number % 2 == 0)]
print(divisible_by_3_or_even_not_both)

# Example 9
# Create a list of numbers from 0 to 9 that are divisible by 3 or even but not both
divisible_by_3_or_even_not_both = [number for number in range(10) if (number % 3 == 0 or number % 2 == 0) and not (number % 3 == 0 and number % 2 == 0)]
print(divisible_by_3_or_even_not_both)

# Example 10
# Create a list of numbers from 0 to 9 that are divisible by 3 or even but not both
divisible_by_3_or_even_not_both = [number for number in range(10) if (number % 3 == 0 or number % 2 == 0) and not (number % 3 == 0 and number % 2 == 0)]
print(divisible_by_3_or_even_not_both)

# Example 11
# Create a list of numbers from 0 to 9 that are divisible by 3 or even but not both
divisible_by_3_or_even_not_both = [number for number in range(10) if (number % 3 == 0 or number % 2 == 0) and not (number % 3 == 0 and number