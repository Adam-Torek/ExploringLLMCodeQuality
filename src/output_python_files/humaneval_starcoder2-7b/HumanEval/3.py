from typing import List


def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fallls below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    """
/0x00-python-hello_world/10-check_cycle.c
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: pointer to the head of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
/0x00-python-hello_world/100-write.py
#!/usr/bin/python3
"""
Write a function that writes a string to a text file (UTF8) and returns the number of characters written:
"""


def write_file(filename="", text=""):
    """
    Write a function that writes a string to a text file (UTF8) and returns the number of characters written:
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
/0x00-python-hello_world/101-compile.py
#!/usr/bin/python3
"""
Write a script that compiles a Python file.
"""
import sys

if __name__ == "__main__":
    if len(sys.argv)!= 2:
        print("Usage:./101-compile.py <file>")
        exit(1)
    try:
        with open(sys.argv[1], mode="r", encoding="utf-8") as f:
            text = f.read()
        with open(sys.argv[1][:-3] + "c", mode="w", encoding="utf-8") as f:
            f.write(text)
    except IOError:
        print("Error: can't read file")
        exit(1)
/0x00-python-hello_world/102-magic_calculation.py
#!/usr/bin/python3
"""
Write a function that does exactly the same as the built-in function map().
"""


def magic_calculation(a, b):
    """
    Write a function that does exactly the same as the built-in function map().
    """
    return a + b
/0x00-python-hello_world/10-main.py
#!/usr/bin/python3
"""
Write a function that prints a text with 2 new lines after each of these characters:.,? and :
"""


def text_indentation(text):
    """
    Write a function that prints a text with 2 new lines after each of these characters:.,? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.replace('.', '. \n\n')
    text = text.replace('?', '? \n\n')
    text = text.replace(':', ': \n\n')
    print(text, end="")
/0x00-python-hello_world/100-print_python_list_info.c
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_list - prints all the elements of a list_t list
 * @h: pointer to the head of the list
 * Return: number of nodes
 */
size_t print_list(const list_t *h)
{
	size_t count = 0;

	while (h)
	{
		if (h->str == NULL)
			printf("[0] (nil)\n");
		else
			printf("[%d] %s\n", h->len, h