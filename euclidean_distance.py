"""
Euclidean Distance Calculator

Calculates the straight-line distance between two points in n-dimensional
Euclidean space using the formula: d = √Σ(xi - yi)²

Time Complexity: O(n) where n is the dimension of points
Space Complexity: O(1) using vectorized operations
"""


def euclidean_distance(point1: tuple, point2: tuple) -> float:
    """
    Calculate Euclidean distance between two points in n-dimensional space.

    Args:
        point1 (tuple): Coordinates of first point
        point2 (tuple): Coordinates of second point

    Returns:
        float: Euclidean distance between points

    Raises:
        ValueError: If points have different dimensions

    Examples:
        >>> euclidean_distance((1, 2), (4, 6))
        5.0
        >>> euclidean_distance((1, 2, 3), (4, 6, 8))
        7.07
    """
    if len(point1) != len(point2):
        raise ValueError("Points must have same dimension")

    return np.sqrt(np.sum((np.array(point1) - np.array(point2)) ** 2))


def main() -> None:
    """
    Demonstrate Euclidean distance calculation with examples.
    """
    test_cases = [((1, 2), (4, 6)), ((1, 2, 3), (4, 6, 8))]  # 2D points  # 3D points

    for p1, p2 in test_cases:
        distance = euclidean_distance(p1, p2)
        print(f"Distance between {p1} and {p2}: {distance:.2f}")


if __name__ == "__main__":
    main()
