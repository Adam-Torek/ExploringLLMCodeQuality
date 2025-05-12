"""
Write a function to interleave 3 lists of the same length into a single flat list.
assert interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700])==[1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]
"""
def interleave_lists(lst1,lst2,lst3):
    result = []
    i = 0
    while i < len(lst1) or i < len(lst2) or i < len(lst3):
        if i < len(lst1):
            result.append(lst1[i])
        if i < len(lst2):
            result.append(lst2[i])
        if i < len(lst3):
            result.append(lst3[i])
        i += 1
    return result

assert interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700])==[1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]