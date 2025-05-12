"""
Write a function to create the next bigger number by rearranging the digits of a given number.
assert rearrange_bigger(12)==21
"""

def rearrange_bigger(num):
    num_list = list(str(num))
    for i in range(len(num_list)-1):
        if num_list[i] < num_list[i+1]:
            num_list[i], num_list[i+1] = num_list[i+1], num_list[i]
            return int(''.join(num_list))
    return -1

print(rearrange_bigger(12))
print(rearrange_bigger(1234))
print(rearrange_bigger(12345))
print(rearrange_bigger(123456))
print(rearrange_bigger(1234567))
print(rearrange_bigger(12345678))
print(rearrange_bigger(123456789))
print(rearrange_bigger(1234567890))
print(rearrange_bigger(12345678901))
print(rearrange_bigger(123456789012))
print(rearrange_bigger(1234567890123))
print(rearrange_bigger(12345678901234))
print(rearrange_bigger(123456789012345))
print(rearrange_bigger(1234567890123456))
print(rearrange_bigger(12345678901234567))
print(rearrange_bigger(123456789012345678))
print(rearrange_bigger(1234567890123456789))
print(rearrange_bigger(12345678901234567890))
print(rearrange_bigger(123456789012345678901))
print(rearrange_bigger(1234567890123456789012))
print(rearrange_bigger(12345678901234567890123))
print(rearrange_bigger(123456789012345678901234))
print(rearrange_bigger(1234567890123456789012345))
print(rearrange_bigger(12345678901234567890123456))
print(rearrange_bigger(123456789012345678901234567))
print(rearrange_bigger(1234567890123456789012345678))
print(rearrange_bigger(12345678901234567890123456789))
print(rearrange_bigger(123456789012345678901234567890))
print(rearrange_bigger(1234567890123456789012345678901))
print(rearrange_bigger(12345678901234567890123456789012))
print(rearrange_bigger(123456789012345678901234567890123))