class TreeNode:
    """
    A class to represent a node in an AVL Tree.

    Attributes:
        value (any): The value stored in the node.
        left (TreeNode): Reference to the left child node.
        right (TreeNode): Reference to the right child node.
        height (int): The height of the node in the tree.
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  # Height is initialized to 1 for new node


class AVLTree:
    """
    A class to represent an AVL Tree, a self-balancing binary search tree.

    Methods:
        insert: Inserts a value into the AVL Tree and rebalances if necessary.
        rotate_left: Performs a left rotation to balance the tree.
        rotate_right: Performs a right rotation to balance the tree.
        get_height: Retrieves the height of a node.
        get_balance: Calculates the balance factor of a node.
        inorder_traversal: Performs an in-order traversal of the tree.
    """

    def insert(self, root, value):
        """
        Inserts a value into the AVL Tree and rebalances if necessary.

        Args:
            root (TreeNode): The root node of the current subtree.
            value (any): The value to be inserted.

        Returns:
            TreeNode: The new root of the subtree after insertion and balancing.
        """
        if not root:
            return TreeNode(value)
        if value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        # Update the height of the current node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Get the balance factor
        balance = self.get_balance(root)

        # Balancing the tree based on the balance factor
        # Case 1: Left Left
        if balance > 1 and value < root.left.value:
            return self.rotate_right(root)
        # Case 2: Right Right
        if balance < -1 and value > root.right.value:
            return self.rotate_left(root)
        # Case 3: Left Right
        if balance > 1 and value > root.left.value:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        # Case 4: Right Left
        if balance < -1 and value < root.right.value:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def rotate_left(self, z):
        """
        Performs a left rotation to balance the tree.

        Args:
            z (TreeNode): The node to be rotated.

        Returns:
            TreeNode: The new root after rotation.
        """
        y = z.right
        z.right = y.left
        y.left = z
        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def rotate_right(self, z):
        """
        Performs a right rotation to balance the tree.

        Args:
            z (TreeNode): The node to be rotated.

        Returns:
            TreeNode: The new root after rotation.
        """
        y = z.left
        z.left = y.right
        y.right = z
        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def get_height(self, node):
        """
        Retrieves the height of a node.

        Args:
            node (TreeNode): The node whose height is to be retrieved.

        Returns:
            int: The height of the node, or 0 if the node is None.
        """
        return node.height if node else 0

    def get_balance(self, node):
        """
        Calculates the balance factor of a node.

        Args:
            node (TreeNode): The node whose balance factor is to be calculated.

        Returns:
            int: The balance factor, which is the difference in heights of left and right subtrees.
        """
        return self.get_height(node.left) - self.get_height(node.right)

    def inorder_traversal(self, node):
        """
        Performs an in-order traversal of the tree.

        Args:
            node (TreeNode): The root node of the subtree to be traversed.

        Returns:
            list: A list of node values in in-order sequence.
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
    avl_tree = AVLTree()
    root = None
    for value in [10, 20, 30, 40, 50, 25]:
        root = avl_tree.insert(root, value)
    print(avl_tree.inorder_traversal(root))
    # Expected Output: [10, 20, 25, 30, 40, 50]
