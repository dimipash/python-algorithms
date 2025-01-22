class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def has_path_sum(self, node, target):
        """
        Determines if there exists a root-to-leaf path in the binary tree such that the sum of the values along the path equals the target sum.

        Parameters:
        node (TreeNode): The current node in the tree.
        target (int): The remaining sum to reach the target along the current path.

        Returns:
        bool: True if such a path exists, False otherwise.

        Approach:
        - Use Depth-First Search (DFS) to traverse the tree.
        - Recursively subtract the current node's value from the target sum.
        - If a leaf node is reached and the remaining target sum is zero, a valid path is found.
        - If the node is None, return False as there's no path through this node.

        Time Complexity:
        - O(N), where N is the number of nodes in the tree, since each node is visited exactly once.

        Space Complexity:
        - O(H), where H is the height of the tree, due to the recursion stack.
        - In the worst case (skewed tree), O(N); in the best case (balanced tree), O(log N).

        Edge Cases:
        - Empty tree (root is None): should return False.
        - Single node tree: return True if the node's value equals the target sum.
        - Multiple paths leading to the target sum: should return True if at least one path satisfies the condition.
        - Negative node values or target sum: handled correctly as the subtraction accounts for negative values.
        """
        if not node:
            return False  # No path through this node
        target -= node.value
        if not node.left and not node.right:  # Leaf node
            return target == 0
        return self.has_path_sum(node.left, target) or self.has_path_sum(
            node.right, target
        )


# Example usage:
if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    tree = BinaryTree()
    target_sum = 22
    result = tree.has_path_sum(root, target_sum)
    print(result)  # Output: True (5 -> 4 -> 11 -> 2)
