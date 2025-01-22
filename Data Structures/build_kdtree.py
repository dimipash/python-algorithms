class KDNode:
    """
    A class representing a node in a KD-Tree.

    Attributes:
        point (tuple): The k-dimensional point stored in this node.
        left (KDNode): The left child of this node.
        right (KDNode): The right child of this node.
        axis (int): The axis along which this node is partitioned.
    """

    def __init__(self, point, axis):
        """
        Initializes a KDNode with the given point and axis.

        Parameters:
            point (tuple): The k-dimensional point.
            axis (int): The axis for this node.
        """
        self.point = point  # The k-dimensional point
        self.left = None  # Left child
        self.right = None  # Right child
        self.axis = axis  # Axis for this node


class KDTree:
    """
    A class representing a KD-Tree for organizing points in k-dimensional space.

    Methods:
        build(points, depth=0): Recursively builds the KD-Tree from the given points.

    Time Complexity:
        - Building the KD-Tree: O(n log n) on average, where n is the number of points.
          This is due to sorting the points at each level of recursion. In the worst case,
          if the input is already sorted along one dimension, it can degrade to O(n^2).

    Space Complexity:
        - O(n) for storing all nodes in memory, where n is the number of points.
          Additionally, recursive calls will use stack space proportional to the height
          of the tree, which is O(log n) in a balanced tree.
    """

    def build(self, points, depth=0):
        """
        Builds a KD-Tree from the provided list of points.

        Parameters:
            points (list): A list of k-dimensional points to organize in the tree.
            depth (int): The current depth in the tree, used to determine the axis.

        Returns:
            KDNode: The root node of the constructed KD-Tree.
        """
        if not points:  # Base case: no points to process
            return None

        k = len(points[0])  # Number of dimensions
        axis = depth % k  # Current axis to partition by

        # Sort points by the current axis and find the median
        points.sort(key=lambda x: x[axis])
        median = len(points) // 2  # Choose median

        # Create a new node with the median point
        node = KDNode(points[median], axis)

        # Recursively build left and right subtrees
        node.left = self.build(points[:median], depth + 1)
        node.right = self.build(points[median + 1 :], depth + 1)

        return node


def print_kd_tree(node, depth=0):
    """
    Prints the structure of the KD-Tree for visualization.

    Parameters:
        node (KDNode): The current node in the KD-Tree.
        depth (int): The current depth in the tree for formatting output.
    """
    if node is not None:
        print_kd_tree(node.left, depth + 1)
        print(" " * depth * 4, node.point)
        print_kd_tree(node.right, depth + 1)


# Example usage:
if __name__ == "__main__":
    points = [(7, 2), (5, 4), (9, 6), (2, 3), (4, 7), (8, 1)]
    kd_tree = KDTree()
    root = kd_tree.build(points)

    # Output the KD-Tree structure
    print_kd_tree(root)
