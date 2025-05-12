"""
Write a function to find the sum of the largest contiguous sublist in the given list.
assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
"""

def max_sub_array_sum(arr, k):
    """
    :param arr: list of integers
    :param k: integer
    :return: integer
    """
    # TODO: Write your code here
    max_sum = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            if sum > max_sum:
                max_sum = sum
    return max_sum

if __name__ == '__main__':
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8))
/src/main/java/com/github/hcsp/controlflow/Main.java
package com.github.hcsp.controlflow;

public class Main {
    public static void main(String[] args) {
        System.out.println(isLeapYear(2019));
        System.out.println(isLeapYear(2020));
        System.out.println(isLeapYear(2021));
        System.out.println(isLeapYear(2022));
        System.out.println(isLeapYear(2023));
        System.out.println(isLeapYear(2024));
        System.out.println(isLeapYear(2025));
        System.out.println(isLeapYear(2026));
        System.out.println(isLeapYear(2027));
        System.out.println(isLeapYear(2028));
        System.out.println(isLeapYear(2029));
        System.out.println(isLeapYear(2030));
        System.out.println(isLeapYear(2031));
        System.out.println(isLeapYear(2032));
        System.out.println(isLeapYear(2033));
        System.out.println(isLeapYear(2034));
        System.out.println(isLeapYear(2035));
        System.out.println(isLeapYear(2036));
        System.out.println(isLeapYear(2037));
        System.out.println(isLeapYear(2038));
        System.out.println(isLeapYear(2039));
        System.out.println(isLeapYear(2040));
        System.out.println(isLeapYear(2041));
        System.out.println(isLeapYear(2042));
        System.out.println(isLeapYear(2043));
        System.out.println(isLeapYear(2044));
        System.out.println(isLeapYear(2045));
        System.out.println(isLeapYear(2046));
        System.out.println(isLeapYear(2047));
        System.out.println(isLeapYear(2048));
        System.out.println(isLeapYear(2049));
        System.out.println(isLeapYear(2050));
        System.out.println(isLeapYear(2051));
        System.out.println(isLeapYear(2052));
        System.out.println(isLeapYear(2053));
        System.out.println(isLeapYear(2054));
        System.out.println(isLeapYear(2055));
        System.out.println(isLeapYear(2056));
        System.out.println(isLeapYear(2057));
        System.out.println(isLeapYear(2058));
        System.out.println(isLeapYear(2059));
        System.out.println(isLeapYear(2060));
        System.out.println(isLeapYear(2061));
        System.out.println(isLeapYear(2062));
        System.out.println(