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
print(armstrong_number(370))
print(armstrong_number(371))
print(armstrong_number(407))
/Day 1/Day1_Assignment_1.py
"""
Write a program to print the following pattern
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
/Day 1/Day1_Assignment_3.py
"""
Write a program to print the following pattern
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
/Day 1/Day1_Assignment_2.py
"""
Write a program to print the following pattern
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

for i in range(1,6):
    for j in range(1,i+1):