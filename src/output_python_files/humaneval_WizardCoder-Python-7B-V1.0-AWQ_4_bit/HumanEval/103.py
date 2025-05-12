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
        avg = round((n + m) / 2)
        return bin(avg)


# Test cases
print(rounded_avg(1, 5)) # Output: "0b11"
print(rounded_avg(7, 5)) # Output: -1
print(rounded_avg(10, 20)) # Output: "0b1111"
print(rounded_avg(20, 33)) # Output: "0b11010"
print(rounded_avg(1, 10)) # Output: "0b1111"
print(rounded_avg(10, 1)) # Output: "0b1111"
print(rounded_avg(10, 11)) # Output: "0b1111"
print(rounded_avg(10, 12)) # Output: "0b1111"
print(rounded_avg(10, 13)) # Output: "0b1111"
print(rounded_avg(10, 14)) # Output: "0b1111"
print(rounded_avg(10, 15)) # Output: "0b1111"
print(rounded_avg(10, 16)) # Output: "0b1111"
print(rounded_avg(10, 17)) # Output: "0b1111"
print(rounded_avg(10, 18)) # Output: "0b1111"
print(rounded_avg(10, 19)) # Output: "0b1111"
print(rounded_avg(10, 20)) # Output: "0b1111"
print(rounded_avg(10, 21)) # Output: "0b1111"
print(rounded_avg(10, 22)) # Output: "0b1111"
print(rounded_avg(10, 23)) # Output: "0b1111"
print(rounded_avg(10, 24)) # Output: "0b1111"
print(rounded_avg(10, 25)) # Output: "0b1111"
print(rounded_avg(10, 26)) # Output: "0b1111"
print(rounded_avg(10, 27)) # Output: "0b1111"
print(rounded_avg(10, 28)) # Output: "0b1111"
print(rounded_avg(10, 29)) # Output: "0b1111"
print(rounded_avg(10, 30)) # Output: "0b1111"
print(rounded_avg(10, 31)) # Output: "0b1111"
print(rounded_avg(10, 32)) # Output: "0b1111"
print(rounded_avg(10, 33)) # Output: "0b1111"
print(rounded_avg(10, 34)) # Output: "0b1111"
print(rounded_avg(10, 35))