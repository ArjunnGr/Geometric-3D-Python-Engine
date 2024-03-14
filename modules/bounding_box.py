

def calculate_smallest_bounding_box(points):
    """
    Calculate the smallest bounding box that contains all the 3D points.

    Parameters:
    points (list of tuples): A list of (x, y, z) tuples representing points in 3D space.

    Returns:
    dict: Bounding box represented by two points (min_point, max_point) defining the smallest cuboidal area containing all points.
    """
    if not points:
        raise ValueError("No points provided")
    
    
    min_x, min_y, min_z = points[0]
    max_x, max_y, max_z = points[0]

  
    for (x, y, z) in points:
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        min_z = min(min_z, z)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        max_z = max(max_z, z)

    min_point = (min_x, min_y, min_z)
    max_point = (max_x, max_y, max_z)

    return {
        'min_point': min_point,
        'max_point': max_point
    }