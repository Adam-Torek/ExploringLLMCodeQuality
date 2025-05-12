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
print(armstrong_number(125))
print(armstrong_number(370))
print(armstrong_number(371))
print(armstrong_number(407))
/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/Day 1/