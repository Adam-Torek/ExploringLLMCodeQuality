def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for num in nums:
        if num > 10:
            if int(str(num)[0]) % 2 == 1 and int(str(num)[-1]) % 2 == 1:
                count += 1
    return count

# Test cases
print(specialFilter([15, -73, 14, -15])) # Output: 1
print(specialFilter([33, -2, -3, 45, 21, 109])) # Output: 2
print(specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # Output: 0
print(specialFilter([11, 13, 15, 17, 19, 21, 23, 25, 27, 29])) # Output: 4
print(specialFilter([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])) # Output: 4
print(specialFilter([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10])) # Output: 0
print(specialFilter([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29])) # Output: 4

# Test case for negative numbers
print(specialFilter([-11, -13, -15, -17, -19])) # Output: 0
print(specialFilter([-1, -3, -5, -7, -9])) # Output: 0
print(specialFilter([-11, -13, -15, -17, -19, -21, -23, -25, -27, -29])) # Output: 0
print(specialFilter([-1, -3, -5, -7, -9, -11, -13, -15, -17, -19, -21, -23, -25, -27, -29])) # Output: 0

# Test case for even numbers
print(specialFilter([112, 114, 116, 118, 120, 122])) # Output: 0
print(specialFilter([121, 123, 125, 127, 129])) # Output: 0
print(specialFilter([112, 114, 116, 118, 120, 122, 121, 123, 125, 127, 129])) # Output: 2
print(specialFilter([112, 114, 116, 118, 120, 122, 121, 123, 125, 127, 129, 131, 133, 135])) # Output: 4

# Test case for even numbers with negative numbers
print(specialFilter([-112, -114, -11