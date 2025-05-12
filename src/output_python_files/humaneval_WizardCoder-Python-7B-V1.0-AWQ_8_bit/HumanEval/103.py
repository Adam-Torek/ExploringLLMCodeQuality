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
print(rounded_avg(1, 5)) # should return "0b11"
print(rounded_avg(7, 5)) # should return -1
print(rounded_avg(10, 20)) # should return "0b1111"
print(rounded_avg(20, 33)) # should return "0b11010"
print(rounded_avg(1, 10)) # should return "0b1111"
print(rounded_avg(10, 1)) # should return "0b1111"
print(rounded_avg(10, 11)) # should return "0b1111"
print(rounded_avg(10, 12)) # should return "0b11110"
print(rounded_avg(10, 13)) # should return "0b11111"
print(rounded_avg(10, 14)) # should return "0b111110"
print(rounded_avg(10, 15)) # should return "0b111111"
print(rounded_avg(10, 16)) # should return "0b1111110"
print(rounded_avg(10, 17)) # should return "0b1111111"
print(rounded_avg(10, 18)) # should return "0b11111110"
print(rounded_avg(10, 19)) # should return "0b11111111"
print(rounded_avg(10, 20)) # should return "0b111111111"
print(rounded_avg(10, 21)) # should return "0b1111111110"
print(rounded_avg(10, 22)) # should return "0b1111111111"
print(rounded_avg(10, 23)) # should return "0b11111111110"
print(rounded_avg(10, 24)) # should return "0b11111111111"
print(rounded_avg(10, 25)) # should return "0b111111111110"
print(rounded_avg(10, 26)) # should return "0b111111111111"
print(rounded_avg(10, 27)) # should return "0b1111111111110"
print(rounded_avg(10, 28)) # should return "0b1111111111111"
print(rounded_avg(10, 29)) # should return "0b11111111111110"
print(rounded_avg(10, 30)) # should return "0b11111111111111"
print(rounded_avg(10, 31)) # should return