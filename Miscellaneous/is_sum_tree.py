class TreeNode:
    """
    A class to represent a node in a binary tree.

    Attributes:
        value (int): The value of the node.
        left (TreeNode): Reference to the left child node.
        right (TreeNode): Reference to the right child node.
    """

    def __init__(self, value):
        """
        Initializes a TreeNode with a given value.

        :param value: The integer value of the node.
        """
        self.value = value
        self.left = None
        self.right = None


def is_sum_tree(node):
    """
    Determines whether a given binary tree is a Sum Tree.

    A binary tree is considered a Sum Tree if, for every node in the tree,
    the value of the node is equal to the sum of the values of its left and
    right children. This property must hold for all nodes in the tree.

    :param node: The root node of the binary tree.
    :return: The total sum of the subtree rooted at this node if it is a Sum Tree,
    otherwise returns -1.

    Time Complexity: O(n), where n is the number of nodes in the tree.
    Space Complexity: O(h), where h is the height of the tree (due to recursion stack).
    """
    if not node:  # An empty tree is a Sum Tree
        return 0

    if not node.left and not node.right:  # Leaf nodes
        return node.value

    left_sum = is_sum_tree(node.left)  # Recursively get left subtree sum
    right_sum = is_sum_tree(node.right)  # Recursively get right subtree sum

    # Check if current node satisfies Sum Tree property
    if left_sum == -1 or right_sum == -1 or node.value != left_sum + right_sum:
        return -1  # Return -1 if it's not a Sum Tree

    return left_sum + right_sum + node.value  # Return total sum of this subtree


# Example usage:
if __name__ == "__main__":
    root = TreeNode(26)
    root.left = TreeNode(10)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(6)
    root.right.right = TreeNode(3)

    result = is_sum_tree(root)
    print(f"Is Sum Tree: {result != -1}")  # Output: Is Sum Tree: True
