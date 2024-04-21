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
    lst1_even = [x for x in lst1 if x % 2 == 0]
    lst2_even = [x for x in lst2 if x % 2 == 0]
    if len(lst1_even) == len(lst1) and len(lst2_even) == len(lst2):
        return "YES"
    else:
        return "NO"


def main():
    lst1 = [1, 2, 3, 4]
    lst2 = [1, 2, 3, 4]
    print(exchange(lst1, lst2))


if __name__ == "__main__":
    main()
</s>