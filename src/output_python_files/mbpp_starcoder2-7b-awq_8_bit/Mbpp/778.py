"""
Write a function to pack consecutive duplicates of a given list elements into sublists.
assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])==[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
"""

def pack_consecutive_duplicates(lst):
    """
    >>> pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])
    [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
    """
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    result = []
    current_sublist = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            current_sublist.append(lst[i])
        else:
            result.append(current_sublist)
            current_sublist = [lst[i]]
    result.append(current_sublist)
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/for_loop_basic1.py
"""
Basic - Print all integers from 0 to 150.
"""

def print_integers():
    for i in range(151):
        print(i)

if __name__ == '__main__':
    print_integers()
/python/python_fundamentals/for_loop_basic2.py
"""
Multiples of Five - Print all the multiples of 5 from 5 to 1,000,000.
"""

def print_multiples_of_five():
    for i in range(5, 1000001, 5):
        print(i)

if __name__ == '__main__':
    print_multiples_of_five()
/python/python_fundamentals/for_loop_basic3.py
"""
Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
"""

def print_countdown_by_fours():
    for i in range(2018, 0, -4):
        print(i)

if __name__ == '__main__':
    print_countdown_by_fours()
/python/python_fundamentals/for_loop_basic4.py
"""
Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
"""

def print_flexible_counter(low_num, high_num, mult):
    for i in range(low_num, high_num + 1):
        if i % mult == 0:
            print(i)

if __name__ == '__main__':
    print_flexible_counter(2, 9, 3)
/python/python_fundamentals/for_loop_basic5.py
"""
Print and Count - Print all integers from 0 to 1000, but for multiples of 5 print "Coding" instead of the number, and for multiples of 10 print "Coding Dojo".
"""

def print_and_count():
    for i in range(1001):
        if i % 5 == 0 and i % 10 == 0:
            print("Coding Dojo")
        elif i % 5 == 0:
            print("Coding")
        else:
            print(i)

if __name__ == '__main__':
    print_and_count()
/python/python_fundamentals/for_loop_basic6.py
"""
Whoa.