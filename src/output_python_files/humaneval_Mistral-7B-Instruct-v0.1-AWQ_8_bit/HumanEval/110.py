def exchange(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    It is assumed that the input lists will be non-empty.
    """
    # check if lst1 is all even
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    # check if lst2 is all even
    if all(num % 2 == 0 for num in lst2):
        return "YES"
    # check if lst1 has an odd number
    if any(num % 2 != 0 for num in lst1):
        # check if lst2 has an even number
        if any(num % 2 == 0 for num in lst2):
            # swap the odd number from lst1 with the even number from lst2
            lst1.pop(lst1.index(min(lst1, key=lambda x: (x % 2 != 0))))
            lst2.pop(lst2.index(min(lst2, key=lambda x: (x % 2 == 0))))
            return "YES"
        # if lst2 doesn't have an even number, return NO
        return "NO"
    # if lst1 doesn't have an odd number, return NO
    return "NO"

# test the function
lst1 = [1, 2, 3, 4]
lst2 = [1, 2, 3, 4]
print(exchange(lst1, lst2)) # YES
lst1 = [1, 2, 3, 4]
lst2 = [1, 5, 3, 4]
print(exchange(lst1, lst2)) # NO
lst1 = [1, 2, 3, 4]
lst2 = [1, 2, 3, 5]
print(exchange(lst1, lst2)) # NO