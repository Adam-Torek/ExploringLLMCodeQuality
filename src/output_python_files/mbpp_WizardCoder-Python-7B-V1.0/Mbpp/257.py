"""
Write a function that takes in two numbers and returns a tuple with the second number and then the first number.
assert swap_numbers(10,20)==(20,10)
"""

def swap_numbers(a,b):
    return (b,a)

print(swap_numbers(10,20)) #Output: (20, 10)
print(swap_numbers(20,10)) #Output: (10, 20)
print(swap_numbers(30,40)) #Output: (40, 30)
print(swap_numbers(50,60)) #Output: (60, 50)
print(swap_numbers(70,80)) #Output: (80, 70)
print(swap_numbers(90,100)) #Output: (100, 90)