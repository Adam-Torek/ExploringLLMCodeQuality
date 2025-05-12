"""
Write a function to interleave 3 lists of the same length into a single flat list.
assert interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700])==[1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]
"""

def interleave_lists(lst1, lst2, lst3):
    """
    This function takes in 3 lists of the same length and returns a single flat list
    that contains all the elements from the 3 input lists.
    """
    flat_list = []
    for i in range(len(lst1)):
        flat_list.append(lst1[i])
        flat_list.append(lst2[i])
        flat_list.append(lst3[i])
    return flat_list

# test the function
assert interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700])==[1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]