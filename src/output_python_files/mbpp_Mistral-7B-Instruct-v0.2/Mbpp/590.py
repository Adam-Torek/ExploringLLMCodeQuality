"""
Write a function to convert polar coordinates to rectangular coordinates.
assert polar_rect(3,4)==((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))
"""
def polar_rect(r, theta):
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return (x, y)

assert polar_rect(3,4) == (5.0, 0.9272952180016122)
assert polar_rect(3,np.pi/2) == (np.sqrt(2)*3, 3)
assert polar_rect(1,np.pi) == (-1, 0)
assert polar_rect(1,np.pi/2) == (np.sqrt(2), 1)
assert polar_rect(1,np.pi/4) == (np.sqrt(2)/2, np.sqrt(2)/2)
assert polar_rect(1,3*np.pi/2) == (-np.sqrt(2)/2, np.sqrt(2)/2)
assert polar_rect(1,5*np.pi/4) == (-np.sqrt(2)/2, -np.sqrt(2)/2)
assert polar_rect(1,7*np.pi/4) == (np.sqrt(2)/2, -np.sqrt(2)/2)</s>