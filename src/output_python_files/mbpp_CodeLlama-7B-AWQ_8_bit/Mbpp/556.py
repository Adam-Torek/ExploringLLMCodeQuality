"""
Write a python function to count the number of pairs whose xor value is odd.
assert find_Odd_Pair([5,4,7,2,1],5) == 6
"""


def find_Odd_Pair(arr, n):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] ^ arr[j] == n:
                count += 1
    return count


if __name__ == '__main__':
    print(find_Odd_Pair([5, 4, 7, 2, 1], 5))
    print(find_Odd_Pair([1, 2, 3, 4, 5], 5))
    print(find_Odd_Pair([1, 2, 3, 4, 5], 6))
    print(find_Odd_Pair([1, 2, 3, 4, 5], 7))
    print(find_Odd_Pair([1, 2, 3, 4, 5], 8))
    print(find_Odd_Pair([1, 2, 3, 4, 5], 9))
    print(find_Odd_Pair([1, 2, 3, 4, 5], 10))
    print(find_Odd_Pair([1, 2, 3, 4, 5], 11))
    print(find_Odd_Pair([1, 2, 3, 4, 5], 12))
    print(find_Odd_Pair([1, 2, 3, 4, 5], 13))
    print(find_Odd_Pair([1, 2, 3, 4, 5], 14))
    print(find_Odd_Pair([1, 2, 3, 4, 5], 15))
    print(find_Odd_Pair([1, 2, 3, 4, 5], 16))
    print(find_Odd_Pair([1, 2, 3, 4, 5], 17))
    print(find_Odd_Pair([1, 2, 3, 4, 5], 18))
    print(find_Odd_Pair([1, 2, 3, 4, 5], 19))
    print(find_Odd_Pair([1, 2, 3, 4, 5], 20))
    print(find_Odd_Pair([1, 2, 3, 4, 5], 21))
    print(find_Odd_Pair([1, 2, 3, 4, 5], 22))
    print(find_Odd_Pair([1, 2, 3, 4, 5], 23))
    print(find_Odd_Pair([1, 2, 3, 4, 5], 24))
    print(find_Odd_Pair([1, 2, 3, 4, 5], 25))
    print(find_Odd_Pair([1, 2, 3, 4, 5], 26))
    print(find_Odd_Pair([1, 2, 3, 4, 5], 27))
    print(find_Odd_Pair([1, 2, 3, 4, 5], 28))
    print(find_Odd_Pair([1, 2, 3, 4, 5], 29))
    print(find_Odd_Pair([1, 2, 3, 4, 5], 30))
    print(find_Odd_Pair([1, 2, 3, 4, 5], 31))
    print(find_Odd_Pair([1, 2, 3, 4, 5], 32))
    print(find_Odd_Pair([1, 2, 3, 4, 5], 33))
    print(find_Odd_Pair([1, 2, 3, 4, 5], 34))
    print