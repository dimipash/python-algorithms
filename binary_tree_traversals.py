class TreeNode:
    """Represents a node in a binary tree."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """Provides methods for traversing a binary tree."""

    def _inorder(self, node):
        """Helper method for inorder traversal."""
        if node is None:
            return []
        return self._inorder(node.left) + [node.value] + self._inorder(node.right)

    def _preorder(self, node):
        """Helper method for preorder traversal."""
        if node is None:
            return []
        return [node.value] + self._preorder(node.left) + self._preorder(node.right)

    def _postorder(self, node):
        """Helper method for postorder traversal."""
        if node is None:
            return []
        return self._postorder(node.left) + self._postorder(node.right) + [node.value]

    def inorder(self, node):
        """
        Perform Inorder Traversal: Left subtree, Root, Right subtree.

        Parameters:
        node (TreeNode): The current node.

        Returns:
        list: List of node values in inorder sequence.

        Time Complexity: O(N), where N is the number of nodes.
        Space Complexity: O(N) due to recursion stack in the worst case (skewed tree),
                          O(log N) in the best case (balanced tree). Additionally, O(N)
                          space is used to store the traversal result.
        """
        return self._inorder(node)

    def preorder(self, node):
        """
        Perform Preorder Traversal: Root, Left subtree, Right subtree.

        Parameters:
        node (TreeNode): The current node.

        Returns:
        list: List of node values in preorder sequence.

        Time Complexity: O(N), where N is the number of nodes.
        Space Complexity: O(N) due to recursion stack in the worst case (skewed tree),
                          O(log N) in the best case (balanced tree). Additionally, O(N)
                          space is used to store the traversal result.
        """
        return self._preorder(node)

    def postorder(self, node):
        """
        Perform Postorder Traversal: Left subtree, Right subtree, Root.

        Parameters:
        node (TreeNode): The current node.

        Returns:
        list: List of node values in postorder sequence.

        Time Complexity: O(N), where N is the number of nodes.
        Space Complexity: O(N) due to recursion stack in the worst case (skewed tree),
                          O(log N) in the best case (balanced tree). Additionally, O(N)
                          space is used to store the traversal result.
        """
        return self._postorder(node)


# Example usage:
if __name__ == "__main__":
    # Create the tree structure
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Create an instance of BinaryTree
    tree = BinaryTree()

    # Inorder Traversal: [4, 2, 5, 1, 3]
    print("Inorder:", tree.inorder(root))

    # Preorder Traversal: [1, 2, 4, 5, 3]
    print("Preorder:", tree.preorder(root))

    # Postorder Traversal: [4, 5, 2, 3, 1]
    print("Postorder:", tree.postorder(root))
