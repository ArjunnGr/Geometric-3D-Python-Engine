import unittest
from modules.convexity_check import is_convex

class TestConvexityCheck(unittest.TestCase):

    def test_triangle_always_convex(self):
        triangle = [(0, 0, 0), (1, 0, 0), (0, 1, 0)]
        self.assertTrue(is_convex(triangle))

    def test_square_is_convex(self):
        square = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]
        self.assertTrue(is_convex(square))

    def test_convex_polygon(self):
        convex_polygon = [(0, 0, 0), (2, 0, 0), (2, 1, 0), (1, 2, 0), (0, 1, 0)]
        self.assertTrue(is_convex(convex_polygon))

    def test_non_convex_polygon(self):
        non_convex_polygon = [(0, 0, 0), (2, 0, 0), (1, -1, 0), (0, 2, 0)]
        self.assertFalse(is_convex(non_convex_polygon))

    def test_non_convex_polygon_with_internal_angle_greater_than_180(self):
        non_convex_polygon = [(0, 0, 0), (3, 0, 0), (2, 1, 0), (1, 1, 0), (1, 2, 0), (0, 1, 0)]
        self.assertFalse(is_convex(non_convex_polygon))

    def test_convexity_with_colinear_points(self):
        # This should return True, but depending on the implementation, colinear points may cause issues.
        polygon_with_colinear_points = [(0, 0, 0), (1, 0, 0), (2, 0, 0), (1, 1, 0)]
        self.assertTrue(is_convex(polygon_with_colinear_points))

    def test_empty_polygon(self):
        empty_polygon = []
        self.assertTrue(is_convex(empty_polygon))  # Depending on definition, an empty polygon might be considered convex

    def test_polygon_with_two_points(self):
        line = [(0, 0, 0), (1, 1, 1)]
        self.assertTrue(is_convex(line))  # Depending on definition, a two-point polygon might be considered convex

    def test_polygon_with_one_point(self):
        single_point = [(0, 0, 0)]
        self.assertTrue(is_convex(single_point))  # Depending on definition, a single-point polygon might be considered convex

if __name__ == '__main__':
    unittest.main()