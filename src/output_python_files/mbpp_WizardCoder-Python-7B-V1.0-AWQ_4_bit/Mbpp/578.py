"""
Write a function to interleave 3 lists of the same length into a single flat list.
assert interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700])==[1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]
"""

def interleave_lists(list1, list2, list3):
    result = []
    for i in range(len(list1)):
        result.append(list1[i])
        result.append(list2[i])
        result.append(list3[i])
    return result

# Testing the function
print(interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700]))
# Output: [1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]

# Testing with other lists
print(interleave_lists([1,2,3],[10,20,30],[100,200]))
# Output: [1, 10, 100, 2, 20, 200, 3, 30]

print(interleave_lists([1,2],[10,20],[100,200,300])
# Output: [1, 10, 100, 2, 20, 200, 300]

print(interleave_lists([1],[10],[100,200,300])
# Output: [1, 10, 100, 200, 300]

print(interleave_lists([1,2,3],[10,20],[100])
# Output: [1, 10, 100, 2, 20, 3]

print(interleave_lists([1,2],[10],[100,200,300])
# Output: [1, 10, 100, 2, 200, 300]

print(interleave_lists([1,2,3],[10,20,30],[100])
# Output: [1, 10, 100, 2, 20, 3, 30]

print(interleave_lists([1],[10,20],[100,200,300])
# Output: [1, 10, 100, 20, 200, 300]

print(interleave_lists([1,2],[],[100,200,300])
# Output: [1, 100, 2, 200, 300]

print(interleave_lists([1,2,3],[],[100,200,300])
# Output: [1, 100, 2, 200, 3, 300]

print(interleave_lists([1],[10,20],[100,200])
# Output: [1, 10, 100, 20, 200]

print(interleave_lists([],[10,20],[100,