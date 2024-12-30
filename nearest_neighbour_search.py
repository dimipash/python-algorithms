from typing import List, Tuple
from scipy.spatial import KDTree


def nearest_neighbor_search(
    points: List[List[float]], query_point: List[float]
) -> Tuple[List[float], float]:
    """
    Perform nearest neighbor search using a KD-Tree.

    Args:
        points: List of points in k-dimensional space.
        query_point: The point to find the nearest neighbor for.

    Returns:
        The nearest point and its distance from the query point.

    Time complexity: O(log n) for querying, where n is the number of points.
    Space complexity: O(n) for storing the KD-Tree.
    """
    tree = KDTree(points)  # Build the KD-Tree
    distance, index = tree.query(query_point)  # Find nearest neighbor
    return points[index], distance


if __name__ == "__main__":
    # Example usage
    points = [[1, 2], [3, 4], [5, 6], [7, 8]]
    query_point = [4, 5]
    nearest_point, nearest_distance = nearest_neighbor_search(points, query_point)
    print(f"Nearest Point: {nearest_point}")
    print(f"Distance: {nearest_distance}")
