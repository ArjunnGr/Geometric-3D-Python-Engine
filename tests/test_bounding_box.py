import unittest
import sys
sys.path.append('../')  # Appends the parent directory to sys.path
from modules.bounding_box import calculate_smallest_bounding_box

class TestCalculateSmallestBoundingBox(unittest.TestCase):

    def test_calculate_smallest_bounding_box(self):
        # Test case with a list of points
        points = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        expected_result = {'min_point': (1, 2, 3), 'max_point': (7, 8, 9)}
        self.assertEqual(calculate_smallest_bounding_box(points), expected_result)

    def test_empty_points_list(self):
        # Test case with an empty list of points
        points = []
        with self.assertRaises(ValueError):
            calculate_smallest_bounding_box(points)

    def test_single_point(self):
        # Test case with a single point
        points = [(1, 2, 3)]
        expected_result = {'min_point': (1, 2, 3), 'max_point': (1, 2, 3)}
        self.assertEqual(calculate_smallest_bounding_box(points), expected_result)

if __name__ == '__main__':
    unittest.main()