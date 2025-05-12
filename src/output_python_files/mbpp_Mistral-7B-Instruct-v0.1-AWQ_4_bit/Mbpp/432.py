"""
Write a function to find the median length of a trapezium.
assert median_trapezium(15,25,35)==20
"""

def median_trapezium(a,b,c,d):
    """
    Find the median length of a trapezium
    """
    # Find the sum of the lengths of the two parallel sides
    s=a+b
    # Find the sum of the lengths of the two non-parallel sides
    t=c+d
    # Find the length of the trapezium
    l=(s+t)/2
    # Find the median length of the trapezium
    m=l
    if l%2==0:
        m=(l+t)/2
    return m

assert median_trapezium(15,25,35)==20