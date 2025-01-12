"""
Chebyshev Distance Calculator

Calculates the maximum metric (L∞ norm) between two points in n-dimensional space.
The Chebyshev distance is defined as: max(|xi - yi|) for all coordinates i.

Time Complexity: O(n) where n is the dimension of the points
Space Complexity: O(1) as only scalar values are stored
"""


def chebyshev_distance(p: tuple, q: tuple) -> float:
    """
    Calculate Chebyshev distance between two points.

    Args:
        p (tuple): First point coordinates
        q (tuple): Second point coordinates

    Returns:
        float: Chebyshev distance between p and q

    Raises:
        ValueError: If points have different dimensions
    """
    if len(p) != len(q):
        raise ValueError("Points must have the same dimension")

    return max(abs(pi - qi) for pi, qi in zip(p, q))


def main() -> None:
    """
    Demonstrate Chebyshev distance calculation with examples.
    """
    test_cases = [
        ((1, 2, 3), (4, 6, 1)),  # 3D points
        ((0, 0), (1, 1)),  # 2D points
        ((5,), (2,)),  # 1D points
        ((0, 0, 0), (1, 1, 1)),  # Unit cube diagonal
    ]

    for p, q in test_cases:
        distance = chebyshev_distance(p, q)
        print(f"Distance between {p} and {q}: {distance}")


if __name__ == "__main__":
    main()
