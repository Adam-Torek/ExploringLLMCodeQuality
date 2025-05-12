"""
Write a function to find area of a sector. The function takes the radius and angle as inputs. Function should return None if the angle is larger than 360 degrees.
assert sector_area(4,45)==6.283185307179586
"""


def sector_area(radius, angle):
    if angle > 360:
        return None
    else:
        return radius * radius * angle * (angle - 90) / 360


print(sector_area(4, 45))
print(sector_area(4, 90))
print(sector_area(4, 180))
print(sector_area(4, 270))
print(sector_area(4, 360))
print(sector_area(4, 361))
print(sector_area(4, 362))
print(sector_area(4, 363))
print(sector_area(4, 364))
print(sector_area(4, 365))
print(sector_area(4, 366))
print(sector_area(4, 367))
print(sector_area(4, 368))
print(sector_area(4, 369))
print(sector_area(4, 370))
print(sector_area(4, 371))
print(sector_area(4, 372))
print(sector_area(4, 373))
print(sector_area(4, 374))
print(sector_area(4, 375))
print(sector_area(4, 376))
print(sector_area(4, 377))
print(sector_area(4, 378))
print(sector_area(4, 379))
print(sector_area(4, 380))
print(sector_area(4, 381))
print(sector_area(4, 382))
print(sector_area(4, 383))
print(sector_area(4, 384))
print(sector_area(4, 385))
print(sector_area(4, 386))
print(sector_area(4, 387))
print(sector_area(4, 388))
print(sector_area(4, 389))
print(sector_area(4, 390))
print(sector_area(4, 391))
print(sector_area(4, 392))
print(sector_area(4, 393))
print(sector_area(4, 394))
print(sector_area(4, 395))
print(sector_area(4, 396))
print(sector_area(4, 397))
print(sector_area(4, 398))
print(sector_area(4, 399))
print(sector_area(4, 400))
print(sector_area(4, 401))
print(sector_area(4, 402))
print(sector_area(4, 403))
print(sector_area(4, 404))
print(sector_area(4, 405))
print(sector_area(4, 406))
print(sector_area(4, 407))
print(sector_area(4, 408))
print(sector_area(4, 409))
print(sector_area(4, 410))
print(sector_area(4, 411))
print(sector_area(4