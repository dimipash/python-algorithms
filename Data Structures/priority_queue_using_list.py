from typing import Optional, Any, List, Tuple


class PriorityQueue:
    """
    A priority queue implementation using a sorted list.
    Elements with higher priority are dequeued first.

    Time Complexity:
        - Enqueue: O(n log n) due to sorting
        - Dequeue: O(1)
        - Peek: O(1)
        - Is_empty: O(1)
    Space Complexity: O(n) where n is number of elements
    """

    def __init__(self):
        self.elements: List[Tuple[Any, int]] = []

    def is_empty(self) -> bool:
        """Check if queue is empty."""
        return not self.elements

    def enqueue(self, item: Any, priority: int) -> None:
        """
        Add item with given priority and sort queue.
        Higher priority elements come first.
        """
        self.elements.append((item, priority))
        self.elements.sort(key=lambda x: x[1], reverse=True)

    def dequeue(self) -> Optional[Any]:
        """Remove and return highest priority item."""
        if not self.is_empty():
            return self.elements.pop(0)[0]
        return None

    def peek(self) -> Optional[Any]:
        """Return highest priority item without removing."""
        if not self.is_empty():
            return self.elements[0][0]
        return None


def main():
    # Example usage
    pq = PriorityQueue()

    # Add tasks with priorities
    tasks = [("task1", 2), ("task2", 1), ("task3", 3)]
    for task, priority in tasks:
        pq.enqueue(task, priority)

    print(f"Dequeued: {pq.dequeue()}")  # task3 (highest priority)
    print(f"Next task: {pq.peek()}")  # task1 (next highest)
    print(f"Is empty: {pq.is_empty()}")  # False


if __name__ == "__main__":
    main()
