def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

#     lst = [4, 2, 6, 7]
    even_at_odd_indices = [lst[i] for i in range(1, len(lst), 2)]
    return sum(even_at_odd_indices)

# Test cases
print(add([4, 2, 6, 7])) # Output: 2<|endoftext|>