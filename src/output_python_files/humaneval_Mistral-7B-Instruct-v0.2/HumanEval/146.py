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

# Testing
print(specialFilter([15, -73, 14, -15]))
print(specialFilter([33, -2, -3, 45, 21, 109]))
print(specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
print(specialFilter([10, 11, 12, 13, 14, 15]))
print(specialFilter([100, 111, 123, 135, 147, 159]))