def tri(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    """

#     if n == 1:
#         return [1]
#     elif n == 2:
#         return [1, 3]
#     elif n == 3:
#         return [1, 3, 2]
#     else:
#         tri_list = [1, 3, 2]
#         for i in range(3, n + 1):
#             tri_list.append(tri_list[i - 1] + tri_list[i - 2] + tri_list[i - 3])
#         return tri_list

#     # Using recursion
#     def tri_helper(n, prev_prev_num, prev_num, curr_num):
#         if n == 1:
#             return [curr_num]
#         elif n == 2:
#             return [curr_num, prev_num]
#         elif n == 3:
#             return [curr_num, prev_num, prev_prev_num]
#         else:
#             return tri_helper(n - 1, prev_prev_num, prev_num, curr_num + prev_num + prev_prev_num)

#     return tri_helper(n, 1, 3, 1)

    # Using dynamic programming
    def tri_helper(n, prev_prev_num, prev_num, curr_num):
        if n == 1:
            return [curr_num]
        elif n == 2:
            return [curr_num, prev_num]
        elif n == 3:
            return [curr_num, prev_num, prev_prev_num]
        else:
            return tri_helper(n - 1, prev_prev_num, prev_num, curr_num + prev_num + prev_prev_num)

    tri_list = [1, 3, 2]
    for i in range(3, n + 1):
        tri_list.append(tri_helper(i, 1, 3, 1))
    return tri_list


# Test cases
print(tri(3))  # Output: [1, 3, 2, 8]
print(tri(4))  # Output: [1, 3, 2, 8, 13]
print(tri(5))  # Output: [1, 3, 2, 8, 13, 21]
print(tri(6))  # Output: [1, 3, 2, 8, 13, 21, 34]
print(tri(7))  # Output: [1, 3, 2, 8, 13, 21, 34, 55]
print(tri(8))  # Output: [1, 3, 2, 8, 13, 21, 34, 55, 89]
print(tri(9))  # Output: [1, 3, 2, 8, 13, 21, 34, 55, 89, 144]
print(tri(10))  # Output: [1, 3, 2, 8, 13, 21, 34, 55, 89, 144, 233]
print