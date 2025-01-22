import math


class Node:
    """
    A node in the KD-Tree.

    Attributes:
        point (list): The point in k-dimensional space.
        axis (int): The axis (dimension) used for partitioning.
        left (Node): Reference to the left child.
        right (Node): Reference to the right child.
    """

    def __init__(self, point, axis):
        """
        Initialize a new node.

        Args:
            point (list): The point in k-dimensional space.
            axis (int): The axis for partitioning.
        """
        self.point = point
        self.axis = axis
        self.left = None
        self.right = None


class KDTree:
    """
    A KD-Tree data structure for organizing points in k-dimensional space.

    Time Complexity:
        Insertion: O(log N) on average, O(N) in the worst case.
        Nearest Neighbor Search: O(log N) on average, O(N) in the worst case.

    Space Complexity: O(N), where N is the number of points.
    """

    def __init__(self, k):
        """
        Initialize a KD-Tree with k dimensions.

        Args:
            k (int): The number of dimensions.
        """
        self.root = None
        self.k = k

    def insert(self, point, node=None, depth=0):
        """
        Insert a point into the KD-Tree.

        Args:
            point (list): The point to insert.
            node (Node, optional): The current node during recursion. Defaults to None.
            depth (int, optional): The current depth during recursion. Defaults to 0.

        Returns:
            Node: The root node of the tree.

        Time Complexity: O(log N) on average, O(N) in the worst case.
        """
        if len(point) != self.k:
            raise ValueError("Point must have exactly k dimensions.")
        if node is None:
            if self.root is None:
                self.root = Node(point, depth % self.k)
                return self.root
            node = self.root
        current_axis = depth % self.k
        if point[current_axis] < node.point[current_axis]:
            if node.left is None:
                node.left = Node(point, (depth + 1) % self.k)
            else:
                self.insert(point, node.left, depth + 1)
        else:
            if node.right is None:
                node.right = Node(point, (depth + 1) % self.k)
            else:
                self.insert(point, node.right, depth + 1)
        return self.root

    def nearest_neighbor(self, target, node=None, depth=0, best=None):
        """
        Find the nearest neighbor to the target point in the KD-Tree.

        Args:
            target (list): The target point.
            node (Node, optional): The current node during recursion. Defaults to None.
            depth (int, optional): The current depth during recursion. Defaults to 0.
            best (tuple, optional): The best (closest) point found so far. Defaults to None.

        Returns:
            tuple: The closest point and its distance to the target.

        Time Complexity: O(log N) on average, O(N) in the worst case.
        """
        if self.root is None:
            raise ValueError("The tree is empty.")
        if node is None:
            node = self.root
            best = (node.point, self.euclidean_distance(node.point, target))
        current_axis = depth % self.k
        if target[current_axis] < node.point[current_axis]:
            next_branch = node.left
            opposite_branch = node.right
        else:
            next_branch = node.right
            opposite_branch = node.left
        if next_branch:
            best = self.nearest_neighbor(target, next_branch, depth + 1, best)
        distance = self.euclidean_distance(node.point, target)
        if distance < best[1]:
            best = (node.point, distance)
        if abs(target[current_axis] - node.point[current_axis]) < best[1]:
            if opposite_branch:
                best = self.nearest_neighbor(target, opposite_branch, depth + 1, best)
        return best

    @staticmethod
    def euclidean_distance(p1, p2):
        """
        Calculate the Euclidean distance between two points.

        Args:
            p1 (list): The first point.
            p2 (list): The second point.

        Returns:
            float: The Euclidean distance between p1 and p2.
        """
        return math.sqrt(sum((x - y) ** 2 for x, y in zip(p1, p2)))


# Example usage:
if __name__ == "__main__":
    # Create a 2D KD-Tree
    kdtree = KDTree(k=2)

    # Insert points
    points = [[2, 3], [5, 4], [9, 6], [4, 7], [8, 1]]
    for point in points:
        kdtree.insert(point)

    # Find the nearest neighbor to the target point [7, 2]
    target = [7, 2]
    nearest, distance = kdtree.nearest_neighbor(target)
    print(f"The nearest point to {target} is {nearest} with distance {distance:.2f}")
