class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def sum_nodes(self, node):
        """
        Recursively calculates the sum of all node values in the binary tree.

        Parameters:
        node (TreeNode): The root node of the tree or subtree.

        Returns:
        int: The sum of all node values.

        Step-by-Step Explanation:
        1. If the node is None, return 0 (base case).
        2. Otherwise, calculate the sum as:
           - Current node's value
           - Plus the sum of the left subtree
           - Plus the sum of the right subtree
        3. Recursively apply this to all nodes in the tree.

        Time Complexity: O(n), where n is the number of nodes.
        Space Complexity: O(h), where h is the height of the tree.
        """
        if not node:
            return 0  # Base case: no node, sum is 0
        return (
            node.value + self.sum_nodes(node.left) + self.sum_nodes(node.right)
        )  # Recursive sum


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

    # Calculate and print the sum of all node values
    total_sum = tree.sum_nodes(root)
    print(total_sum)  # Output: 15
