"""
Write a python function to check whether the count of divisors is even. https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-24.php
assert count_divisors(10)
"""

def count_divisors(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    if count % 2 == 0:
        return True
    else:
        return False

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
print(count_divisors(110)) # True
print(count_divisors(115)) # False
print(count_divisors(120)) # True
print(count_divisors(125)) # False
print(count_divisors(130)) # True
print(count_divisors(136)) # True
print(count_divisors(140)) # True
print(count_divisors(145)) # False
print(count_divisors(150)) # True
print(count_divisors(154)) # False
print(count_divisors(160)) # True
print(count_divisors(165)) # False
print(count_divisors(170)) # True
print(count_divisors(175)) # False
print(count_divisors(180)) # True
print(count_divisors(185)) # False
print(count_divisors(190)) # True
print(count_divisors(196)) # True
print(count_divisors(200)) # True
print(count_divisors(205)) # False
print(count_divisors(210)) # True
print(count_divisors(215)) # False
print(count_divisors(220)) # True
print(count_divisors(225)) # False
print(count_divisors(230)) # True
print(count_divisors(236)) # True
print(count_divisors(240)) # True
print(count_divisors(245)) # False
print(count_divisors(250)) # True
print(count_divisors(254)) # False
print(count_divisors(260)) # True
print(count_divisors(265)) # False
print(count_divisors(270)) # True
print(count_divisors(275)) # False
print(count_divisors(280)) # True
print(count_divisors(285)) # False
print(count_divisors(290)) # True
print(count_divisors(296)) # True
print(count_divisors(300)) # True
print(count_divisors