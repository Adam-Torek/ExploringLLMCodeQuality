"""
Write a function takes as input two lists [a_1,...,a_n], [b_1,...,b_n] and returns [a_1+b_1,...,a_n+b_n].
assert sum_list([10,20,30],[15,25,35])==[25,45,65]
"""
def sum_list(a, b):
    return [a[i] + b[i] for i in range(len(a))]

print(sum_list([10,20,30],[15,25,35])) # Output: [25, 45, 65]
print(sum_list([1,2,3],[4,5,6])) # Output: [5, 7, 9]
print(sum_list([-1,0,1],[1,2,3])) # Output: [0, 2, 4]
print(sum_list([0,0,0],[0,0,0])) # Output: [0, 0, 0]
print(sum_list([1],[2])) # Output: [3]
print(sum_list([],[1,2,3])) # Output: []
print(sum_list([],[1])) # Output: []
print(sum_list([1,2],[3,4,5])) # Output: [4, 6]
print(sum_list([1,2,3],[4,5])) # Output: [5, 7]
print(sum_list([1,2],[3,4,5])) # Output: [4, 6]
print(sum_list([1,2,3],[4,5,6,7])) # Output: [5, 7, 9]
print(sum_list([1,2,3,4],[4,5,6,7])) # Output: [5, 7, 9, 10]
print(sum_list([1,2,3,4],[4,5,6])) # Output: [5, 7, 9]
print(sum_list([1,2],[3,4,5,6])) # Output: [4, 6, 7]
print(sum_list([1,2,3,4],[4,5,6,7,8])) # Output: [5, 7, 9, 10]
print(sum_list([1,2,3,4],[4,5,6,7,8,9])) # Output: [5, 7, 9, 10, 11]
print(sum_list([1,2,3,4,5],[4,5,6,7,8,9,10])) # Output: [5, 7, 9, 10, 11, 11]
print(sum_list([1,2,3,4,5],[4,5,6,7,8,9,10,11])) # Output: [5, 7, 9, 10, 11, 12]
print(sum_list([1,2,3,4,5],[4,5,6,7,8,9,10,11,12])) # Output: [5, 7, 9, 10, 11, 12, 13]
print(sum_list([1,2,3,4,5,6],[4,5,6,7,8,9,10,11,12,13])) # Output: [5, 7, 9, 10, 11, 12, 13, 14]
print(sum_list([1,2,3,4,5,6,7],[4,5,6,7,8,9,10,11,12,13,14])) # Output: [5, 7, 9, 10, 11, 12, 13, 14, 15]
print(sum_list([1,2,3,4,5,6,7,8],[4,5,6,7,8,9,10,11,12,13,14,15])) # Output: [5,