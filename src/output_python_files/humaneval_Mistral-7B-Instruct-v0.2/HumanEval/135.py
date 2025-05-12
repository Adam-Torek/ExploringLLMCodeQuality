def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Create a dictionary to store the count of each element
    count_dict = {}
    for i in arr:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1

    # Find the first element which count is odd
    odd_count = None
    for key, value in count_dict.items():
        if value % 2 != 0:
            odd_count = key
            break

    # If no odd count element is found then return -1
    if odd_count is None:
        return -1

    # Find the index of the first element which is smaller than the odd count element
    for i, j in enumerate(arr):
        if j < odd_count:
            return i

# Test the function
arr = [1,2,4,3,5]
print(can_arrange(arr)) # 3

arr = [1,2,3]
print(can_arrange(arr)) # -1

arr = [1,3,5,2,4]
print(can_arrange(arr)) # 0

arr = [1,2,3,3,4]
print(can_arrange(arr)) # 2

arr = [1,2,3,3,4,3]
print(can_arrange(arr)) # 3

arr = [1,2,3,3,4,3,3]
print(can_arrange(arr)) # 4

arr = [1,2,3,3,4,3,3,3]
print(can_arrange(arr)) # 5

arr = [1,2,3,3,4,3,3,3,3]
print(can_arrange(arr)) # 6

arr = [1,2,3,3,4,3,3,3,3,3]
print(can_arrange(arr)) # 7

arr = [1,2,3,3,4,3,3,3,3,3,3]
print(can_arrange(arr)) # 8

arr = [1,2,3,3,4,3,3,3,3,3,3,3]
print(can_arrange(arr)) # 9

arr = [1,2,3,3,4,3,3,3,3,3,3,3,3]
print(can_arrange(arr)) # 10

arr = [1,2,3,3,4,3,3,3,3,3,3,3,3,3]
print(can_arrange(arr)) # 11

arr = [1,2,3,3,4,3,3,3,3,3,3,3,3,3,3]
print(can_arrange(arr)) # 12

arr = [1,2,3,3,4,3,3,3,3,3,3,3,3,3,3,3]
print(can_arrange(arr)) # 13

arr = [1,2,3,3,4,3,3,3,3,3,3,3,3,3,3,3,3]
print(can_arrange(arr)) # 14

arr = [1,2,3,3,4,3,3,3,3,3,3,3,3,3,3,3,3,3]
print