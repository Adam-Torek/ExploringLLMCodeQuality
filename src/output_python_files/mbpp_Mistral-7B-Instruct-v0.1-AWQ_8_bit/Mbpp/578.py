"""
Write a function to interleave 3 lists of the same length into a single flat list.
assert interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700])==[1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]
"""

def interleave_lists(lst1, lst2, lst3):
    """
    This function takes in 3 lists of the same length and returns a single flat list
    that is the interleaving of the 3 input lists.
    """
    # create an empty list to store the interleaved list
    interleaved_list = []
    # iterate through the input lists
    for i in range(len(lst1)):
        # append the element from the first list
        interleaved_list.append(lst1[i])
        # append the element from the second list
        interleaved_list.append(lst2[i])
        # append the element from the third list
        interleaved_list.append(lst3[i])
    # return the interleaved list
    return interleaved_list

# test the function
assert interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700])==[1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]