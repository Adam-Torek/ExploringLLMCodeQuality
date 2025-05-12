"""
Write a python function to check whether the count of divisors is even. https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-24.php
assert count_divisors(10)
"""

def count_divisors(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count % 2 == 0

print(count_divisors(10)) # True
print(count_divisors(15)) # False
print(count_divisors(20)) # True
print(count_divisors(24)) # True
print(count_divisors(25)) # False
print(count_divisors(30)) # True
print(count_divisors(36)) # True
print(count_divisors(40)) # True
print(count_divisors(45)) # False
print(count_divisors(50)) # True
print(count_divisors(54)) # False
print(count_divisors(60)) # True
print(count_divisors(65)) # False
print(count_divisors(70)) # True
print(count_divisors(75)) # False
print(count_divisors(80)) # True
print(count_divisors(85)) # False
print(count_divisors(90)) # True
print(count_divisors(96)) # True
print(count_divisors(100)) # True
print(count_divisors(105)) # False
print(count_divisors(120)) # True
print(count_divisors(125)) # False
print(count_divisors(150)) # True
print(count_divisors(155)) # False
print(count_divisors(180)) # True
print(count_divisors(185)) # False
print(count_divisors(200)) # True
print(count_divisors(205)) # False
print(count_divisors(240)) # True
print(count_divisors(245)) # False
print(count_divisors(250)) # True
print(count_divisors(270)) # True
print(count_divisors(275)) # False
print(count_divisors(300)) # True
print(count_divisors(305)) # False
print(count_divisors(360)) # True
print(count_divisors(365)) # False
print(count_divisors(400)) # True
print(count_divisors(405)) # False
print(count_divisors(450)) # True
print(count_divisors(455)) # False
print(count_divisors(500)) # True
print(count_divisors(505)) # False
print(count_divisors(540)) # True
print(count_divisors(545)) # False
print(count_divisors(600)) # True
print(count_divisors(605)) # False
print(count_divisors(650)) # True
print(count_divisors(655)) # False
print(count_divisors(720)) # True
print(count_divisors(725)) # False
print(count_divisors(750)) # True
print(count_divisors(755)) # False
print(count_divisors(800)) # True
print(count_divisors(805)) # False
print(count_divisors(850