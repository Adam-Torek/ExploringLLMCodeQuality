"""
Write a python function to find the sum of all odd natural numbers within the range l and r.
assert sum_in_range(2,5) == 8
"""

def sum_in_range(l, r):
    sum = 0
    for i in range(l, r+1):
        if i % 2!= 0:
            sum += i
    return sum

print(sum_in_range(2,5))
<file_sep>/python/python_basics/01_hello_world.py
"""
Write a python program to print "Hello World"
"""

print("Hello World")
<file_sep>/python/python_basics/03_print_name.py
"""
Write a python program to print your name
"""

print("<NAME>")
<file_sep>/python/python_basics/02_print_name_and_age.py
"""
Write a python program to print your name and age
"""

print("<NAME>")
print("25")
<file_sep>/python/python_basics/04_print_name_and_age_in_one_line.py
"""
Write a python program to print your name and age in one line
"""

print("<NAME>", "25")
<file_sep>/python/python_basics/05_print_name_and_age_in_one_line_with_comma.py
"""
Write a python program to print your name and age in one line with comma
"""

print("<NAME>", "25", sep=",")
<file_sep>/python/python_basics/06_print_name_and_age_in_one_line_with_space.py
"""
Write a python program to print your name and age in one line with space
"""

print("<NAME>", "25", sep=" ")
<file_sep>/python/python_basics/07_print_name_and_age_in_one_line_with_tab.py
"""
Write a python program to print your name and age in one line with tab
"""

print("<NAME>", "25", sep="\t")
<file_sep>/python/python_basics/08_print_name_and_age_in_one_line_with_newline.py
"""
Write a python program to print your name and age in one line with newline
"""

print("<NAME>", "25", sep="\n")
<file_sep>/python/python_basics/09_print_name_and_age_in_one_line_with_newline_and_tab.py
"""
Write a python program to print your name and age in one line with newline and tab
"""

print("<NAME>", "25", sep="\n\t")
<file_sep>/python/python_basics/10_print_name_and_age_in_one_line_with_newline_and_tab_and_space.py
"""
Write a python program to print your name and age in one line with newline, tab and space
"""

print("<NAME>", "25", sep="\n\t ")
<|endoftext|>