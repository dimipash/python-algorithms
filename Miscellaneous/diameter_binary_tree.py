class TreeNode:
    """
    Represents a node in a binary tree.

    Attributes:
        value (int): The value of the node.
        left (TreeNode): The left child of the node.
        right (TreeNode): The right child of the node.
    """

    def __init__(self, value):
        """
        Initializes a TreeNode with a given value.

        Args:
            value (int): The value of the node.
        """
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """
    Represents a binary tree.

    Attributes:
        max_diameter (int): The maximum diameter found in the tree.
    """

    def diameter(self, node):
        """
        Calculates the diameter of a binary tree.

        The diameter is the length of the longest path between any two nodes in the tree.
        This path may or may not pass through the root.

        Args:
            node (TreeNode): The root node of the tree.

        Returns:
            int: The diameter of the tree.

        Notes:
            Time Complexity: O(n), where n is the number of nodes in the tree, since we visit each node once.
            Space Complexity: O(h), where h is the height of the tree, due to the recursive call stack.
            In the worst case, the tree is skewed, and the space complexity becomes O(n).
        """
        self.max_diameter = 0  # Initialize maximum diameter

        def height(n):
            """
            Calculates the height of a subtree.

            Args:
                n (TreeNode): The root node of the subtree.

            Returns:
                int: The height of the subtree.
            """
            if not n:
                # Base case: height of null is 0
                return 0
            left_height = height(n.left)  # Height of left subtree
            right_height = height(n.right)  # Height of right subtree
            # Update maximum diameter
            self.max_diameter = max(self.max_diameter, left_height + right_height)
            # Return height
            return max(left_height, right_height) + 1

        height(node)  # Start the height calculation
        return self.max_diameter  # Return the maximum diameter


# Example usage:
if __name__ == "__main__":
    root = TreeNode(1)
    root.left, root.right = TreeNode(2), TreeNode(3)
    root.left.left, root.left.right = TreeNode(4), TreeNode(5)
    tree = BinaryTree()
    print(tree.diameter(root))  # Output: 3 (length of the path 4 -> 2 -> 1 -> 3)
