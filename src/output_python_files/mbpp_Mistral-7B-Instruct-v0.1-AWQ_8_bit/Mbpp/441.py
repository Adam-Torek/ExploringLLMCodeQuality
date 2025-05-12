"""
Write a function to find the surface area of a cube of a given size.
assert surfacearea_cube(5)==150
"""

def surfacearea_cube(size):
    """
    This function calculates the surface area of a cube of a given size.
    """
    surface_area = 6 * size**2
    return surface_area


if __name__ == '__main__':
    import unittest

    class TestSurfaceAreaCube(unittest.TestCase):

        def test_surfacearea_cube(self):
            self.assertEqual(surfacearea_cube(5), 150)

    unittest.main()