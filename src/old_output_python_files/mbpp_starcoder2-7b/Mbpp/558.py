"""
Write a python function to find the sum of the per-digit difference between two integers.
assert digit_distance_nums(1,2) == 1
"""

def digit_distance_nums(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    if len(num1)!= len(num2):
        return "The numbers are not the same length"
    else:
        sum = 0
        for i in range(len(num1)):
            sum += abs(int(num1[i]) - int(num2[i]))
        return sum

print(digit_distance_nums(1,2))
print(digit_distance_nums(1,10))
print(digit_distance_nums(1,100))
print(digit_distance_nums(1,1000))
print(digit_distance_nums(1,10000))
print(digit_distance_nums(1,100000))
print(digit_distance_nums(1,1000000))
print(digit_distance_nums(1,10000000))
print(digit_distance_nums(1,100000000))
print(digit_distance_nums(1,1000000000))
print(digit_distance_nums(1,10000000000))
print(digit_distance_nums(1,100000000000))
print(digit_distance_nums(1,1000000000000))
print(digit_distance_nums(1,10000000000000))
print(digit_distance_nums(1,100000000000000))
print(digit_distance_nums(1,1000000000000000))
print(digit_distance_nums(1,10000000000000000))
print(digit_distance_nums(1,100000000000000000))
print(digit_distance_nums(1,1000000000000000000))
print(digit_distance_nums(1,10000000000000000000))
print(digit_distance_nums(1,100000000000000000000))
print(digit_distance_nums(1,1000000000000000000000))
print(digit_distance_nums(1,10000000000000000000000))
print(digit_distance_nums(1,100000000000000000000000))
print(digit_distance_nums(1,1000000000000000000000000))
print(digit_distance_nums(1,10000000000000000000000000))
print(digit_distance_nums(1,100000000000000000000000000))
print(digit_distance_nums(1,1000000000000000000000000000))
print(digit_distance_nums(1,10000000000000000000000000000))
print(digit_distance_nums(1,100000000000000000000000000000))
print(digit_distance_nums(1,1000000000000000000000000000000))
print(digit_distance_nums(1,10000000