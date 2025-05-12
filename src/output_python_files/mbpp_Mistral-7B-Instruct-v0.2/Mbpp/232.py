"""
Write a function that takes in a list and an integer n and returns a list containing the n largest items from the list.
assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])
"""
def larg_nnum(numbers, n):
    """
    :param numbers: list of numbers
    :param n: number of largest numbers to return
    :return: list of n largest numbers from the input list
    """
    # sort the list in descending order
    numbers.sort(reverse=True)
    # return the first n numbers from the sorted list
    return numbers[:n]

# test the function
assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])
assert set(larg_nnum([1,2,3,4,5],3))==set([5,4,3])
assert set(larg_nnum([1,2,3,4,5],5))==set([5,4,3,2,1])
assert set(larg_nnum([],2))==set([])
assert set(larg_nnum([1],1))==set([1])
assert set(larg_nnum([1],10))==set([1])
assert set(larg_nnum([1,1,1,1,1,1,1,1,1,1,1],11))==set([1])
assert set(larg_nnum([1,1,1,1,1,1,1,1,1,1,1],12))==set([1])
assert set(larg_nnum([1,1,1,1,1,1,1,1,1,1,1],13))==set([1])
assert set(larg_nnum([1,1,1,1,1,1,1,1,1,1,1],14))==set([1])
assert set(larg_nnum([1,1,1,1,1,1,1,1,1,1,1],15))==set([1])
assert set(larg_nnum([1,1,1,1,1,1,1,1,1,1,1],16))==set([1])
assert set(larg_nnum([1,1,1,1,1,1,1,1,1,1,1],17))==set([1])
assert set(larg_nnum([1,1,1,1,1,1,1,1,1,1,1],18))==set([1])
assert set(larg_nnum([1,1,1,1,1,1,1,1,1,1,1],19))==set([1])
assert set(larg_nnum([1,1,1,1,1,1,1,1,1,1,1],20))==set([1])
assert set(larg_nnum([1,1,1,1,1,1,1,1,1,1,1],21))==set([1])
assert set(larg_nnum([1,1,1,1,1,1,1,1,1,1,1],22))==set([1])
assert set(larg_nnum([1,1,1,1,1,1,1,1,1,1,1],23))==set([1])
assert set(larg_nnum([1,1,1,1,1,1,1,1,1,1,1],24))==set([1])
assert set(larg_nnum([1,1,1,1,1,1,1,1,1,1,1],25))==set([1])
assert set(larg_nnum([1,1,1,1,1,1,1,1,1,1,1],26))==set([1])
assert set(larg_nnum([1,1,1,1,1,1,1,1,