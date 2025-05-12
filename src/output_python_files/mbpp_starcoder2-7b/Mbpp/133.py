"""
Write a function to calculate the sum of the negative numbers of a given list of numbers.
assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==-32
"""

def sum_negativenum(list):
    sum = 0
    for i in list:
        if i < 0:
            sum += i
    return sum

print(sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]))
/python/python_basics/001_hello_world.py
"""
Write a program that prints "Hello World" to the screen.
"""

print("Hello World")
/python/python_basics/002_print_name.py
"""
Write a program that prints your name on screen.
"""

print("")
/python/python_basics/003_print_name_and_age.py
"""
Write a program that prints your name and age on screen.
"""

print("")
print("25")
/python/python_basics/004_print_name_and_age_in_one_line.py
"""
Write a program that prints your name and age in one line.
"""

print("", "25")
/python/python_basics/005_print_name_and_age_in_one_line_with_separator.py
"""
Write a program that prints your name and age in one line with a separator.
"""

print("", "25", sep=" ")
/python/python_basics/006_print_name_and_age_in_one_line_with_separator_and_end.py
"""
Write a program that prints your name and age in one line with a separator and end.
"""

print("", "25", sep=" ", end=" ")
/python/python_basics/007_print_name_and_age_in_one_line_with_separator_and_end_and_new_line.py
"""
Write a program that prints your name and age in one line with a separator, end and new line.
"""

print("", "25", sep=" ", end=" ", file=open("output.txt", "w"))
/python/python_basics/008_print_name_and_age_in_one_line_with_separator_and_end_and_new_line_and_file.py
"""
Write a program that prints your name and age in one line with a separator, end, new line and file.
"""

print("", "25", sep=" ", end=" ", file=open("output.txt", "w"))
/python/python_basics/009_print_name_and_age_in_one_line_with_separator_and_end_and_new_line_and_file_and_flush.py
"""
Write a program that prints your name and age in one line with a separator, end, new line, file and flush.
"""

print("", "25", sep=" ", end=" ", file=open("output.txt", "w"), flush=True)
/python/python_basics/010_print_name_and_age_in_one_line_with_separator_and_end_and_new_line_and_file_and_flush_and_close.py
"""
Write a program that prints your name and age in one line with a separator, end, new line, file, flush and close.
"""

print("", "25", sep=" ", end=" ", file=open("output.txt", "w"), flush=True)
print("", "25", sep=" ", end=" ", file=open("output.txt", "w"), flush=True)
print("", "25", sep=" ", end=" ", file=open("output.txt", "w"), flush=True)
print("", "25", sep=" ", end=" ", file=open("output.txt", "w"), flush=True)
print("", "25