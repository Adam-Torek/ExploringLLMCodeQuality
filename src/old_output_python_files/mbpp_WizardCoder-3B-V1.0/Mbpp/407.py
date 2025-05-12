"""
Write a function to create the next bigger number by rearranging the digits of a given number.
assert rearrange_bigger(12)==21
"""
def rearrange_bigger(num):
    digits = [int(d) for d in str(num)]
    digits.sort(reverse=True)
    return int(''.join(map(str, digits)))

# Test cases
assert rearrange_bigger(12) == 21
assert rearrange_bigger(100) == 100
assert rearrange_bigger(123) == 321
assert rearrange_bigger(987654321) == 987654321
assert rearrange_bigger(123456789) == 987654321<|endoftext|>