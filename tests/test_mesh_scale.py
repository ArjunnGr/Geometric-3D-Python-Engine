import unittest
from modules.mesh_scale import scale_mesh  # Make sure to import scale_mesh from the correct module

class TestScaleMesh(unittest.TestCase):

    # ... Other test cases ...

    def test_scale_mesh_with_negative_factor(self):
        mesh = [[1, 2, 3], [4, 5, 6]]
        scale_factor = -1
        expected = [[-1, -2, -3], [-4, -5, -6]]
        actual = scale_mesh(mesh, scale_factor)
        self.assertEqual(actual, expected, f"Expected {expected}, but got {actual}")

    # ... Other test cases ...

    def test_scale_mesh_with_precision_loss(self):
        mesh = [[1/3, 2/3, 1/9]]
        scale_factor = 3
        precision = 2
        expected = [[1.0, 2.0, 0.33]]
        actual = scale_mesh(mesh, scale_factor, precision)
        self.assertEqual(actual, expected, f"Expected {expected}, but got {actual} with precision {precision}")

    # ... Other test cases ...

if __name__ == '__main__':
    unittest.main()