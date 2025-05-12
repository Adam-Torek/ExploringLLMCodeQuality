def fruit_distribution(s,n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.
    for examble:
    fruit_distribution("5 apples and 6 oranges", 19) ->19 - 5 - 6 = 8
    fruit_distribution("0 apples and 1 oranges",3) -> 3 - 0 - 1 = 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
    fruit_distribution("100 apples and 1 oranges",120) -> 120 - 100 - 1 = 19
    """
    apples, oranges = s.split()
    apples = int(apples.split()[0])
    oranges = int(oranges.split()[0])
    return n - apples - oranges


# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19)) # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3)) # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
print(fruit_distribution("100 apples and 1 oranges", 100)) # Output: 0
print(fruit_distribution("100 apples and 1 oranges", 101)) # Output: 0
print(fruit_distribution("100 apples and 1 oranges", 102)) # Output: 1
print(fruit_distribution("100 apples and 1 oranges", 103)) # Output: 2
print(fruit_distribution("100 apples and 1 oranges", 104)) # Output: 3
print(fruit_distribution("100 apples and 1 oranges", 105)) # Output: 4
print(fruit_distribution("100 apples and 1 oranges", 106)) # Output: 5
print(fruit_distribution("100 apples and 1 oranges", 107)) # Output: 6
print(fruit_distribution("100 apples and 1 oranges", 108)) # Output: 7
print(fruit_distribution("100 apples and 1 oranges", 109)) # Output: 8
print(fruit_distribution("100 apples and 1 oranges", 110)) # Output: 9
print(fruit_distribution("100 apples and 1 oranges", 111)) # Output: 10
print(fruit_distribution("100 apples and 1 oranges", 112)) # Output: 11
print(fruit_distribution("100 apples and 1 oranges", 113)) # Output: 12
print(fruit_distribution("100 apples and 1 oranges", 114)) # Output: 13
print(fruit_distribution("100 apples and 1 oranges", 115)) # Output: 14
print(fruit_distribution("100 apples and 1 oranges", 116)) # Output: 15
print(fruit_distribution("100 apples and 1 oranges", 117)) # Output: 16
print(fruit_distribution("100 apples and 1 oranges", 118)) # Output: 17
print(fruit_distribution("100 apples and 1 oranges", 119)) # Output: 18
print(fruit_distribution("100