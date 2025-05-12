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
    lst1 = lst1.copy()
    lst2 = lst2.copy()
    while True:
        for i in range(len(lst1)):
            if lst1[i] % 2 != 0:
                for j in range(len(lst2)):
                    if lst2[j] % 2 == 0:
                        lst1[i], lst2[j] = lst2[j], lst1[i]
                        break
                else:
                    continue
                break
        else:
            return "YES"
        break
    return "NO"

# Test cases
print(exchange([1, 2, 3, 4], [1, 2, 3, 4])) # YES
print(exchange([1, 2, 3, 4], [1, 5, 3, 4])) # NO
print(exchange([1, 2, 3, 4], [1, 2, 5, 4])) # YES
print(exchange([1, 2, 3, 4], [1, 2, 3, 5])) # NO
print(exchange([1, 2, 3, 4], [1, 2, 3, 6])) # YES
print(exchange([1, 2, 3, 4], [1, 2, 3, 7])) # NO
print(exchange([1, 2, 3, 4], [1, 2, 3, 8])) # YES
print(exchange([1, 2, 3, 4], [1, 2, 3, 9])) # NO
print(exchange([1, 2, 3, 4], [1, 2, 3, 10])) # YES
print(exchange([1, 2, 3, 4], [1, 2, 3, 11])) # NO
print(exchange([1, 2, 3, 4], [1, 2, 3, 12])) # YES
print(exchange([1, 2, 3, 4], [1, 2, 3, 13])) # NO
print(exchange([1, 2, 3, 4], [1, 2, 3, 14])) # YES
print(exchange([1, 2, 3, 4], [1, 2, 3, 15])) # NO
print(exchange([1, 2, 3, 4], [1, 2, 3, 16])) # YES
print(exchange([1, 2, 3, 4], [1, 2, 3, 17])) # NO
print(exchange([1, 2, 3, 4], [1, 2, 3, 18])) # YES
print(exchange([1, 2, 3, 4], [1, 2, 3, 19])) # NO
print(exchange([1, 2, 3, 4], [1, 2, 3, 20])) # YES
print(exchange([1, 2, 3, 4], [1, 2, 3, 21])) # NO
print(exchange([1,