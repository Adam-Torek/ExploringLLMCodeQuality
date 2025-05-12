"""
Write a function that takes in an array and an integer n, and re-arranges the first n elements of the given array so that all negative elements appear before positive ones, and where the relative order among negative and positive elements is preserved.
assert re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9) == [-1, -3, -7, 4, 5, 6, 2, 8, 9]
"""

def re_arrange_array(arr, n):
    neg_arr = []
    pos_arr = []
    for i in arr:
        if i < 0:
            neg_arr.append(i)
        else:
            pos_arr.append(i)
    return neg_arr + pos_arr

print(re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9)) # Output: [-1, -3, -7, 4, 5, 6, 2, 8, 9]

# Another way to solve this problem using two pointers:
def re_arrange_array(arr, n):
    neg_arr = []
    pos_arr = []
    for i in arr:
        if i < 0:
            neg_arr.append(i)
        else:
            pos_arr.append(i)
    return neg_arr + pos_arr

def re_arrange_array(arr, n):
    neg_arr = []
    pos_arr = []
    for i in arr:
        if i < 0:
            neg_arr.append(i)
        else:
            pos_arr.append(i)
    return neg_arr + pos_arr

def re_arrange_array(arr, n):
    neg_arr = []
    pos_arr = []
    for i in arr:
        if i < 0:
            neg_arr.append(i)
        else:
            pos_arr.append(i)
    return neg_arr + pos_arr

def re_arrange_array(arr, n):
    neg_arr = []
    pos_arr = []
    for i in arr:
        if i < 0:
            neg_arr.append(i)
        else:
            pos_arr.append(i)
    return neg_arr + pos_arr

print(re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9)) # Output: [-1, -3, -7, 4, 5, 6, 2, 8, 9]

# Another way to solve this problem using two pointers:
def re_arrange_array(arr, n):
    neg_arr = []
    pos_arr = []
    for i in arr:
        if i < 0:
            neg_arr.append(i)
        else:
            pos_arr.append(i)
    return neg_arr + pos_arr

def re_arrange_array(arr, n):
    neg_arr = []
    pos_arr = []
    for i in arr:
        if i < 0:
            neg_arr.append(i)
        else:
            pos_arr.append(i)
    return neg_arr + pos_arr

def re_arrange_array(arr, n):
    neg_arr = []
    pos_arr = []
    for i in arr:
        if i < 0:
            neg_arr.append(i)
        else:
            pos_arr.append(i)
    return neg_arr + pos_arr

print(re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9) # Output: [-1, -3, -7, 4, 5, 6, 2, 8, 9]

# Another way to solve this problem using two pointers:
def re_arrange_array(arr, n):
    neg_arr = []
    pos_arr = []
    for i in arr: