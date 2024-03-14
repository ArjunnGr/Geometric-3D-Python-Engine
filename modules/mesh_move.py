

def move_mesh(mesh, translation_vector):
    """
    Translate a mesh by a given vector.

    Parameters:
    mesh (list of tuples): A list of (x, y, z) tuples representing the mesh vertices.
    translation_vector (tuple): The (x, y, z) vector by which to translate the mesh.

    Returns:
    list: The mesh after translation, as a list of new (x, y, z) tuples.
    """
    tx, ty, tz = translation_vector
    moved_mesh = [(x + tx, y + ty, z + tz) for x, y, z in mesh]
    return moved_mesh


if __name__ == '__main__':
    test_mesh = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    translation_vector = (10, -10, 0)
    moved_mesh = move_mesh(test_mesh, translation_vector)
    print(f"Moved Mesh: {moved_mesh}")