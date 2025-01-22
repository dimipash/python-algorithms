class MinHeap:
    """
    A Min Heap implementation that maintains the min-heap property.

    Attributes:
        heap (list): A list to store the heap elements.
    """

    def __init__(self):
        """
        Initializes an empty Min Heap.
        """
        self.heap = []

    def insert(self, item):
        """
        Inserts an item into the min-heap.

        Parameters:
            item (any): The item to be added to the heap.

        Time Complexity:
            - O(log n)

        Space Complexity:
            - O(1)
        """
        self.heap.append(item)  # Add item to the end
        self._heapify_up(len(self.heap) - 1)  # Maintain heap property

    def _heapify_up(self, index):
        """
        Maintains the min-heap property by bubbling up the element at the specified index.

        Parameters:
            index (int): The index of the element to bubble up.
        """
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            # Swap
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)  # Recur for parent

    def extract_min(self):
        """
        Removes and returns the smallest item from the min-heap.

        Returns:
            any: The smallest item if the heap is not empty, else None.

        Time Complexity:
            - O(log n)

        Space Complexity:
            - O(1)
        """
        if not self.heap:
            return None

        min_value = self.heap[0]
        last_value = self.heap.pop()  # Remove last element

        if self.heap:
            self.heap[0] = last_value  # Move last to root
            self._heapify_down(0)  # Maintain heap property

        return min_value

    def _heapify_down(self, index):
        """
        Maintains the min-heap property by bubbling down the element at the specified index.

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
            self._heapify_down(smallest)  # Recur for smallest

    def get_min(self):
        """
        Returns the smallest item from the min-heap without removing it.

        Returns:
            any: The smallest item if the heap is not empty, else None.

        Time Complexity:
            - O(1)

        Space Complexity:
            - O(1)
        """
        return self.heap[0] if self.heap else None  # Return min without removing

    def is_empty(self):
        """
        Checks if the min-heap is empty.

        Returns:
            bool: True if the heap is empty, False otherwise.

        Time Complexity:
            - O(1)

        Space Complexity:
            - O(1)
        """
        return len(self.heap) == 0  # Check if the heap is empty


# Example usage
if __name__ == "__main__":
    min_heap = MinHeap()

    # Inserting integers into the min-heap
    min_heap.insert(3)
    min_heap.insert(1)
    min_heap.insert(4)
    min_heap.insert(2)

    print("Minimum element:", min_heap.get_min())  # Output: 1
    print("Extracted minimum:", min_heap.extract_min())  # Output: 1
    print("New minimum after extraction:", min_heap.get_min())  # Output: 2
