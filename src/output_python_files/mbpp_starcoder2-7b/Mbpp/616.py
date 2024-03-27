"""
Write a function which takes two tuples of the same length and performs the element wise modulo.
assert tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)) == (0, 4, 5, 1)
"""

def tuple_modulo(a, b):
    return tuple(map(lambda x, y: x % y, a, b))

print(tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)))
<file_sep>/python/0000_python_basics/0000_python_basics.py
"""
Python Basics
"""

# 1. Print the string "Hello, World!" to your terminal
print("Hello, World!")

# 2. Print the string "Hello, World!" to your terminal 10 times
print("Hello, World!" * 10)

# 3. Print the string "Hello, World!" to your terminal 10 times, but on separate lines
print("Hello, World!\n" * 10)

# 4. Print the string "Hello, World!" to your terminal 10 times, but on separate lines, with a space between each line
print("Hello, World!\n" * 10, end="")

# 5. Print the string "Hello, World!" to your terminal 10 times, but on separate lines, with a space between each line, and a newline at the end
print("Hello, World!\n" * 10, end="\n")

# 6. Print the string "Hello, World!" to your terminal 10 times, but on separate lines, with a space between each line, and a newline at the end, and a tab at the end
print("Hello, World!\n" * 10, end="\t")

# 7. Print the string "Hello, World!" to your terminal 10 times, but on separate lines, with a space between each line, and a newline at the end, and a tab at the end, and a comma at the end
print("Hello, World!\n" * 10, end=", ")

# 8. Print the string "Hello, World!" to your terminal 10 times, but on separate lines, with a space between each line, and a newline at the end, and a tab at the end, and a comma at the end, and a newline at the end
print("Hello, World!\n" * 10, end=", \n")

# 9. Print the string "Hello, World!" to your terminal 10 times, but on separate lines, with a space between each line, and a newline at the end, and a tab at the end, and a comma at the end, and a newline at the end, and a tab at the end
print("Hello, World!\n" * 10, end=", \n\t")

# 10. Print the string "Hello, World!" to your terminal 10 times, but on separate lines, with a space between each line, and a newline at the end, and a tab at the end, and a comma at the end, and a newline at the end, and a tab at the end, and a newline at the end
print("Hello, World!\n" * 10, end=", \n\t\n")

# 11. Print the string "Hello, World!" to your terminal 10 times, but on separate lines, with a space between each line, and a newline at the end, and a tab at the end, and a comma at the end, and a newline at the end, and a tab at the end, and a newline at the end, and a tab at the end
print("Hello, World!\n" * 10, end=", \n\t\n\t")

# 12. Print the string "Hello, World!" to your terminal 10 times, but on separate lines, with a space between each line, and a newline at the end, and a tab at the end, and a comma at the end, and a newline at the end, and a tab at the end, and a newline at the end, and a tab at the end, and a newline at the end
print("Hello, World!\n" * 10, end=", \n\t\n\t\n")

# 13. Print the string "Hello, World!" to your terminal 10 times, but on separate lines, with a space between