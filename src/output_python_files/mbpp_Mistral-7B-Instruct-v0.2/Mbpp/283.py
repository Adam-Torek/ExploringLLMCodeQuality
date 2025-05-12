"""
Write a python function takes in an integer and check whether the frequency of each digit in the integer is less than or equal to the digit itself.
assert validate(1234) == True
"""
def validate(num):
    num_str = str(num)
    freq = {}
    for digit in num_str:
        if digit in freq:
            if int(digit) > freq[digit]:
                return False
            freq[digit] += 1
        else:
            freq[digit] = 1
    return True

# Test cases
assert validate(1234) == True
assert validate(11122) == True
assert validate(33221) == True
assert validate(12303) == False
assert validate(12300) == False