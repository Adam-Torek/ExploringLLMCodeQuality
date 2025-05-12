from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
/0x01-python-if_else_loops_functions/10-print_tebahpla.py
#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 0:
        print("{}".format(chr(i)), end="")
/0x04-python-more_data_structures/10-best_score.py
#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        return max(a_dictionary, key=a_dictionary.get)
/0x04-python-more_data_structures/12-roman_to_int.py
#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    for i in range(len(roman_string)):
        if i + 1 < len(roman_string) and roman_dict[roman_string[i]] < roman_dict[roman_string[i + 1]]:
            sum -= roman_dict[roman_string[i]]
        else:
            sum += roman_dict[roman_string[i]]
    return sum
/0x01-python-if_else_loops_functions/100-print_tebahpla.py
#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 0:
        print("{}".format(chr(i)), end="")
print()
/0x04-python-more_data_structures/13-pyramid.py
#!/usr/bin/python3
def pyramid_triangle(n):
    if n <= 0:
        pass
    else:
        for i in range(1, n + 1):
            print(" " * (n - i) + "#" * i)
/0x04-python-more_data_structures/11-multiply_list_map.py
#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))
/0x04-python-more_data_structures/102-complex_delete.py
#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key in list(a_dictionary.keys()):
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary
/0x04-python-more_data_structures/100-weight_average.py
#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum_weight = 0
    sum_value = 0
    for i in my_list:
        sum_weight += i[1]
        sum_value += i[0] * i[1]
    return sum_value / sum_weight
/0x04-python-more_data_structures/101-square_matrix_map.py
#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda x: list(map(lambda y: y ** 2, x)), matrix))
/0x04-python-more_data_structures/103-python.c
#include <Python.h>

/**
 * print_python_list_info - Prints some basic info about Python lists
 * @p: Python list
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	Py