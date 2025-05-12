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
<file_sep>/python/python_basics/001_hello_world.py
"""
Write a program that prints "Hello World" to the screen.
"""

print("Hello World")
<file_sep>/python/python_basics/002_print_name.py
"""
Write a program that prints your name on screen.
"""

print("<NAME>")
<file_sep>/python/python_basics/003_print_name_and_age.py
"""
Write a program that prints your name and age.
"""

print("<NAME>")
print("26")
<file_sep>/python/python_basics/004_print_name_and_age_in_one_line.py
"""
Write a program that prints your name and age in one line.
"""

print("<NAME>", "26")
<file_sep>/python/python_basics/005_print_name_and_age_in_one_line_with_comma.py
"""
Write a program that prints your name and age in one line with comma.
"""

print("<NAME>", "26", sep=",")
<file_sep>/python/python_basics/006_print_name_and_age_in_one_line_with_space.py
"""
Write a program that prints your name and age in one line with space.
"""

print("<NAME>", "26", sep=" ")
<file_sep>/python/python_basics/007_print_name_and_age_in_one_line_with_tab.py
"""
Write a program that prints your name and age in one line with tab.
"""

print("<NAME>", "26", sep="\t")
<file_sep>/python/python_basics/008_print_name_and_age_in_one_line_with_newline.py
"""
Write a program that prints your name and age in one line with newline.
"""

print("<NAME>", "26", sep="\n")
<file_sep>/python/python_basics/009_print_name_and_age_in_one_line_with_newline_and_tab.py
"""
Write a program that prints your name and age in one line with newline and tab.
"""

print("<NAME>", "26", sep="\n\t")
<file_sep>/python/python_basics/010_print_name_and_age_in_one_line_with_newline_and_space.py
"""
Write a program that prints your name and age in one line with newline and space.
"""

print("<NAME>", "26", sep="\n ")
<file_sep>/python/python_basics/011_print_name_and_age_in_one_line_with_newline_and_comma.py
"""
Write a program that prints your name and age in one line with newline and comma.
"""

print("<NAME>", "26", sep="\n,")
<file_sep>/python/python_basics/012_print_name_and_age_in_one_line_with_newline_and_tab_and_space.py
"""
Write a program that prints your name and age in one line with newline, tab and space.
"""

print("<NAME>", "26", sep="\n\t ")
<file_sep>/python/python_basics/013_print_name_and_age_in_one_line_with_newline_and_tab_and_comma.py
"""
Write a program that prints your name and age in one line with newline, tab and comma.
"""

print("<NAME>", "26", sep="\n\t,")
<file_sep>/python/python_basics/014_print_name_and_age_in_one_line_with_newline_and_tab_and_space_and_comma.py
"""
Write a program that prints