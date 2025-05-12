"""
Write a function to create the next bigger number by rearranging the digits of a given number.
assert rearrange_bigger(12)==21
"""

def rearrange_bigger(num):
    num = str(num)
    for i in range(len(num)-1):
        if num[i] < num[i+1]:
            num = num[:i] + num[i+1] + num[i] + num[i+2:]
            return int(num)
    return -1

print(rearrange_bigger(12))
print(rearrange_bigger(1254))
print(rearrange_bigger(12543))
print(rearrange_bigger(125436))
print(rearrange_bigger(1254365))
print(rearrange_bigger(12543659))
print(rearrange_bigger(125436598))
print(rearrange_bigger(1254365987))
print(rearrange_bigger(12543659876))
print(rearrange_bigger(125436598765))
print(rearrange_bigger(1254365987654))
print(rearrange_bigger(12543659876543))
print(rearrange_bigger(125436598765432))
print(rearrange_bigger(1254365987654321))
print(rearrange_bigger(12543659876543210))
print(rearrange_bigger(125436598765432109))
print(rearrange_bigger(1254365987654321098))
print(rearrange_bigger(12543659876543210987))
print(rearrange_bigger(125436598765432109876))
print(rearrange_bigger(1254365987654321098765))
print(rearrange_bigger(12543659876543210987654))
print(rearrange_bigger(125436598765432109876543))
print(rearrange_bigger(1254365987654321098765432))
print(rearrange_bigger(12543659876543210987654321))
print(rearrange_bigger(125436598765432109876543210))
print(rearrange_bigger(1254365987654321098765432109))
print(rearrange_bigger(12543659876543210987654321098))
print(rearrange_bigger(125436598765432109876543210987))
print(rearrange_bigger(1254365987654321098765432109876))
print(rearrange_bigger(12543659876543210987654321098765))
print(rearrange_bigger(125436598765432109876543210987654))
print(rearrange_bigger(1254365987654321098765432109876