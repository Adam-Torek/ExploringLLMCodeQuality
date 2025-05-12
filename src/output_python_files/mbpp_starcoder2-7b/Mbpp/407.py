"""
Write a function to create the next bigger number by rearranging the digits of a given number.
assert rearrange_bigger(12)==21
"""

def rearrange_bigger(n):
    n = str(n)
    for i in range(len(n)-1, 0, -1):
        if n[i] > n[i-1]:
            break
    else:
        return -1
    for j in range(len(n)-1, i-1, -1):
        if n[j] > n[i-1]:
            break
    n = n[:i-1] + n[j] + n[i-1:j] + n[i] + n[j+1:]
    return int(n)

print(rearrange_bigger(12))
print(rearrange_bigger(123456789))
print(rearrange_bigger(123456798))
print(rearrange_bigger(12345678))
print(rearrange_bigger(1234567))
print(rearrange_bigger(123456))
print(rearrange_bigger(12345))
print(rearrange_bigger(1234))
print(rearrange_bigger(123))
print(rearrange_bigger(12))
print(rearrange_bigger(1))
print(rearrange_bigger(21))
print(rearrange_bigger(59884848459873))
print(rearrange_bigger(111))
print(rearrange_bigger(531))
print(rearrange_bigger(10))
print(rearrange_bigger(20))
print(rearrange_bigger(21))
print(rearrange_bigger(121))
print(rearrange_bigger(123456789))
print(rearrange_bigger(123456798))
print(rearrange_bigger(12345678))
print(rearrange_bigger(1234567))
print(rearrange_bigger(123456))
print(rearrange_bigger(12345))
print(rearrange_bigger(1234))
print(rearrange_bigger(123))
print(rearrange_bigger(12))
print(rearrange_bigger(1))
print(rearrange_bigger(21))
print(rearrange_bigger(59884848459873))
print(rearrange_bigger(111))
print(rearrange_bigger(531))
print(rearrange_bigger(10))
print(rearrange_bigger(20))
print(rearrange_bigger(21))
print(rearrange_bigger(121))
print(rearrange_bigger(123456789))
print(rearrange_bigger(123456798))
print(rearrange_bigger(12345678))
print(rearrange_bigger(1234567))
print(rearrange_bigger(123456))
print(rearrange_bigger(12345))
print(rearrange_bigger(1234))
print(rearrange_bigger(123))
print(rearrange_bigger(12))
print(rearrange_bigger(1))
print(rearrange_bigger(21))
print(rearrange_bigger(59884848459873))
print(rearrange_bigger(111))
print(rearrange_bigger(531))
print(rearrange_bigger(10))
print(rearrange_bigger(20))
print(rearrange_bigger(21))
print(rearrange_bigger(121))
print(rearrange_bigger(123456789))
print(rearrange_