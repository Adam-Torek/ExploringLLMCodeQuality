"""
Write a python function to count the number of substrings with the sum of digits equal to their length.
assert count_Substrings('112112') == 6
"""


def count_Substrings(string):
    count = 0
    for i in range(len(string)):
        for j in range(i, len(string)):
            if sum(int(x) for x in string[i:j+1]) == j-i+1:
                count += 1
    return count


if __name__ == '__main__':
    print(count_Substrings('112112'))
    print(count_Substrings('111111'))
    print(count_Substrings('1111111'))
    print(count_Substrings('11111111'))
    print(count_Substrings('111111111'))
    print(count_Substrings('1111111111'))
    print(count_Substrings('11111111111'))
    print(count_Substrings('111111111111'))
    print(count_Substrings('1111111111111'))
    print(count_Substrings('11111111111111'))
    print(count_Substrings('111111111111111'))
    print(count_Substrings('1111111111111111'))
    print(count_Substrings('11111111111111111'))
    print(count_Substrings('111111111111111111'))
    print(count_Substrings('1111111111111111111'))
    print(count_Substrings('11111111111111111111'))
    print(count_Substrings('111111111111111111111'))
    print(count_Substrings('1111111111111111111111'))
    print(count_Substrings('11111111111111111111111'))
    print(count_Substrings('111111111111111111111111'))
    print(count_Substrings('1111111111111111111111111'))
    print(count_Substrings('11111111111111111111111111'))
    print(count_Substrings('111111111111111111111111111'))
    print(count_Substrings('1111111111111111111111111111'))
    print(count_Substrings('11111111111111111111111111111'))
    print(count_Substrings('111111111111111111111111111111'))
    print(count_Substrings('1111111111111111111111111111111'))
    print(count_Substrings('11111111111111111111111111111111'))
    print(count_Substrings('111111111111111111111111111111111'))
    print(count_Substrings('1111111111111111111111111111111111'))