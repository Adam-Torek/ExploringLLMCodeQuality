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
    # filter out numbers outside of range
    arr = [x for x in arr if 1 <= x <= 9]
    # sort the array
    arr.sort()
    # reverse the array
    arr.reverse()
    # replace each number with its corresponding name
    names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    result = [names[x-1] for x in arr]
    return result

# Test cases
print(by_length([2, 1, 1, 4, 5, 8, 2, 3])) # ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
print(by_length([])) # []
print(by_length([1, -1, 55])) # ['One']
print(by_length([1, 2, 3, 4, 5, 6, 7, 8, 9])) # ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
print(by_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
print(by_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])) # ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
print(by_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])) # ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
print(by_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])) # ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
print(by_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])) # ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
print(by_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,