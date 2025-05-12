from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
<file_sep>/week02/day02/01_list_of_lists.py
# Create a list of lists where the inner lists have 5 random numbers in them.
# Print the third inner list.
# Print the sum of the numbers in the 4th inner list.

import random

list_of_lists = []

for i in range(5):
    inner_list = []
    for j in range(5):
        inner_list.append(random.randint(0, 100))
    list_of_lists.append(inner_list)

print(list_of_lists[2])
print(sum(list_of_lists[3]))
<file_sep>/week02/day02/04_append_a_list.py
# - Create an empty list which will contain names (strings)
# - Ask the user for a name
# - Add it to the list
# - If the user typed "0" as a name, aka "None" in English, print the list

names = []

while True:
    name = input("Enter a name: ")
    if name == "0":
        break
    names.append(name)

print(names)
<file_sep>/week02/day02/03_append_a_list.py
# - Create an empty list which will contain names (strings)
# - Ask the user for a name
# - Add it to the list
# - If the user typed "0" as a name, aka "None" in English, print the list

names = []

while True:
    name = input("Enter a name: ")
    if name == "0":
        break
    names.append(name)

print(names)
<file_sep>/week02/day02/02_list_of_lists.py
# Create a list of lists where the inner lists have 5 random numbers in them.
# Print the third inner list.
# Print the sum of the numbers in the 4th inner list.

import random

list_of_lists = []

for i in range(5):
    inner_list = []
    for j in range(5):
        inner_list.append(random.randint(0, 100))
    list_of_lists.append(inner_list)

print(list_of_lists[2])
print(sum(list_of_lists[3]))
<file_sep>/week02/day02/05_append_a_list.py
# - Create an empty list which will contain names (strings)
# - Ask the user for a name
# - Add it to the list
# - If the user typed "0" as a name, aka "None" in English, print the list

names = []

while True:
    name = input("Enter a name: ")
    if name == "0":
        break
    names.append(name)

print(names)
<file_sep>/week02/day02/06_append_a_list.py
# - Create an empty list which will contain names (strings)
# - Ask the user for a name
# - Add it to the list
# - If the user typed "0" as a name, aka "None" in English, print the list

names = []

while True:
    name = input("Enter a name: ")
    if name == "0":
        break
    names.append(name)

print(names)
<file_sep>/week02/day02/07_append_a_list.py
# - Create an empty list which will contain names (strings)
# - Ask the user for a name
# - Add it to the list
# - If the user typed "0" as a name, aka "None" in English, print the list

names = []

while True:
    name = input("Enter a name: ")
    if name == "0":
        break
    names.append(name)

print(names)
<file_sep>/week02/day02/08_append_a_list