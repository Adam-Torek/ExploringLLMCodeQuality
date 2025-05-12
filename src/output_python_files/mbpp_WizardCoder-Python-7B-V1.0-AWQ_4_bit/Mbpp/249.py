"""
Write a function to find the intersection of two arrays.
assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])==[1, 2, 8, 9]
"""

def intersection_array(arr1, arr2):
    return list(set(arr1) & set(arr2))

print(intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])) #[1, 2, 8, 9]

#Alternative solution using list comprehension
def intersection_array(arr1, arr2):
    return [x for x in arr1 if x in arr2]

print(intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])) #[1, 2, 8, 9]

#Alternative solution using set intersection
def intersection_array(arr1, arr2):
    return list(set(arr1) & set(arr2))

print(intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])) #[1, 2, 8, 9]

#Alternative solution using list comprehension with set intersection
def intersection_array(arr1, arr2):
    return [x for x in set(arr1) if x in set(arr2)]

print(intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])) #[1, 2, 8, 9]

#Alternative solution using list comprehension with list intersection
def intersection_array(arr1, arr2):
    return [x for x in arr1 if x in arr2]

print(intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9]) #[1, 2, 8, 9]

#Alternative solution using list intersection
def intersection_array(arr1, arr2):
    return list(filter(lambda x: x in arr2, arr1))

print(intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9]) #[1, 2, 8, 9]

#Alternative solution using list intersection with set intersection
def intersection_array(arr1, arr2):
    return list(filter(lambda x: x in set(arr2), arr1)

print(intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9]) #[1, 2, 8, 9]

#Alternative solution using list intersection with set intersection
def intersection_array(arr1, arr2):
    return list(set(arr1) & set(arr2))

print(intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9]) #[1, 2, 8, 9]

#Alternative solution using list intersection with set intersection
def intersection_array(arr1, arr2):
    return list(set(arr1).intersection(set(arr2))

print(intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9]) #[1, 2, 8, 9]

#Alternative solution using set intersection with list intersection
def intersection_array(arr1, arr2):
    return list(set(arr1).intersection(set(arr2))

print(inter