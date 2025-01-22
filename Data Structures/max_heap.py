class MaxHeap:
    """
    A Max Heap implementation that maintains the max-heap property.

    Attributes:
        heap (list): A list to store the heap elements.
    """

    def __init__(self):
        """
        Initializes an empty Max Heap.
        """
        self.heap = []

    def insert(self, item):
        """
        Inserts an item into the max-heap.

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
        Maintains the max-heap property by bubbling up the element at the specified index.

        Parameters:
            index (int): The index of the element to bubble up.
        """
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent]:
            # Swap
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)  # Recur for parent

    def extract_max(self):
        """
        Removes and returns the maximum element from the max-heap.

        Returns:
            any: The maximum element if the heap is not empty, else None.

        Time Complexity:
            - O(log n)

        Space Complexity:
            - O(1)
        """
        if not self.heap:
            return None

        max_value = self.heap[0]
        last_value = self.heap.pop()  # Remove last element

        if self.heap:
            self.heap[0] = last_value  # Move last to root
            self._heapify_down(0)  # Maintain heap property

        return max_value

    def _heapify_down(self, index):
        """
        Maintains the max-heap property by bubbling down the element at the specified index.

        Parameters:
            index (int): The index of the element to bubble down.
        """
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            # Swap
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)  # Recur for largest

    def get_max(self):
        """
        Returns the maximum element from the max-heap without removing it.

        Returns:
            any: The maximum element if the heap is not empty, else None.

        Time Complexity:
            - O(1)

        Space Complexity:
            - O(1)
        """
        return self.heap[0] if self.heap else None  # Return max without removing

    def is_empty(self):
        """
        Checks if the max-heap is empty.

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
    max_heap = MaxHeap()

    # Inserting integers into the max-heap
    max_heap.insert(3)
    max_heap.insert(1)
    max_heap.insert(4)
    max_heap.insert(2)

    print("Maximum element:", max_heap.get_max())  # Output: 4
    print("Extracted maximum:", max_heap.extract_max())  # Output: 4
    print("New maximum after extraction:", max_heap.get_max())  # Output: 3
