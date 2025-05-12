def rounded_avg(n, m):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    """
    if n > m:
        return -1
    else:
        return bin(round(sum(range(n, m + 1)) / (m - n + 1)))[2:]


def test_function(test_case):
    print(rounded_avg(test_case[0], test_case[1]))


test_function([1, 5])
test_function([7, 5])
test_function([10, 20])
test_function([20, 33])
test_function([1, 1])
test_function([1, 2])
test_function([2, 1])
test_function([1, 3])
test_function([3, 1])
test_function([1, 4])
test_function([4, 1])
test_function([1, 5])
test_function([5, 1])
test_function([1, 6])
test_function([6, 1])
test_function([1, 7])
test_function([7, 1])
test_function([1, 8])
test_function([8, 1])
test_function([1, 9])
test_function([9, 1])
test_function([1, 10])
test_function([10, 1])
test_function([1, 11])
test_function([11, 1])
test_function([1, 12])
test_function([12, 1])
test_function([1, 13])
test_function([13, 1])
test_function([1, 14])
test_function([14, 1])
test_function([1, 15])
test_function([15, 1])
test_function([1, 16])
test_function([16, 1])
test_function([1, 17])
test_function([17, 1])
test_function([1, 18])
test_function([18, 1])
test_function([1, 19])
test_function([19, 1])
test_function([1, 20])
test_function([20, 1])
test_function([1, 21])
test_function([21, 1])
test_function([1, 22])
test_function([22, 1])
test_function([1, 23])
test_function([23, 1])
test_function([1, 24])
test_function([24, 1])
test_function([1, 25])
test_function([25, 1])
test_function([1, 26])
test_function([26, 1])
test_function([1, 27])
test_function([27, 1])
test_function([1, 28])
test_function([28, 1])
test_function([1, 29])
test_function([29, 1])
test_function([1, 30])
test_function([30, 1])
test_function([1, 31])
test_function([31, 1])
test_function([1, 32])
test_function([32, 1])
test_function([1, 33])
test_function([33, 1])
test_function([1, 34])
test_function([34, 1])
test_function([1, 35])