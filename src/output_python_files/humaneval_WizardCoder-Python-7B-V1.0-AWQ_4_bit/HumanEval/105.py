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
    if not arr:
        return []
    
    arr = sorted([x for x in arr if 1 <= x <= 9])
    arr.reverse()
    
    result = []
    for num in arr:
        if num == 1:
            result.append("One")
        elif num == 2:
            result.append("Two")
        elif num == 3:
            result.append("Three")
        elif num == 4:
            result.append("Four")
        elif num == 5:
            result.append("Five")
        elif num == 6:
            result.append("Six")
        elif num == 7:
            result.append("Seven")
        elif num == 8:
            result.append("Eight")
        elif num == 9:
            result.append("Nine")
    
    return result

# Test cases
print(by_length([2, 1, 1, 4, 5, 8, 2, 3])) # ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
print(by_length([1, 2, 3, 4, 5, 6, 7, 8, 9])) # ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
print(by_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
print(by_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])) # ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
print(by_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])) # ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
print(by_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])) # ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
print(by_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])) # ["Nine", "Eight", "Seven", "Six",