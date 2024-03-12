import unittest
import math
from modules.mesh_rotate import rotate_point, rotate_mesh

class TestMeshRotate(unittest.TestCase):

    def test_rotate_point_x_axis_90_degrees(self):
        point = (1, 0, 0)
        angle_rad = math.radians(90)
        expected = (1, 0, 0)
        rotated_point = rotate_point(point, angle_rad, 'X')
        for rp, ep in zip(rotated_point, expected):
            self.assertAlmostEqual(rp, ep)

    def test_rotate_point_y_axis_90_degrees(self):
        point = (1, 0, 0)
        angle_rad = math.radians(90)
        expected = (0, 0, 1)
        rotated_point = rotate_point(point, angle_rad, 'Y')
        for rp, ep in zip(rotated_point, expected):
            self.assertAlmostEqual(rp, ep)

    def test_rotate_point_z_axis_90_degrees(self):
        point = (0, 1, 0)
        angle_rad = math.radians(90)
        expected = (-1, 0, 0)
        rotated_point = rotate_point(point, angle_rad, 'Z')
        for rp, ep in zip(rotated_point, expected):
            self.assertAlmostEqual(rp, ep)

    def test_rotate_point_no_rotation(self):
        point = (1, 2, 3)
        angle_rad = math.radians(0)
        expected = (1, 2, 3)
        rotated_point = rotate_point(point, angle_rad, 'X')
        self.assertEqual(rotated_point, expected)

    def test_rotate_point_full_rotation(self):
        point = (1, 2, 3)
        angle_rad = math.radians(360)
        expected = (1, 2, 3)
        rotated_point = rotate_point(point, angle_rad, 'X')
        for rp, ep in zip(rotated_point, expected):
            self.assertAlmostEqual(rp, ep)

    def test_rotate_point_negative_angle(self):
        point = (0, 1, 0)
        angle_rad = math.radians(-90)
        expected = (1, 0, 0)
        rotated_point = rotate_point(point, angle_rad, 'Z')
        for rp, ep in zip(rotated_point, expected):
            self.assertAlmostEqual(rp, ep)

    def test_rotate_point_invalid_axis(self):
        point = (1, 0, 0)
        angle_rad = math.radians(90)
        with self.assertRaises(ValueError):
            rotate_point(point, angle_rad, 'A')

    # You can add similar tests for rotate_mesh function as needed.

if __name__ == '__main__':
    unittest.main()