def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

    For example:
      arr = [2, 1, 1, 4, 5, 8, 2, 3]   
            -> sort arr -> [1, 1, 2, 2, 3, 4, 5, 8] 
            -> reverse arr -> [8, 5, 4, 3, 2, 2, 1, 1]
      return ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    
      If the array is empty, return an empty array:
      arr = []
      return []
    
      If the array has any strange number ignore it:
      arr = [1, -1 , 55] 
            -> sort arr -> [-1, 1, 55]
            -> reverse arr -> [55, 1, -1]
      return = ['One']
    """
    # Filter out the numbers that are not between 1 and 9
    filtered_arr = [num for num in arr if 1 <= num <= 9]
    # Sort the filtered array
    sorted_arr = sorted(filtered_arr)
    # Reverse the sorted array
    reversed_arr = reversed(sorted_arr)
    # Create a list of strings with the names of the digits
    names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    # Create a list with the names of the digits in the reversed order
    result = [names[i] for i in reversed_arr]
    # Return the result
    return result

# Test cases
print(by_length([2, 1, 1, 4, 5, 8, 2, 3])) # ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
print(by_length([1, -1, 55])) # ['One']
print(by_length([])) # []
print(by_length([10, 11, 12])) # []
print(by_length([100, 11, 12])) # []