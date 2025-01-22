from typing import Optional, Any, List


class Queue:
    """
    A FIFO queue implementation using a list.

    Time Complexity:
        - Enqueue: O(1) - append to end
        - Dequeue: O(n) - remove from front requires shifting elements
        - Peek: O(1) - access front element
        - Is_empty: O(1) - check length
    Space Complexity: O(n) where n is number of elements
    """

    def __init__(self):
        self.items: List[Any] = []

    def is_empty(self) -> bool:
        """Check if queue is empty."""
        return not self.items

    def enqueue(self, item: Any) -> None:
        """Add item to end of queue."""
        self.items.append(item)

    def dequeue(self) -> Optional[Any]:
        """Remove and return front item."""
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def peek(self) -> Optional[Any]:
        """Return front item without removing."""
        if not self.is_empty():
            return self.items[0]
        return None

    def size(self) -> int:
        """Return number of items in queue."""
        return len(self.items)


def main():
    # Example usage
    queue = Queue()

    # Add elements
    for i in range(1, 4):
        queue.enqueue(i)
        print(f"Enqueued: {i}")

    print(f"Front element: {queue.peek()}")  # 1
    print(f"Dequeued: {queue.dequeue()}")  # 1
    print(f"Queue size: {queue.size()}")  # 2
    print(f"Is empty: {queue.is_empty()}")  # False


if __name__ == "__main__":
    main()
