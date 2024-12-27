import random


class RandomizedHeap:
    """
    A Randomized Heap implementation that integrates randomization techniques with heap properties.

    Attributes:
        heap (list): A list to store the heap elements.
    """

    def __init__(self):
        """
        Initializes an empty Randomized Heap.
        """
        self.heap = []

    def insert(self, item):
        """
        Inserts an item into the randomized heap.

        Parameters:
            item (any): The item to be added to the heap.

        Time Complexity:
            - O(log n)

        Space Complexity:
            - O(1)
        """
        self.heap.append(item)  # Insert at the end
        self._heapify_up(len(self.heap) - 1)  # Restore heap property

    def _heapify_up(self, idx):
        """
        Maintains the heap property by bubbling up the element at the specified index.

        Parameters:
            idx (int): The index of the element to bubble up.
        """
        parent = (idx - 1) // 2
        if idx > 0 and self.heap[idx] < self.heap[parent]:
            # Swap
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            self._heapify_up(parent)  # Recur upwards

    def extract_min(self):
        """
        Removes and returns the smallest item from the randomized heap.

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
            self.heap[0] = last_value  # Replace root with last
            self._heapify_down(0)  # Restore heap property

        return min_value

    def _heapify_down(self, idx):
        """
        Maintains the heap property by bubbling down the element at the specified index.

        Parameters:
            idx (int): The index of the element to bubble down.
        """
        smallest = idx
        left, right = 2 * idx + 1, 2 * idx + 2

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != idx:
            # Swap
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            self._heapify_down(smallest)  # Recur downwards

    def random_merge(self, other):
        """
        Merges this heap with another randomized heap.

        Parameters:
            other (RandomizedHeap): Another randomized heap to merge with.

        Time Complexity:
            - O(n)

        Space Complexity:
            - O(n)
        """
        self.heap += other.heap  # Combine heaps
        random.shuffle(self.heap)  # Shuffle for randomness
        self.build_heap()  # Restore heap property

    def build_heap(self):
        """
        Builds a heap from an unordered list of elements.

        Time Complexity:
            - O(n)

        Space Complexity:
            - O(1)
        """
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)  # Restore properties


# Example usage
if __name__ == "__main__":
    randomized_heap = RandomizedHeap()

    # Inserting integers into the randomized heap
    for num in [5, 1, 3, 4, 2]:
        randomized_heap.insert(num)

    print("Minimum:", randomized_heap.extract_min())  # Output: 1
    print("Current Heap:", randomized_heap.heap)  # Output: Remaining elements
