"""
Write a function to find whether a given array of integers contains any duplicate element.
assert test_duplicate(([1,2,3,4,5]))==False
"""
def test_duplicate(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                return True
    return False

"""
Write a function to find whether a given array of integers contains any duplicate element.
assert test_duplicate_set(([1,2,3,4,5]))==False
"""
def test_duplicate_set(arr):
    return len(set(arr))!=len(arr)

"""
Write a function to find whether a given array of integers contains any duplicate element.
assert test_duplicate_dict(([1,2,3,4,5]))==False
"""
def test_duplicate_dict(arr):
    d={}
    for i in arr:
        if i in d:
            return True
        d[i]=1
    return False

"""
Write a function to find whether a given array of integers contains any duplicate element.
assert test_duplicate_dict_2(([1,2,3,4,5]))==False
"""
def test_duplicate_dict_2(arr):
    d={}
    for i in arr:
        if i in d:
            return True
        d[i]=1
    return False

"""
Write a function to find whether a given array of integers contains any duplicate element.
assert test_duplicate_dict_3(([1,2,3,4,5]))==False
"""
def test_duplicate_dict_3(arr):
    d={}
    for i in arr:
        if i in d:
            return True
        d[i]=1
    return False

"""
Write a function to find whether a given array of integers contains any duplicate element.
assert test_duplicate_dict_4(([1,2,3,4,5]))==False
"""
def test_duplicate_dict_4(arr):
    d={}
    for i in arr:
        if i in d:
            return True
        d[i]=1
    return False

"""
Write a function to find whether a given array of integers contains any duplicate element.
assert test_duplicate_dict_5(([1,2,3,4,5]))==False
"""
def test_duplicate_dict_5(arr):
    d={}
    for i in arr:
        if i in d:
            return True
        d[i]=1
    return False

"""
Write a function to find whether a given array of integers contains any duplicate element.
assert test_duplicate_dict_6(([1,2,3,4,5]))==False
"""
def test_duplicate_dict_6(arr):
    d={}
    for i in arr:
        if i in d:
            return True
        d[i]=1
    return False

"""
Write a function to find whether a given array of integers contains any duplicate element.
assert test_duplicate_dict_7(([1,2,3,4,5]))==False
"""
def test_duplicate_dict_7(arr):
    d={}
    for i in arr:
        if i in d:
            return True
        d[i]=1
    return False

"""
Write a function to find whether a given array of integers contains any duplicate element.
assert test_duplicate_dict_8(([1,2,3,4,5]))==False
"""
def test_duplicate_dict_8(arr):
    d={}
    for i in arr:
        if i in d:
            return True
        d[i]=1
    return False

"""
Write a function to find whether a given array of integers contains any duplicate element.
assert test_duplicate_dict_9(([1,2,3,4,5]))==False
"""
def test_duplicate_dict_9(arr):
    d={}
    for i in arr:
        if i in d:
            return True
        d[i]=1
    return False

"""
Write a function to find whether a given array of integers contains any duplicate element.
assert test_duplicate_dict_10(([1,2,3,4,5]))==False
"""
def test_duplicate_dict_10(arr):
    d={}
    for i in arr:
        if i in d:
            return True
        d[i]=1
    return False

"""
Write a function to find whether a given array of integers contains any duplicate element.
assert test_duplicate_dict_11(([1,2,3,4,5]))==False
"""