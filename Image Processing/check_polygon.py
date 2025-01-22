"""
Point in Polygon Checker using Ray Casting Algorithm

Determines if a point lies inside a polygon using ray casting method.
A ray is cast from the point, and the number of intersections with polygon
edges determines if the point is inside (odd) or outside (even).

Time Complexity: O(n) where n is number of vertices
Space Complexity: O(1) as only scalar values are stored
"""


def is_point_in_polygon(point: tuple, polygon: list) -> bool:
    """
    Check if a point lies inside a polygon using ray casting.

    Args:
        point (tuple): Point coordinates (x, y)
        polygon (list): List of vertex coordinates [(x1,y1), (x2,y2), ...]

    Returns:
        bool: True if point is inside polygon, False otherwise

    Raises:
        ValueError: If polygon has less than 3 vertices
    """
    if len(polygon) < 3:
        raise ValueError("Polygon must have at least 3 vertices")

    x, y = point
    n = len(polygon)
    inside = False

    # Get the first vertex
    p1x, p1y = polygon[0]

    # Check each edge of the polygon
    for i in range(n + 1):
        # Get next vertex (wrap around to first vertex)
        p2x, p2y = polygon[i % n]

        # Check if ray intersects edge
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside

        # Move to next edge
        p1x, p1y = p2x, p2y

    return inside


def main() -> None:
    """
    Demonstrate point in polygon testing with example cases.
    """
    # Define test cases
    polygon = [(1, 1), (1, 3), (3, 3), (3, 1)]
    test_points = [
        (2, 2),  # Inside
        (4, 2),  # Outside
        (1, 1),  # On vertex
        (2, 3),  # On edge
        (0, 2),  # Outside
    ]

    for point in test_points:
        result = is_point_in_polygon(point, polygon)
        print(f"Point {point} is {'inside' if result else 'outside'} polygon")


if __name__ == "__main__":
    main()
