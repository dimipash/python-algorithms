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

    Provides methods to get different views of the tree.
    """

    def left_view(self, node):
        """
        Returns the left view of the binary tree.

        The left view consists of the nodes visible when the tree is viewed from the left side.

        Args:
            node (TreeNode): The root node of the tree.

        Returns:
            list: A list of node values representing the left view of the tree.

        Notes:
            Time Complexity: O(n), where n is the number of nodes in the tree, since we visit each node once.
            Space Complexity: O(h), where h is the height of the tree, due to the recursive call stack.
        """
        result = []
        self._left_view_util(node, 0, result)
        return result

    def _left_view_util(self, node, level, result):
        """
        Helper function to get the left view of the binary tree.

        Args:
            node (TreeNode): The current node.
            level (int): The current level.
            result (list): The list to store the node values.
        """
        if not node:
            return
        if level == len(result):  # First node at this level
            result.append(node.value)
        self._left_view_util(node.left, level + 1, result)  # Recur for left child
        self._left_view_util(node.right, level + 1, result)  # Recur for right child

    def right_view(self, node):
        """
        Returns the right view of the binary tree.

        The right view consists of the nodes visible when the tree is viewed from the right side.

        Args:
            node (TreeNode): The root node of the tree.

        Returns:
            list: A list of node values representing the right view of the tree.

        Notes:
            Time Complexity: O(n), where n is the number of nodes in the tree, since we visit each node once.
            Space Complexity: O(h), where h is the height of the tree, due to the recursive call stack.
        """
        result = []
        self._right_view_util(node, 0, result)
        return result

    def _right_view_util(self, node, level, result):
        """
        Helper function to get the right view of the binary tree.

        Args:
            node (TreeNode): The current node.
            level (int): The current level.
            result (list): The list to store the node values.
        """
        if not node:
            return
        if level == len(result):  # First node at this level
            result.append(node.value)
        self._right_view_util(node.right, level + 1, result)  # Recur for right child
        self._right_view_util(node.left, level + 1, result)  # Recur for left child


# Example usage:
if __name__ == "__main__":
    root = TreeNode(1)
    root.left, root.right = TreeNode(2), TreeNode(3)
    root.left.left, root.left.right = TreeNode(4), TreeNode(5)
    root.right.right = TreeNode(6)
    tree = BinaryTree()
    print("Left View:", tree.left_view(root))  # Output: [1, 2, 4]
    print("Right View:", tree.right_view(root))  # Output: [1, 3, 6]
