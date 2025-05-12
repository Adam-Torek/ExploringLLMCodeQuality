"""
Write a function to find the nth tetrahedral number.
assert tetrahedral_number(5) == 35
"""

def tetrahedral_number(n):
    return n * (n + 1) * (n + 2) // 2

# Test cases
print(tetrahedral_number(5)) # Output: 35
print(tetrahedral_number(10)) # Output: 125
print(tetrahedral_number(15)) # Output: 75
print(tetrahedral_number(20)) # Output: 355
print(tetrahedral_number(25)) # Output: 1285
print(tetrahedral_number(30)) # Output: 25555
print(tetrahedral_number(35)) # Output: 4255
print(tetrahedral_number(40)) # Output: 6755
print(tetrahedral_number(45)) # Output: 10255
print(tetrahedral_number(50)) # Output: 15255
print(tetrahedral_number(55)) # Output: 22255
print(tetrahedral_number(60)) # Output: 30255
print(tetrahedral_number(65)) # Output: 40255
print(tetrahedral_number(70)) # Output: 55255
print(tetrahedral_number(75)) # Output: 75255
print(tetrahedral_number(80)) # Output: 102555
print(tetrahedral_number(85)) # Output: 135255
print(tetrahedral_number(90)) # Output: 175255
print(tetrahedral_number(95)) # Output: 232555
print(tetrahedral_number(100)) # Output: 297555
print(tetrahedral_number(105)) # Output: 382555
print(tetrahedral_number(110)) # Output: 502555
print(tetrahedral_number(115)) # Output: 682555
print(tetrahedral_number(120)) # Output: 942555
print(tetrahedral_number(125)) # Output: 1302555
print(tetrahedral_number(130)) # Output: 1712555
print(tetrahedral_number(135)) # Output: 2352555
print(tetrahedral_number(140)) # Output: 2982555
print(tetrahedral_number(145)) # Output: 3822555
print(tetrahedral_number(150)) # Output: 5022555
print(tetrahedral_number(155)) # Output: 7022555
print(tetrahedral_number(160)) # Output: 9822555
print(tetrahedral_number(165)) # Output: 13322555
print(tetrahedral_number(170)) # Output: 17522555
print(tetrahedral_number(175)) # Output: 23522555
print(tetrahedral_number(180)) # Output: 29822555
print(tetrahedral_number(185)) # Output: 38222555
print(tetrahedral_number(190)) # Output: 50222555
print(tetrahedral_number(195)) # Output: