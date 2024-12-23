class TreeNode:
    def __init__(self, value):
        # Initialize the node with value and no children
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def mirror(self, node):
        """
        Recursively mirrors the binary tree by swapping left and right children of each node.

        Key Points:
        - Swaps the left and right children of each node.
        - Recursively applies the mirroring to the subtrees.
        - Modifies the tree structure in place.
        - Time Complexity: O(N), where N is the number of nodes.
        - Space Complexity: O(H), where H is the height of the tree (due to recursion stack).
        """
        if node:
            # Swap the left and right children
            node.left, node.right = node.right, node.left
            # Recursively mirror the new left and right subtrees
            self.mirror(node.left)
            self.mirror(node.right)

    def inorder_traversal(self, node):
        """
        Performs an inorder traversal of the tree and returns the values in a list.

        Key Points:
        - Traverses the tree in the order: left subtree, root, right subtree.
        - Returns a list of node values in inorder sequence.
        - Time Complexity: O(N), where N is the number of nodes.
        - Space Complexity: O(N) for the list of values.
        """
        return (
            (
                self.inorder_traversal(node.left)
                + [node.value]
                + self.inorder_traversal(node.right)
            )
            if node
            else []
        )


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

    # Print inorder traversal before mirroring
    print("Inorder before mirroring:", tree.inorder_traversal(root))
    # Output: [4, 2, 5, 1, 3]

    # Mirror the tree
    tree.mirror(root)

    # Print inorder traversal after mirroring
    print("Inorder after mirroring:", tree.inorder_traversal(root))
    # Output: [3, 1, 5, 2, 4]
