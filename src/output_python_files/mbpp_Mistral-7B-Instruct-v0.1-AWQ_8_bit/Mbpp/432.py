"""
Write a function to find the median length of a trapezium.
assert median_trapezium(15,25,35)==20
"""

def median_trapezium(a,b,c,d):
    """
    Find the median length of a trapezium
    """
    # Calculate the sum of the lengths of the two parallel sides
    s=a+b
    # Calculate the sum of the lengths of the two perpendicular sides
    t=c+d
    # Calculate the length of the trapezium
    l=(s+t)/2
    # Calculate the median length of the trapezium
    m=l*(1+0.5*(s-t))
    # Return the median length
    return m

assert median_trapezium(15,25,35)==20