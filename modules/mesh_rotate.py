
import math

def rotate_point(point, angle_rad, axis):
    """
    Rotate a point in 3D space around the origin along the specified axis.

    Parameters:
    point (tuple): The (x, y, z) coordinates of the point to rotate.
    angle_rad (float): The rotation angle in radians.
    axis (str): The axis to rotate around ('X', 'Y', or 'Z').

    Returns:
    tuple: The new (x, y, z) coordinates of the rotated point.
    """
    x, y, z = point
    cos_angle = math.cos(angle_rad)
    sin_angle = math.sin(angle_rad)

    if axis == 'X':
        new_y = y * cos_angle - z * sin_angle
        new_z = y * sin_angle + z * cos_angle
        return x, new_y, new_z

    elif axis == 'Y':
        new_x = x * cos_angle + z * sin_angle
        new_z = -x * sin_angle + z * cos_angle
        return new_x, y, new_z

    elif axis == 'Z':
        new_x = x * cos_angle - y * sin_angle
        new_y = x * sin_angle + y * cos_angle
        return new_x, new_y, z

    else:
        raise ValueError("Invalid axis. Please choose 'X', 'Y', or 'Z'.")


def rotate_mesh(mesh, angle_deg, axis):
    """
    Rotate an entire mesh around the specified axis by the specified angle.

    Parameters:
    mesh (list of tuples): A list of (x, y, z) tuples representing the mesh vertices.
    angle_deg (float): The rotation angle in degrees.
    axis (str): The axis to rotate around ('X', 'Y', or 'Z').

    Returns:
    list: The mesh after rotation, as a list of new (x, y, z) tuples.
    """
    angle_rad = math.radians(angle_deg)  
    return [rotate_point(point, angle_rad, axis) for point in mesh]



if __name__ == '__main__':
    test_mesh = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    rotated_mesh = rotate_mesh(test_mesh, 90, 'Z')
    print(f"Rotated Mesh: {rotated_mesh}")