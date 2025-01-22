from typing import List, Optional, Union


class KDNode:
    """
    A node in a k-dimensional tree (KD-Tree).

    This class represents a node in a KD-Tree, which is used for organizing
    points in a k-dimensional space. Each node contains a point, references
    to left and right child nodes, and the axis used for partitioning at this level.

    Attributes:
        point (List[float]): The k-dimensional point stored in this node.
        left (Optional[KDNode]): The left child node.
        right (Optional[KDNode]): The right child node.
        axis (int): The axis (dimension) used for partitioning at this node.

    Time Complexity:
        - Initialization: O(1)
        - Space Complexity: O(1) per node, O(n) for a tree with n points
    """

    def __init__(self, point: List[float], axis: int):
        """
        Initialize a KD Node.

        Args:
            point (List[float]): The k-dimensional point to store in this node.
            axis (int): The axis (dimension) used for partitioning at this node.
        """
        self.point = point
        self.left: Optional[KDNode] = None
        self.right: Optional[KDNode] = None
        self.axis = axis

    def __str__(self) -> str:
        """Return a string representation of the KD Node."""
        return f"KDNode(point={self.point}, axis={self.axis})"

    def is_leaf(self) -> bool:
        """Check if this node is a leaf node (has no children)."""
        return self.left is None and self.right is None

    def dimension(self) -> int:
        """Get the dimension of the point stored in this node."""
        return len(self.point)


# Example usage
if __name__ == "__main__":
    # Creating a KD Node for a point in 3D space
    node = KDNode(point=[2, 3, 4], axis=0)
    print("KD Node Point:", node.point)  # Output: [2, 3, 4]
    print("Partitioning Axis:", node.axis)  # Output: 0
    print("Is leaf node:", node.is_leaf())  # Output: True
    print("Dimension:", node.dimension())  # Output: 3

    # Creating child nodes
    node.left = KDNode([1, 2, 3], 1)
    node.right = KDNode([3, 4, 5], 1)
    print("Is leaf node after adding children:", node.is_leaf())  # Output: False

    # Printing the entire node
    print(node)  # Output: KDNode(point=[2, 3, 4], axis=0)
