"""
Write a function to convert a tuple to a string.
assert tup_string(('e', 'x', 'e', 'r', 'c', 'i','s', 'e','s'))==("exercises")
"""
def tup_string(tup):
    return ''.join(tup)

"""
Write a function to convert a list to a tuple.
assert list_tuple([1, 3, 5, 7, 9])== (1, 3, 5, 7, 9)
"""
def list_tuple(lst):
    return tuple(lst)

"""
Write a function to compute the net amount of a bank account based a transaction log from console input.
The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.

Suppose the following input is supplied to the function:
D 300
D 300
W 200
D 100
Then, the output should be:
500
"""
def bank_account():
    total = 0
    while True:
        try:
            transaction = input()
            if transaction == '':
                break
            else:
                transaction = transaction.split()
                if transaction[0] == 'D':
                    total += int(transaction[1])
                elif transaction[0] == 'W':
                    total -= int(transaction[1])
                else:
                    print('Invalid transaction')
        except:
            print('Invalid transaction')
    return total

"""
Write a function to compute the hypotenuse of a right angled triangle.
"""
def hypotenuse(a, b):
    return (a**2 + b**2)**0.5

"""
Write a function to compute the distance between two points.
"""
def distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

"""
Write a function to compute the area of a circle.
"""
def circle_area(r):
    return 3.14*r**2

"""
Write a function to compute the area of a rectangle.
"""
def rectangle_area(l, w):
    return l*w

"""
Write a function to compute the area of a triangle.
"""
def triangle_area(b, h):
    return 0.5*b*h

"""
Write a function to compute the volume of a sphere.
"""
def sphere_volume(r):
    return 4/3*3.14*r**3

"""
Write a function to compute the volume of a cylinder.
"""
def cylinder_volume(r, h):
    return 3.14*r**2*h

"""
Write a function to compute the volume of a cone.
"""
def cone_volume(r, h):
    return 1/3*3.14*r**2*h

"""
Write a function to compute the volume of a pyramid.
"""
def pyramid_volume(b, h):
    return 1/3*b*h

"""
Write a function to compute the volume of a cube.
"""
def cube_volume(s):
    return s**3

"""
Write a function to compute the volume of a tetrahedron.
"""
def tetrahedron_volume(s):
    return 1/6*s**3

"""
Write a function to compute the volume of a sphere.
"""
def sphere_volume(r):
    return 4/3*3.14*r**3

"""
Write a function to compute the volume of a cylinder.
"""
def cylinder_volume(r, h):
    return 3.14*r**2*h

"""
Write a function to compute the volume of a cone.
"""
def cone_volume(r, h):
    return 1/3*3.14*r**2*h

"""
Write a function to compute the volume of a pyramid.
"""
def pyramid_volume(b, h):
    return 1/3*b*h

"""
Write a function to compute the volume of a cube.
"""
def cube_volume(s):
    return s**