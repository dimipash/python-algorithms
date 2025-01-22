class Node:
    """
    A node in a binomial tree.

    Attributes:
        key (any): The key stored in the node.
        degree (int): The number of children of this node.
        parent (Node): Pointer to the parent node.
        child (Node): Pointer to the first child node.
        sibling (Node): Pointer to the next sibling node.
    """

    def __init__(self, key):
        """
        Initializes a new node with the given key.

        Parameters:
            key (any): The key to be stored in the node.
        """
        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None
        self.sibling = None


class BinomialHeap:
    """
    A Binomial Heap implementation that supports efficient merging of heaps.

    Attributes:
        head (Node): The head of the linked list of root nodes of binomial trees.
    """

    def __init__(self):
        """
        Initializes an empty Binomial Heap.
        """
        self.head = None

    def _merge(self, h1, h2):
        """
        Merges two binomial heaps.

        Parameters:
            h1 (Node): The first heap's root.
            h2 (Node): The second heap's root.

        Returns:
            Node: The merged root of the two heaps.
        """
        if not h1 or not h2:
            return h1 or h2

        # Merging two binomial trees
        if h1.degree <= h2.degree:
            h1.sibling = self._merge(h1.sibling, h2)
            return h1
        else:
            h2.sibling = self._merge(h1, h2.sibling)
            return h2

    def _link(self, y, z):
        """
        Links two binomial trees.

        Parameters:
            y (Node): The child tree to link.
            z (Node): The parent tree to link to.
        """
        y.parent = z
        y.sibling = z.child
        z.child = y
        z.degree += 1

    def insert(self, key):
        """
        Inserts a new key into the Binomial Heap.

        Parameters:
            key (any): The key to be inserted into the heap.

        Time Complexity:
            - O(log n)

        Space Complexity:
            - O(1)
        """
        new_heap = BinomialHeap()
        new_heap.head = Node(key)

        # Merge the new heap with the existing heap
        self.head = self._merge(self.head, new_heap.head)

    def find_min(self):
        """
        Finds the minimum key in the Binomial Heap.

        Returns:
            Node: The node containing the minimum key.

        Time Complexity:
            - O(n)

        Space Complexity:
            - O(1)
        """

        min_node = self.head
        current = self.head

        while current:
            if current.key < min_node.key:
                min_node = current
            current = current.sibling

        return min_node

    def extract_min(self):
        """
        Removes and returns the minimum element from the Binomial Heap.

        Returns:
            any: The minimum element if the heap is not empty, else None.

        Time Complexity:
            - O(log n)

        Space Complexity:
            - O(1)
        """

        # Check if heap is empty
        if not self.head:
            return None

        min_node = self.find_min()

        # Remove min_node from root list
        if min_node == self.head:
            self.head = self.head.sibling
        else:
            current = self.head
            while current.sibling != min_node:
                current = current.sibling
            current.sibling = min_node.sibling

        # Reverse the children of min_node and merge them back into the heap
        child = min_node.child
        min_node.child = None

        while child:
            next_child = child.sibling
            child.sibling = self.head
            self.head = child
            child = next_child

        return min_node.key


# Example usage
if __name__ == "__main__":
    binomial_heap = BinomialHeap()

    # Inserting elements into the binomial heap
    binomial_heap.insert(3)
    binomial_heap.insert(1)
    binomial_heap.insert(4)
    binomial_heap.insert(2)

    print("Minimum element:", binomial_heap.find_min().key)  # Output: 1
    print("Extracted minimum:", binomial_heap.extract_min())  # Output: 1
    print("New minimum after extraction:", binomial_heap.find_min().key)  # Output: 2
