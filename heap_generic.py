import heapq


class GenericMinHeap:
    """
    A generic min-heap implementation that can manage elements of any data type.

    Attributes:
        heap (list): A list to store the heap elements.
    """

    def __init__(self):
        """
        Initializes an empty Generic Min Heap.
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
        heapq.heappush(self.heap, item)  # Add item to the heap

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
        return (
            heapq.heappop(self.heap) if self.heap else None
        )  # Remove and return the smallest item

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
        return (
            self.heap[0] if self.heap else None
        )  # Return the smallest item without removing

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
    min_heap = GenericMinHeap()

    # Inserting integers into the min-heap
    min_heap.insert(3)
    min_heap.insert(1)
    min_heap.insert(4)
    min_heap.insert(2)

    print("Minimum element:", min_heap.get_min())  # Output: 1
    print("Extracted minimum:", min_heap.extract_min())  # Output: 1
    print("New minimum after extraction:", min_heap.get_min())  # Output: 2

    # Working with different data types
    min_heap.insert("apple")
    min_heap.insert("banana")
    min_heap.insert("cherry")

    print(
        "Minimum string element:", min_heap.get_min()
    )  # Output may vary based on type comparison
