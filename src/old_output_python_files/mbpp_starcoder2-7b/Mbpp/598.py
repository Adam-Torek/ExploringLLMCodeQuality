"""
Write a function to check whether the given number is armstrong or not.
assert armstrong_number(153)==True
"""

def armstrong_number(num):
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum=sum+digit**3
        temp=temp//10
    if num==sum:
        return True
    else:
        return False

print(armstrong_number(153))
print(armstrong_number(123))
<file_sep>/Day-1/Day-1-Assignment/Assignment-1.py
"""
Write a program to print the following pattern
1
12
123
1234
12345
"""

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()
<file_sep>/Day-1/Day-1-Assignment/Assignment-2.py
"""
Write a program to print the following pattern
1
22
333
4444
55555
"""

for i in range(1,6):
    for j in range(1,i+1):
        print(i,end="")
    print()
<file_sep>/Day-1/Day-1-Assignment/Assignment-3.py
"""
Write a program to print the following pattern
1
12
123
1234
12345
123456
"""

for i in range(1,7):
    for j in range(1,i+1):
        print(j,end="")
    print()
<file_sep>/Day-1/Day-1-Assignment/Assignment-4.py
"""
Write a program to print the following pattern
1
23
456
78910
"""

for i in range(1,5):
    for j in range(1,i+1):
        print(j,end="")
    print()
<file_sep>/Day-1/Day-1-Assignment/Assignment-5.py
"""
Write a program to print the following pattern
1
12
123
1234
12345
123456
1234567
"""

for i in range(1,8):
    for j in range(1,i+1):
        print(j,end="")
    print()
<file_sep>/Day-1/Day-1-Assignment/Assignment-6.py
"""
Write a program to print the following pattern
1
12
123
1234
12345
123456
1234567
12345678
"""

for i in range(1,9):
    for j in range(1,i+1):
        print(j,end="")
    print()
<file_sep>/Day-1/Day-1-Assignment/Assignment-7.py
"""
Write a program to print the following pattern
1
23
456
78910
1112131415
"""

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()
<file_sep>/Day-1/Day-1-Assignment/Assignment-8.py
"""
Write a program to print the following pattern
1
23
456
78910
1112131415
1617181920
"""

for i in range(1,7):
    for j in range(1,i+1):
        print(j,end="")
    print()
<file_sep>/Day-1/Day-1-Assignment/Assignment-9.py
"""
Write a program to print the following pattern
1
23
456
78910
1112131415
1617181920
212223242526
"""

for i in range(1,7):
    for j in range(1,i+1):
        print(j,end="")
    print()
<file_sep>/Day-1/Day-1-Assignment/Assignment-10.py
"""
Write a program to print the following pattern
1
23
456
78910
1112131415