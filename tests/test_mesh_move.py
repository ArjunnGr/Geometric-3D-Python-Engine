import unittest
from modules.mesh_move import move_mesh

class TestMeshMove(unittest.TestCase):

    def test_move_mesh_positive_translation(self):
        mesh = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        translation_vector = (10, 10, 10)
        expected = [(11, 12, 13), (14, 15, 16), (17, 18, 19)]
        moved_mesh = move_mesh(mesh, translation_vector)
        self.assertEqual(moved_mesh, expected)

    def test_move_mesh_negative_translation(self):
        mesh = [(10, 20, 30), (40, 50, 60), (70, 80, 90)]
        translation_vector = (-5, -5, -5)
        expected = [(5, 15, 25), (35, 45, 55), (65, 75, 85)]
        moved_mesh = move_mesh(mesh, translation_vector)
        self.assertEqual(moved_mesh, expected)

    def test_move_mesh_mixed_translation(self):
        mesh = [(10, 20, 30), (40, 50, 60), (70, 80, 90)]
        translation_vector = (-5, 10, -15)
        expected = [(5, 30, 15), (35, 60, 45), (65, 90, 75)]
        moved_mesh = move_mesh(mesh, translation_vector)
        self.assertEqual(moved_mesh, expected)

    def test_move_mesh_no_translation(self):
        mesh = [(10, 20, 30), (40, 50, 60), (70, 80, 90)]
        translation_vector = (0, 0, 0)
        expected = [(10, 20, 30), (40, 50, 60), (70, 80, 90)]
        moved_mesh = move_mesh(mesh, translation_vector)
        self.assertEqual(moved_mesh, expected)

    def test_move_mesh_single_point(self):
        mesh = [(1, 2, 3)]
        translation_vector = (10, -10, 5)
        expected = [(11, -8, 8)]
        moved_mesh = move_mesh(mesh, translation_vector)
        self.assertEqual(moved_mesh, expected)

    def test_move_mesh_empty_mesh(self):
        mesh = []
        translation_vector = (10, 10, 10)
        expected = []
        moved_mesh = move_mesh(mesh, translation_vector)
        self.assertEqual(moved_mesh, expected)

if __name__ == '__main__':
    unittest.main()