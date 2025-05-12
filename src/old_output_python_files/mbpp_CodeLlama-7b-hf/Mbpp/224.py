"""
Write a python function to count the number of set bits (binary digits with value 1) in a given number.
assert count_Set_Bits(2) == 1
"""


def count_Set_Bits(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count


if __name__ == '__main__':
    print(count_Set_Bits(2))
    print(count_Set_Bits(10))
    print(count_Set_Bits(100))
    print(count_Set_Bits(1000))
    print(count_Set_Bits(10000))
    print(count_Set_Bits(100000))
    print(count_Set_Bits(1000000))
    print(count_Set_Bits(10000000))
    print(count_Set_Bits(100000000))
    print(count_Set_Bits(1000000000))
    print(count_Set_Bits(10000000000))
    print(count_Set_Bits(100000000000))
    print(count_Set_Bits(1000000000000))
    print(count_Set_Bits(10000000000000))
    print(count_Set_Bits(100000000000000))
    print(count_Set_Bits(1000000000000000))
    print(count_Set_Bits(10000000000000000))
    print(count_Set_Bits(100000000000000000))
    print(count_Set_Bits(1000000000000000000))
    print(count_Set_Bits(10000000000000000000))
    print(count_Set_Bits(100000000000000000000))
    print(count_Set_Bits(1000000000000000000000))
    print(count_Set_Bits(10000000000000000000000))
    print(count_Set_Bits(100000000000000000000000))
    print(count_Set_Bits(1000000000000000000000000))
    print(count_Set_Bits(10000000000000000000000000))
    print(count_Set_Bits(100000000000000000000000000))
    print(count_Set_Bits(1000000000000000000000000000))
    print(count_Set_Bits(10000000000000000000000000000))
    print(count_Set_Bits(100000000000000000000000000000))
    print(count_Set_Bits(1000000000000000000000000000000))
    print(count_Set_Bits(10000000000000000000000000000000))
    print(count_Set_Bits(10