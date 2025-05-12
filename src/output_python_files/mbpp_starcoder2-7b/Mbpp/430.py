"""
Write a function to find the directrix of a parabola.
assert parabola_directrix(5,3,2)==-198
"""
def parabola_directrix(a,b,c):
    return -4*a*c

"""
Write a function to find the focus of a parabola.
assert parabola_focus(5,3,2)==-10
"""
def parabola_focus(a,b,c):
    return -2*a*c

"""
Write a function to find the vertex of a parabola.
assert parabola_vertex(5,3,2)==(-1,1)
"""
def parabola_vertex(a,b,c):
    return (-b/(2*a),-parabola_focus(a,b,c)/(4*a))

"""
Write a function to find the equation of a parabola.
assert parabola_equation(5,3,2)=="x^2+3x+2"
"""
def parabola_equation(a,b,c):
    return "x^2"+"+"+str(b)+"x"+"+"+str(c)

"""
Write a function to find the equation of a parabola given the focus and directrix.
assert parabola_equation_focus_directrix(5,3,2,1)=="x^2+3x+2"
"""
def parabola_equation_focus_directrix(a,b,c,d):
    return "x^2"+"+"+str(b)+"x"+"+"+str(c)

"""
Write a function to find the equation of a parabola given the vertex and directrix.
assert parabola_equation_vertex_directrix(5,3,2,1)=="x^2+3x+2"
"""
def parabola_equation_vertex_directrix(a,b,c,d):
    return "x^2"+"+"+str(b)+"x"+"+"+str(c)

"""
Write a function to find the equation of a parabola given the vertex and focus.
assert parabola_equation_vertex_focus(5,3,2,1)=="x^2+3x+2"
"""
def parabola_equation_vertex_focus(a,b,c,d):
    return "x^2"+"+"+str(b)+"x"+"+"+str(c)

"""
Write a function to find the equation of a parabola given the directrix and focus.
assert parabola_equation_directrix_focus(5,3,2,1)=="x^2+3x+2"
"""
def parabola_equation_directrix_focus(a,b,c,d):
    return "x^2"+"+"+str(b)+"x"+"+"+str(c)

"""
Write a function to find the equation of a parabola given the directrix and vertex.
assert parabola_equation_directrix_vertex(5,3,2,1)=="x^2+3x+2"
"""
def parabola_equation_directrix_vertex(a,b,c,d):
    return "x^2"+"+"+str(b)+"x"+"+"+str(c)

"""
Write a function to find the equation of a parabola given the focus and vertex.
assert parabola_equation_focus_vertex(5,3,2,1)=="x^2+3x+2"
"""
def parabola_equation_focus_vertex(a,b,c,d):
    return "x^2"+"+"+str(b)+"x"+"+"+str(c)

"""
Write a function to find the equation of a parabola given the focus and directrix.
assert parabola_equation_focus_directrix(5,3,2,1)=="x^2+3x+2"
"""
def parabola_equation_focus_directrix(a,b,c,d):
    return "x^2"+"+"+str(b)+"x"+"+"+str(c)

"""
Write a function to find the equation of a parabola given the vertex and directrix.
assert parabola_equation_vertex_directrix(5,3,2,1)=