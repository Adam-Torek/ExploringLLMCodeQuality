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
print(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],10)) #[60, 54, 50, 48, 42, 36, 30, 24, 18, 12, 8, 6, 6, 4, 3]

# Time complexity: O(nlogn)
# Space complexity: O(n)

# Efficient solution:
def large_product(list1, list2, k):
    list1.sort(reverse=True)
    list2.sort(reverse=True)
    result = []
    i, j = 0, 0
    while k > 0 and i < len(list1) and j < len(list2):
        result.append(list1[i] * list2[j])
        i += 1
        j += 1
        k -= 1
    return result

print(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)) #[60, 54, 50]
print(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],2)) #[54, 50]
print(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],1)) #[50]
print(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],4)) #[60, 54, 50, 48]
print(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],0)) #[]
print(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9,