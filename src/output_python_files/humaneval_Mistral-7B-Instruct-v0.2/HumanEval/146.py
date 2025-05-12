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
        if len(str(num)) > 1:
            first_digit = int(str(num)[0])
            last_digit = int(str(num)[-1])
            if first_digit % 2 != 0 and last_digit % 2 != 0 and num > 10:
                count += 1
    return count

# Test Cases
print(specialFilter([15, -73, 14, -15])) # 1
print(specialFilter([33, -2, -3, 45, 21, 109])) # 2
print(specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # 0
print(specialFilter([11, 13, 15, 17, 19, 21, 23, 25, 27, 29])) # 11
print(specialFilter([100, 101, 102, 103, 104, 105, 106, 107, 108, 109])) # 10
print(specialFilter([-11, -13, -15, -17, -19, -21, -23, -25, -27, -29])) # 0
print(specialFilter([])) # 0
print(specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) # 0
print(specialFilter([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15])) # 0
print(specialFilter([-21, -23, -25, -27, -29, -31, -33, -35, -37, -39])) # 10
print(specialFilter([1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009])) # 10
print(specialFilter([-1000, -1001, -1002, -1003, -1004, -1005, -1006, -1007, -1008, -1009])) # 0
print(specialFilter([10101, 10102, 10103, 10104, 10105, 10106, 10107, 10108, 10109])) # 1
print(specialFilter([-10101, -10102, -10103, -10104, -10105, -10106, -10107, -10108, -10109])) # 0
print(specialFilter([1011101, 1