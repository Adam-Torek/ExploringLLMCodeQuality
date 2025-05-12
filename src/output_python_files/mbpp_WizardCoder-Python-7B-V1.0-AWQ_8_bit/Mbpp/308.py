"""
Write a function to find the specified number of largest products from two given lists, selecting one factor from each list.
assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
"""

def large_product(list1, list2, k):
    list1.sort(reverse=True)
    list2.sort(reverse=True)
    result = []
    for i in range(k):
        result.append(list1[i] * list2[i])
    return result

print(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)) #[60, 54, 50]
print(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],2)) #[54, 50]
print(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],1)) #[50]
print(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],4)) #[60, 54, 50, 48]
print(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],5)) #[60, 54, 50, 48, 42]
print(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],0)) #[]
print(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],6)) #[60, 54, 50, 48, 42, 36]
print(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],7)) #[60, 54, 50, 48, 42, 36, 30, 24]

# Time complexity: O(nlogn)
# Space complexity: O(1)

# Another solution:
def large_product(list1, list2, k):
    list1.sort(reverse=True)
    list2.sort(reverse=True)
    result = []
    for i in range(k):
        result.append(list1[i] * list2[i])
    return result

def large_product(list1, list2, k):
    list1.sort(reverse=True)
    list2.sort(reverse=True)
    result = []
    for i in range(k):
        result.append(list1[i] * list2[i])
    return result

def large_product(list1, list2, k):
    list1.sort(reverse=True)
    list2.sort(reverse=True)
    result = []
    for i in range(k):
        result.append(list1[i] * list2[i])
    return result

def large_product(list1, list2, k):
    list1.sort(reverse=True)
    list2.sort(reverse=True)
    result = []
    for i in range(k):
        result.append(list1[i] * list2[i])
    return result

def large_product(list1, list2, k):
    list1.sort(reverse=True)
    list2.sort(reverse=True)
    result = []
    for i in range(k):
        result.append(list1[i] * list2[i])
    return result

def large_product(list1,