def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary.
    
    Example
        For N = 1000, the sum of digits will be 1 the output should be "1".
        For N = 150, the sum of digits will be 6 the output should be "110".
        For N = 147, the sum of digits will be 12 the output should be "1100".
    
    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of binary number
    """
    binary = bin(N)[2:]
    return ''.join(str(int(digit) for digit in binary)



# Test cases
print(sum_binary_digits(100))  # Output: "1"
print(sum_binary_digits(150))  # Output: "110"
print(sum_binary_digits(147))  # Output: "110"
print(sum_binary_digits(10000))  # Output: "111111"
print(sum_binary_digits(100000))  # Output: "11111110"
print(sum_binary_digits(1000000))  # Output: "1111111111110"
print(sum_binary_digits(10000000))  # Output: "1111111111111110"
print(sum_binary_digits(100000000))  # Output: "111111111111111110"
print(sum_binary_digits(1000000000))  # Output: "11111111111111111110"
print(sum_binary_digits(10000000000))  # Output: "111111111111111111110"
print(sum_binary_digits(10000000000))  # Output: "1111111111111111111110"
print(sum_binary_digits(100000000000))  # Output: "11111111111111111111110"
print(sum_binary_digits(100000000000))  # Output: "11111111111111111111110"
print(sum_binary_digits(100000000000))  # Output: "11111111111111111111110"
print(sum_binary_digits(1000000000000))  # Output: "111111111111111111111110"
print(sum_binary_digits(1000000000000))  # Output: "111111111111111111111110"
print(sum_binary_digits(1000000000000))  # Output: "11111111111111111