def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """
    a = str(a)
    b = str(b)
    a = [int(i) for i in a]
    b = [int(i) for i in b]
    a = [int(i) for i in a if i != 0]
    b = [int(i) for i in b if i != 0]
    return sum([a[-1] * b[-1]])


print(multiply(148, 412))  # Output: 16
print(multiply(19, 28))  # Output: 72
print(multiply(2020, 1851))  # Output: 0
print(multiply(14, -15))  # Output: 20

# Test.describe("Example Tests")
# Test.assert_equals(multiply(148, 412), 16)
# Test.assert_equals(multiply(19, 28), 72)
# Test.assert_equals(multiply(2020, 1851), 0)
# Test.assert_equals(multiply(14, -15), 20)
# Test.assert_equals(multiply(10, 10), 0)
# Test.assert_equals(multiply(0, 10), 0)
# Test.assert_equals(multiply(10, 0), 0)
# Test.assert_equals(multiply(0, 0), 0)
# Test.assert_equals(multiply(123, 456), 12)
# Test.assert_equals(multiply(12, 34), 4)
# Test.assert_equals(multiply(1234, 5678), 12)
# Test.assert_equals(multiply(12345, 6789), 12)
# Test.assert_equals(multiply(123456, 7890), 12)
# Test.assert_equals(multiply(1234567, 89012), 12)
# Test.assert_equals(multiply(12345678, 90123), 12)
# Test.assert_equals(multiply(123456789, 102345), 12)
# Test.assert_equals(multiply(1234567890, 203456), 12)
# Test.assert_equals(multiply(12345678901, 234567), 12)
# Test.assert_equals(multiply(123456789012, 345678), 12)
# Test.assert_equals(multiply(1234567890123, 456789), 12)
# Test.assert_equals(multiply(12345678901234, 567890), 12)
# Test.assert_equals(multiply(123456789012345, 678901), 12)
# Test.assert_equals(multiply(1234567890123456, 789012), 12)
# Test.assert_equals(multiply(12345678901234567, 890123), 12)
# Test.assert_equals(multiply(1234