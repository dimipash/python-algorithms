class Node:
    """
    A class to represent a node in a binary tree.

    Attributes:
        value (any): The value stored in the node.
        left (Node): Reference to the left child node.
        right (Node): Reference to the right child node.
    """

    def __init__(self, value):
        self.value = value  # Value stored in the node
        self.left = None  # Reference to the left child
        self.right = None  # Reference to the right child


class BinaryTree:
    """
    A class to represent a binary tree data structure.

    Attributes:
        root (Node): The root node of the tree.
    """

    def __init__(self, root_value):
        """
        Initializes the binary tree with a root node containing root_value.

        Args:
            root_value (any): The value for the root node.
        """
        self.root = Node(root_value)  # Create the root node of the tree

    def insert(self, value):
        """
        Inserts a new node with the given value into the binary tree using level order traversal.

        Args:
            value (any): The value to be inserted into the tree.
        """
        if self.root is None:
            self.root = Node(value)  # If the tree is empty, set root to new node
            return
        queue = [self.root]  # Initialize queue with root for level order traversal
        while queue:
            current_node = queue.pop(0)  # Dequeue the first node
            if current_node.left is None:
                current_node.left = Node(value)  # Add new node to the left if empty
                return
            else:
                queue.append(current_node.left)  # Enqueue the left child
            if current_node.right is None:
                current_node.right = Node(value)  # Add new node to the right if empty
                return
            else:
                queue.append(current_node.right)  # Enqueue the right child

    def inorder_traversal(self, node):
        """
        Performs in-order traversal of the binary tree and prints the node values.

        In-order traversal visits nodes in the following order: left subtree, root node, right subtree.

        Args:
            node (Node): The current node being visited.
        """
        if node:
            self.inorder_traversal(node.left)  # Traverse left subtree
            print(node.value, end=" ")  # Visit the current node
            self.inorder_traversal(node.right)  # Traverse right subtree

    def preorder_traversal(self, node):
        """
        Performs pre-order traversal of the binary tree and prints the node values.

        Pre-order traversal visits nodes in the following order: root node, left subtree, right subtree.

        Args:
            node (Node): The current node being visited.
        """
        if node:
            print(node.value, end=" ")  # Visit the current node
            self.preorder_traversal(node.left)  # Traverse left subtree
            self.preorder_traversal(node.right)  # Traverse right subtree

    def postorder_traversal(self, node):
        """
        Performs post-order traversal of the binary tree and prints the node values.

        Post-order traversal visits nodes in the following order: left subtree, right subtree, root node.

        Args:
            node (Node): The current node being visited.
        """
        if node:
            self.postorder_traversal(node.left)  # Traverse left subtree
            self.postorder_traversal(node.right)  # Traverse right subtree
            print(node.value, end=" ")  # Visit the current node

    def print_tree(self):
        """
        Prints the binary tree using in-order, pre-order, and post-order traversals.
        """
        print("In-order Traversal:")
        self.inorder_traversal(self.root)
        print("\nPre-order Traversal:")
        self.preorder_traversal(self.root)
        print("\nPost-order Traversal:")
        self.postorder_traversal(self.root)


# Example usage:
if __name__ == "__main__":
    # Create a binary tree with root node 1
    bt = BinaryTree(1)

    # Insert nodes into the tree
    bt.insert(2)
    bt.insert(3)
    bt.insert(4)
    bt.insert(5)

    # Print the tree using different traversal methods
    bt.print_tree()
