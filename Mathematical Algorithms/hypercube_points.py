from typing import List


def generate_hypercube_points(n: int) -> List[List[int]]:
    """
    Generate all points (vertices) of an n-dimensional hypercube.

    Args:
        n (int): The dimension of the hypercube.

    Returns:
        List[List[int]]: A list of points, where each point is a list of n binary digits (0 or 1).

    Time Complexity: O(n * 2^n)
    Space Complexity: O(n * 2^n)
    """
    return [[(i >> j) & 1 for j in range(n)] for i in range(1 << n)]


def print_hypercube_points(points: List[List[int]], dimension: int) -> None:
    """
    Print the points of a hypercube in a formatted manner.

    Args:
        points (List[List[int]]): The list of hypercube points to print.
        dimension (int): The dimension of the hypercube.
    """
    print(f"Hypercube Points ({dimension}D):")
    for point in points:
        print(point)


if __name__ == "__main__":
    # Example usage
    dimension = 3
    hypercube_points = generate_hypercube_points(dimension)
    print_hypercube_points(hypercube_points, dimension)

    # Additional examples
    print("\nHypercube Points (2D):")
    print_hypercube_points(generate_hypercube_points(2), 2)

    print("\nHypercube Points (4D):")
    print_hypercube_points(generate_hypercube_points(4), 4)
