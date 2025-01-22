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


def find_lca(root, n1, n2):
    """
    Finds the Lowest Common Ancestor (LCA) of two nodes in a binary tree.

    The LCA is defined as the deepest node that is an ancestor of both nodes.

    :param root: The root node of the binary tree.
    :param n1: The value of the first node.
    :param n2: The value of the second node.
    :return: The LCA node if found, otherwise None.

    Time Complexity: O(n), where n is the number of nodes in the tree.
    Space Complexity: O(h), where h is the height of the tree (due to recursion stack).
    """
    if not root:
        return None

    # If either n1 or n2 matches with root's value, report the presence
    if root.value == n1 or root.value == n2:
        return root

    # Look for keys in left and right subtrees
    left_lca = find_lca(root.left, n1, n2)
    right_lca = find_lca(root.right, n1, n2)

    # If both left and right LCA are not None, this node is the LCA
    if left_lca and right_lca:
        return root

    # Otherwise return the non-null child
    return left_lca if left_lca else right_lca


# Example usage:
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    lca = find_lca(root, 4, 5)

    if lca:
        print(f"LCA of 4 and 5: {lca.value}")  # Output: LCA of 4 and 5: 2
    else:
        print("LCA not found.")
