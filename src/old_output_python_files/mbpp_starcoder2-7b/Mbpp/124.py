"""
Write a function to get the angle of a complex number.
assert math.isclose(angle_complex(0,1j), 1.5707963267948966, rel_tol=0.001)
"""

def angle_complex(a,b):
    return math.atan2(b.imag,a.real)

print(angle_complex(0,1j))
<file_sep>/python/python_100_days/day01-15/day03/03.py
"""
题目：
将一个列表的数据复制到另一个列表中。
"""

a = [1, 2, 3, 4, 5, 6]
b = a[:]
print(b)
<file_sep>/python/python_100_days/day01-15/day04/04.py
"""
题目：
输出一个随机数。
"""

import random

print(random.random())
<file_sep>/python/python_100_days/day01-15/day03/04.py
"""
题目：
列表排序及连接。
"""

a = [1, 2, 3, 4, 5, 6]
a.sort()
print(a)

b = [1, 2, 3, 4, 5, 6]
b.reverse()
print(b)

c = [1, 2, 3, 4, 5, 6]
d = [1, 2, 3, 4, 5, 6]
c.extend(d)
print(c)
<file_sep>/python/python_100_days/day01-15/day03/01.py
"""
题目：
求100之内的素数。
"""

import math

for i in range(2, 101):
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            break
    else:
        print(i)
<file_sep>/python/python_100_days/day01-15/day04/03.py
"""
题目：
按相反的顺序输出列表的值。
"""

a = [1, 2, 3, 4, 5, 6]
a.reverse()
print(a)
<file_sep>/python/python_100_days/day01-15/day03/02.py
"""
题目：
按相反的顺序输出列表的值。
"""

a = [1, 2, 3, 4, 5, 6]
a.reverse()
for i in a:
    print(i)
<file_sep>/python/python_100_days/day01-15/day04/01.py
"""
题目：
求输入数字的平方，如果平方运算后小于 50 则退出。
"""

while True:
    a = int(input('请输入数字：'))
    b = a ** 2
    if b < 50:
        break
    print(b)
<file_sep>/python/python_100_days/day01-15/day03/05.py
"""
题目：
列表转化为字典。
"""

a = [1, 2, 3, 4, 5, 6]
b = dict(zip(a, a))
print(b)
<file_sep>/python/python_100_days/day01-15/day04/02.py
"""
题目：
利用循环依次对 list 中的每个元素打印出每个元素的索引及元素本身。
"""

a = [1, 2, 3, 4, 5, 6]
for i in range(len(a)):
    print(i, a[i])
<file_sep>/python/python_100_days/day01-15/day03/06.py
"""
题目：
字典转化为列表。
"""

a = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6}
b = list