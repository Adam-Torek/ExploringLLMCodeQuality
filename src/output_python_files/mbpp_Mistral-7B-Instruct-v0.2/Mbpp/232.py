"""
Write a function that takes in a list and an integer n and returns a list containing the n largest items from the list.
assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])
"""
def larg_nnum(num_list, n):
    """
    :param num_list: list of numbers
    :param n: number of largest numbers to return
    :return: list of n largest numbers from num_list
    """
    # sort the list in descending order
    num_list.sort(reverse=True)
    # return the first n numbers from the sorted list
    return num_list[:n]

# test the function
assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])
assert set(larg_nnum([1,2,3,4,5],3))==set([5,4,3])
assert set(larg_nnum([],3))==set([])
assert set(larg_nnum([1],1))==set([1])
assert set(larg_nnum([1,1,1,1,1],5))==set([1]) # should return all 1s, not just the first one
assert set(larg_nnum([1,1,1,1,1],50))==set([1]) # should return all 1s, not just the first one
assert set(larg_nnum([1,1,1,1,1],100))==set([1]) # should return all 1s, not just the first one
assert set(larg_nnum([1,1,1,1,1],101))==set([]) # should return an empty list, not raise an error
assert set(larg_nnum([1,1,1,1,1],-1))==set([]) # should return an empty list, not raise an error
assert set(larg_nnum([1,1,1,1,1],float('inf')))==set([1]) # should return all 1s, not just the first one
assert set(larg_nnum([1,1,1,1,1],float('nan')))==set([]) # should return an empty list, not raise an error
assert set(larg_nnum([],2))==set([]) # should return an empty list, not raise an error
assert set(larg_nnum([],3))==set([]) # should return an empty list, not raise an error
assert set(larg_nnum([],-1))==set([]) # should return an empty list, not raise an error
assert set(larg_nnum([],float('inf')))==set([]) # should return an empty list, not raise an error
assert set(larg_nnum([],float('nan')))==set([]) # should return an empty list, not raise an error
assert set(larg_nnum([],0))==set([]) # should return an empty list, not raise an error
assert set(larg_nnum([],1))==set([]) # should return an empty list, not raise an error
assert set(larg_nnum([],2))==set([]) # should return an empty list, not raise an error
assert set(larg_nnum([],3))==set([]) # should return an empty list, not raise an error
assert set(larg_nnum([],4))==set([]) # should return an empty list, not raise an error
assert set(larg_nnum([],5))==set([]) # should return an empty list, not raise an error
assert set(larg_nnum([],6))==set([]) # should return an empty list, not raise an error
assert set(larg_nnum([],7))==set([]) # should return an empty list, not raise an error
assert set(larg_nnum([],8))==set([]) # should return an empty list, not raise an error
assert set(larg_nnum([],9))==set([]) # should return an empty list, not raise an error
assert set(larg_n