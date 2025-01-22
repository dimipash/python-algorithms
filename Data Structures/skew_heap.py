class SkewHeapNode:
    """
    A node in a skew heap.

    Attributes:
        key (any): The key stored in the node.
        left (SkewHeapNode): Pointer to the left child node.
        right (SkewHeapNode): Pointer to the right child node.
    """

    def __init__(self, key):
        """
        Initializes a new node with the given key.

        Parameters:
            key (any): The key to be stored in the node.
        """
        self.key = key
        self.left = None
        self.right = None


class SkewHeap:
    """
    A Skew Heap implementation that supports efficient merging of heaps.
    """

    def merge(self, h1, h2):
        """
        Merges two skew heaps.

        Parameters:
            h1 (SkewHeapNode): The first heap's root.
            h2 (SkewHeapNode): The second heap's root.

        Returns:
            SkewHeapNode: The merged root of the two heaps.

        Time Complexity:
            - O(log n) on average due to recursive merging.

        Space Complexity:
            - O(log n) due to recursion stack in the worst case.
        """
        if not h1:
            return h2
        if not h2:
            return h1

        # Ensure h1 has the smaller root
        if h1.key > h2.key:
            h1, h2 = h2, h1

        # Merge right subtree with h2
        h1.right = self.merge(h1.right, h2)

        # Swap left and right children
        h1.left, h1.right = h1.right, h1.left

        return h1

    def insert(self, root, key):
        """
        Inserts a new key into the skew heap.

        Parameters:
            root (SkewHeapNode): The root of the heap.
            key (any): The key to be inserted.

        Returns:
            SkewHeapNode: The new root after insertion.

        Time Complexity:
            - O(log n) on average due to merging operation.

        Space Complexity:
            - O(log n) due to recursion stack in the worst case.
        """
        new_node = SkewHeapNode(key)
        return self.merge(root, new_node)

    def extract_min(self, root):
        """
        Removes and returns the minimum element from the skew heap.

        Parameters:
            root (SkewHeapNode): The root of the heap.

        Returns:
            tuple: A tuple containing the minimum value and the new root.
                   If the heap is empty, returns (None, None).

        Time Complexity:
            - O(log n) on average due to merging left and right subtrees.

        Space Complexity:
            - O(log n) due to recursion stack in the worst case.
        """
        if not root:
            return None, None

        min_value = root.key
        # Merge left and right subtrees
        root = self.merge(root.left, root.right)

        return min_value, root  # Return min value and new root


# Example usage
if __name__ == "__main__":
    skew_heap = SkewHeap()
    root = None

    for num in [5, 1, 3, 4, 2]:
        root = skew_heap.insert(root, num)

    min_value, root = skew_heap.extract_min(root)
    print("Minimum:", min_value)  # Output: 1
    print(
        "Current Root:", root.key if root else "Heap is empty"
    )  # Output: New root after extraction
