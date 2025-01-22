class MinHeap:
    """
    A Min Heap implementation that satisfies the heap property, where the value of each node is less than or equal to its children.

    Attributes:
        heap (list): A list to store the elements of the heap.
    """

    def __init__(self):
        """
        Initializes an empty Min Heap.
        """
        self.heap = []

    def insert(self, key):
        """
        Inserts a new key into the Min Heap.

        Parameters:
            key (any): The key to be inserted into the heap.

        Time Complexity:
            - O(log n) for maintaining the heap property after insertion.

        Space Complexity:
            - O(1) since we are adding a single element to the heap.
        """
        self.heap.append(key)  # Add the new key at the end
        self._bubble_up(len(self.heap) - 1)  # Bubble up to maintain heap property

    def _bubble_up(self, index):
        """
        Bubbles up the element at the specified index to maintain the Min Heap property.

        Parameters:
            index (int): The index of the element to bubble up.
        """
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            # Swap
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._bubble_up(parent)  # Recur for the parent

    def extract_min(self):
        """
        Removes and returns the minimum element from the Min Heap.

        Returns:
            any: The minimum element if the heap is not empty, else None.

        Time Complexity:
            - O(log n) for maintaining the heap property after extraction.

        Space Complexity:
            - O(1) since we are removing a single element from the heap.
        """
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()  # Remove and return the root
        root = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move the last element to the root
        self._bubble_down(0)  # Bubble down to maintain heap property
        return root

    def _bubble_down(self, index):
        """
        Bubbles down the element at the specified index to maintain the Min Heap property.

        Parameters:
            index (int): The index of the element to bubble down.
        """
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            # Swap
            self.heap[index], self.heap[smallest] = (
                self.heap[smallest],
                self.heap[index],
            )
            self._bubble_down(smallest)  # Recur for the smallest child

    def get_min(self):
        """
        Returns the minimum element from the Min Heap without removing it.

        Returns:
            any: The minimum element if the heap is not empty, else None.

        Time Complexity:
            - O(1)

        Space Complexity:
            - O(1)
        """
        return self.heap[0] if self.heap else None  # Return the root element


# Example usage
if __name__ == "__main__":
    min_heap = MinHeap()

    # Inserting elements into the min heap
    min_heap.insert(3)
    min_heap.insert(1)
    min_heap.insert(4)
    min_heap.insert(2)

    print("Minimum element:", min_heap.get_min())  # Output: 1
    print("Extracted minimum:", min_heap.extract_min())  # Output: 1
    print("New minimum after extraction:", min_heap.get_min())  # Output: 2
