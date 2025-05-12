from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
/0x01-python-if_else_loops_functions/10-add.py
#!/usr/bin/python3
def add(a, b):
    """
    Returns the sum of a and b
    """
    return a + b
/0x01-python-if_else_loops_functions/100-print_tebahpla.py
#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 0:
        print("{:c}".format(i), end="")
    else:
        print("{:c}".format(i - 32), end="")
/0x01-python-if_else_loops_functions/102-magic_calculation.py
#!/usr/bin/python3
def magic_calculation(a, b):
    return a + b
/0x01-python-if_else_loops_functions/10-add.py~
#!/usr/bin/python3
def add(a, b):
    """
    Returns the sum of a and b
    """
    return a + b

def main():
    print(add(1, 2))

if __name__ == "__main__":
    main()
/0x01-python-if_else_loops_functions/101-remove_char_at.py
#!/usr/bin/python3
def remove_char_at(str, n):
    return str[:n] + str[n + 1:]
/0x01-python-if_else_loops_functions/100-print_tebahpla.py~
#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 0:
        print("{:c}".format(i), end="")
    else:
        print("{:c}".format(i - 32), end="")
/0x01-python-if_else_loops_functions/101-remove_char_at.py~
#!/usr/bin/python3
def remove_char_at(str, n):
    return str[:n] + str[n + 1:]
/0x01-python-if_else_loops_functions/100-print_tebahpla.py~
#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 0:
        print("{:c}".format(i), end="")
    else:
        print("{:c}".format(i - 32), end="")
/0x01-python-if_else_loops_functions/102-magic_calculation.py~
#!/usr/bin/python3
def magic_calculation(a, b):
    return a + b
/0x01-python-if_else_loops_functions/101-remove_char_at.py~
#!/usr/bin/python3
def remove_char_at(str, n):
    return str[:n] + str[n + 1:]