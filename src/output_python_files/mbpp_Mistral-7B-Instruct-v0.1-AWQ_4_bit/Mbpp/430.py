"""
Write a function to find the directrix of a parabola.
assert parabola_directrix(5,3,2)==-198
"""

def parabola_directrix(a,b,c):
    """
    This function takes in the coefficients of a quadratic equation in the form of ax^2 + bx + c = 0
    and returns the x value of the directrix of the parabola.
    """
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    else:
        x = (-b + math.sqrt(discriminant)) / (2*a)
        return x



#test the function
#assert parabola_directrix(5,3,2)==-198
#assert parabola_directrix(5,3,1)==-198
#assert parabola_directrix(5,3,0)==-198
#assert parabola_directrix(5,3,4)==-198
#assert parabola_directrix(5,3,5)==-198
#assert parabola_directrix(5,3,6)==-198
#assert parabola_directrix(5,3,7)==-198
#assert parabola_directrix(5,3,8)==-198
#assert parabola_directrix(5,3,9)==-198
#assert parabola_directrix(5,3,10)==-198
#assert parabola_directrix(5,3,11)==-198
#assert parabola_directrix(5,3,12)==-198
#assert parabola_directrix(5,3,13)==-198
#assert parabola_directrix(5,3,14)==-198
#assert parabola_directrix(5,3,15)==-198
#assert parabola_directrix(5,3,16)==-198
#assert parabola_directrix(5,3,17)==-198
#assert parabola_directrix(5,3,18)==-198
#assert parabola_directrix(5,3,19)==-198
#assert parabola_directrix(5,3,20)==-198
#assert parabola_directrix(5,3,21)==-198
#assert parabola_directrix(5,3,22)==-198
#assert parabola_directrix(5,3,23)==-198
#assert parabola_directrix(5,3,24)==-198
#assert parabola_directrix(5,3,25)==-198
#assert parabola_directrix(5,3,26)==-198
#assert parabola_directrix(5,3,27)==-198
#assert parabola_directrix(5,3,28)==-198
#assert parabola_directrix(5,3,29)==-198
#assert parabola_directrix(5,3,30)==-198
#assert parabola_directrix(5,3,31)==-198
#assert parabola_directrix(5,3,32)==-198
#assert parabola_directrix(5,3,33)==-198
#assert parabola_directrix(5,3,34)==-198
#assert parabola_directrix(5,3,35)==-198
#assert parabola_directrix(5,3,36)==-198
#assert parabola_directrix(5,3,37)==-198
#assert parabola_directrix(5,3,38)