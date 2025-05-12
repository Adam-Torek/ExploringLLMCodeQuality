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
    return int(a[-1]) * int(b[-1])


print(multiply(148, 412)) # Output: 16
print(multiply(19, 28)) # Output: 72
print(multiply(2020, 1851)) # Output: 0
print(multiply(14, -15)) # Output: 20

# Test.describe("Basic Tests")
# Test.assert_equals(multiply(148, 412), 16)
# Test.assert_equals(multiply(19, 28), 72)
# Test.assert_equals(multiply(2020, 1851), 0)
# Test.assert_equals(multiply(14, -15), 20)
# Test.assert_equals(multiply(0, 100), 0)
# Test.assert_equals(multiply(100, 0), 0)
# Test.assert_equals(multiply(123456789, 987654321), 0)
# Test.assert_equals(multiply(123456789, 123456789), 0)
# Test.assert_equals(multiply(123456789, 1234567890), 0)
# Test.assert_equals(multiply(123456789, 1234567890123456789), 0)
# Test.assert_equals(multiply(123456789, 12345678901234567890123456789), 0)
# Test.assert_equals(multiply(123456789, 123456789012345678901234567890123456789), 0)
# Test.assert_equals(multiply(123456789, 1234567890123456789012345678901234567890123456789), 0)
# Test.assert_equals(multiply(123456789, 12345678901234567890123456789012345678901234567890123456789), 0)
# Test.assert_equals(multiply(123456789, 123456789012345678901234567890123456789012345678901234567890123456789), 0)
# Test.assert_equals(multiply(123456789, 123456789012345678901234567890123456