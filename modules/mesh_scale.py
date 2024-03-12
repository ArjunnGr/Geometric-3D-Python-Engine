

def scale_mesh(mesh, scale_factor, precision=2):
    """Scales a mesh by a given factor with specified precision."""
    scaled_mesh = [[round(x * scale_factor, precision) for x in point] for point in mesh]
    return scaled_mesh

