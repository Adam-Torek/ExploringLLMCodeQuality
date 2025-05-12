"""
Write a function to perform index wise multiplication of tuple elements in the given two tuples.
assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3)) ) == ((6, 21), (12, 45), (2, 9), (7, 30))
"""
def index_multiplication(tuple1,tuple2):
    return tuple(map(lambda x,y: (x[0]*y[0],x[1]*y[1]),tuple1,tuple2))

"""
Write a function to perform index wise addition of tuple elements in the given two tuples.
assert index_addition(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3)) ) == ((7, 10), (7, 14), (3, 10), (8, 13))
"""
def index_addition(tuple1,tuple2):
    return tuple(map(lambda x,y: (x[0]+y[0],x[1]+y[1]),tuple1,tuple2))

"""
Write a function to perform index wise subtraction of tuple elements in the given two tuples.
assert index_subtraction(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3)) ) == ((-5, -4), (1, 6), (1, 8), (-6, 7))
"""
def index_subtraction(tuple1,tuple2):
    return tuple(map(lambda x,y: (x[0]-y[0],x[1]-y[1]),tuple1,tuple2))

"""
Write a function to perform index wise division of tuple elements in the given two tuples.
assert index_division(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3)) ) == ((0, 0), (1, 0), (2, 0), (0, 0))
"""
def index_division(tuple1,tuple2):
    return tuple(map(lambda x,y: (x[0]/y[0],x[1]/y[1]),tuple1,tuple2))

"""
Write a function to perform index wise floor division of tuple elements in the given two tuples.
assert index_floor_division(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3)) ) == ((0, 0), (1, 0), (2, 0), (0, 0))
"""
def index_floor_division(tuple1,tuple2):
    return tuple(map(lambda x,y: (x[0]//y[0],x[1]//y[1]),tuple1,tuple2))

"""
Write a function to perform index wise modulo division of tuple elements in the given two tuples.
assert index_modulo_division(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3)) ) == ((1, 1), (1, 1), (0, 0), (1, 1))
"""
def index_modulo_division(tuple1,tuple2):
    return tuple(map(lambda x,y: (x[0]%y[0],x[1]%y[1]),tuple1,tuple2))

"""
Write a function to perform index wise exponentiation of tuple elements in the given two tuples.
assert index_exponentiation(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3)) ) == ((1, 27), (64, 5), (2, 81), (1,