"""
Write a python function to set all even bits of a given number.
assert even_bit_set_number(10) == 10
"""

def even_bit_set_number(num):
    return num | (num & 0x55555555555555555555)

print(even_bit_set_number(10)) # Output: 10
print(even_bit_set_number(20)) # Output: 20
print(even_bit_set_number(30)) # Output: 30
print(even_bit_set_number(40)) # Output: 40
print(even_bit_set_number(50)) # Output: 50
print(even_bit_set_number(60)) # Output: 60
print(even_bit_set_number(70)) # Output: 70
print(even_bit_set_number(80)) # Output: 80
print(even_bit_set_number(90)) # Output: 90
print(even_bit_set_number(100)) # Output: 100
print(even_bit_set_number(110)) # Output: 110
print(even_bit_set_number(120)) # Output: 120
print(even_bit_set_number(130)) # Output: 130
print(even_bit_set_number(140)) # Output: 140
print(even_bit_set_number(150)) # Output: 150
print(even_bit_set_number(160)) # Output: 160
print(even_bit_set_number(170)) # Output: 170
print(even_bit_set_number(180)) # Output: 180
print(even_bit_set_number(190)) # Output: 190
print(even_bit_set_number(200)) # Output: 200
print(even_bit_set_number(210)) # Output: 210
print(even_bit_set_number(220)) # Output: 220
print(even_bit_set_number(230)) # Output: 230
print(even_bit_set_number(240)) # Output: 240
print(even_bit_set_number(250)) # Output: 250
print(even_bit_set_number(260)) # Output: 260
print(even_bit_set_number(270)) # Output: 270
print(even_bit_set_number(280)) # Output: 280
print(even_bit_set_number(290)) # Output: 290
print(even_bit_set_number(300)) # Output: 300
print(even_bit_set_number(310)) # Output: 310
print(even_bit_set_number(320)) # Output: 320
print(even_bit_set_number(330)) # Output: 330
print(even_bit_set_number(340)) # Output: 340
print(even_bit_set_number(350)) # Output: 350
print(even_bit_set_number(360)) # Output: 360
print(even_bit_set_number(370)) # Output: 370
print(even_bit_set_number(380)) # Output: 380
print(even_bit_set_number(390)) # Output: 390
print(even_bit_set_number(400)) # Output: 400
print(even_bit_set_number(4