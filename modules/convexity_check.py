

def cross_product(p1, p2, p3):
    """
    Calculate the cross product of vectors defined by points p1->p2 and p2->p3.

    Parameters:
    p1, p2, p3 (tuple): Points in the form of (x, y, z).

    Returns:
    tuple: The resulting cross product vector.
    """
    
    u = (p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2])
    v = (p3[0] - p2[0], p3[1] - p2[1], p3[2] - p2[2])

   
    return (u[1]*v[2] - u[2]*v[1], u[2]*v[0] - u[0]*v[2], u[0]*v[1] - u[1]*v[0])

def is_convex(polygon):
    """
    Determine if a polygon is convex based on the cross product of its edges.

    Parameters:
    polygon (list of tuples): A list of (x, y, z) tuples representing the vertices of the polygon in order.

    Returns:
    bool: True if the polygon is convex, False otherwise.
    """
    if len(polygon) < 4:  
        return True

   
    prev_z = 0
    
    sign = None

    for i in range(len(polygon)):
        
        p1, p2, p3 = polygon[i], polygon[(i + 1) % len(polygon)], polygon[(i + 2) % len(polygon)]
        cross_prod = cross_product(p1, p2, p3)

       
        current_z = cross_prod[2]

        if i == 0:  
            sign = current_z
        else:
            if current_z * sign < 0:  
                return False

        prev_z = current_z

    return True


if __name__ == '__main__':
    convex_polygon = [(0, 0, 0), (2, 0, 0), (1, 1, 0), (0, 2, 0)]
    non_convex_polygon = [(0, 0, 0), (2, 0, 0), (1, -1, 0), (0, 2, 0)]

    print(f"Convex Polygon: {is_convex(convex_polygon)}")
    print(f"Non-Convex Polygon: {is_convex(non_convex_polygon)}")