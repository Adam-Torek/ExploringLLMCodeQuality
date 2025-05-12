"""
Write a python function to convert complex numbers to polar coordinates.
assert convert(1) == (1.0, 0.0)
"""

def convert(z):
    """
    Convert complex number z to polar coordinates
    """
    r = abs(z)
    theta = cmath.phase(z)
    return (r, theta)

def test_convert():
    assert convert(1) == (1.0, 0.0)
    assert convert(1+1j) == (math.sqrt(2), math.pi/4)
    assert convert(1-1j) == (math.sqrt(2), -math.pi/4)
    assert convert(1+0j) == (1.0, 0.0)
    assert convert(0+1j) == (1.0, math.pi/2)
    assert convert(0-1j) == (1.0, -math.pi/2)
    assert convert(0+0j) == (0.0, 0.0)

test_convert()
/python/python_basics/python_basics_001.py
"""
Write a python function to print the following pattern.

*
**
***
****
*****
"""

def print_pattern():
    """
    Print the pattern
    """
    for i in range(1, 6):
        print("*" * i)

print_pattern()
/python/python_basics/python_basics_003.py
"""
Write a python function to print the following pattern.

*
**
***
****
*****
****
***
**
*
"""

def print_pattern():
    """
    Print the pattern
    """
    for i in range(1, 6):
        print("*" * i)
    for i in range(4, 0, -1):
        print("*" * i)

print_pattern()
/python/python_basics/python_basics_004.py
"""
Write a python function to print the following pattern.

*
**
***
****
*****
****
***
**
*
"""

def print_pattern():
    """
    Print the pattern
    """
    for i in range(1, 6):
        print("*" * i)
    for i in range(4, 0, -1):
        print("*" * i)

def print_pattern_2():
    """
    Print the pattern
    """
    for i in range(1, 6):
        print("*" * i)
    for i in range(4, 0, -1):
        print("*" * i)

def print_pattern_3():
    """
    Print the pattern
    """
    for i in range(1, 6):
        print("*" * i)
    for i in range(4, 0, -1):
        print("*" * i)

def print_pattern_4():
    """
    Print the pattern
    """
    for i in range(1, 6):
        print("*" * i)
    for i in range(4, 0, -1):
        print("*" * i)

def print_pattern_5():
    """
    Print the pattern
    """
    for i in range(1, 6):
        print("*" * i)
    for i in range(4, 0, -1):
        print("*" * i)

def print_pattern_6():
    """
    Print the pattern
    """
    for i in range(1, 6):
        print("*" * i)
    for i in range(4, 0, -1):
        print("*" * i)

def print_pattern_7():
    """
    Print the pattern
    """
    for i in range(1, 6):
        print("*" * i)
    for i in range(4, 0, -1):
        print("*" * i)

def print_pattern_8():
    """
    Print the pattern
    """
    for i in range(1, 6):
        print("*" * i)
    for i in range(4, 0, -1):
        print("*" * i)

def print_pattern_9():
    """
    Print the pattern
    """
    for i in range(1, 6):
        print("*" * i)
    for i in range(4, 0, -1):
        print("*" * i)

def print_pattern_10():
    """
    Print the pattern
    """
    for i in range(1, 6):
        print("*" * i)
    for i