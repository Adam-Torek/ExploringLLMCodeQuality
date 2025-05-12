"""
Write a function to find the lateral surface area of a cube given its side length.
assert lateralsurface_cube(5)==100
"""

def lateralsurface_cube(side_length):
    """
    This function calculates the lateral surface area of a cube.
    :param side_length: The side length of the cube
    :return: The lateral surface area of the cube
    """
    # Calculate the surface area of one face of the cube
    face_area = side_length**2
    # Calculate the number of faces of the cube
    num_faces = 6
    # Calculate the lateral surface area of the cube
    lateral_surface_area = num_faces * face_area
    return lateral_surface_area

# Test the function
assert lateralsurface_cube(5) == 100