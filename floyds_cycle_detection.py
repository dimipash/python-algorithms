class Node:
    """Represents a node in a singly linked list."""

    def __init__(self, data):
        """
        Initialize a new node with given data.

        :param data: The data to be stored in the node.
        """
        self.data = data
        self.next = None


def has_cycle(head):
    """
    Detects if there is a cycle in the linked list using Floyd's Tortoise and Hare algorithm.

    :param head: The head node of the linked list.
    :return: True if a cycle is detected, False otherwise.

    Time Complexity: O(N), where N is the number of nodes in the list.
    Space Complexity: O(1), as only a constant amount of extra space is used.
    """
    if head is None:
        return False  # Empty list has no cycle

    tortoise = head
    hare = head

    while hare and hare.next:
        tortoise = tortoise.next  # Move tortoise by 1 step
        hare = hare.next.next  # Move hare by 2 steps
        if tortoise == hare:
            return True  # Cycle detected
    return False  # No cycle detected


# Example usage
if __name__ == "__main__":
    # Create a linked list with a cycle
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = second  # Creating a cycle
    print(has_cycle(head))  # Output: True

    # Remove the cycle and check again
    fourth.next = None
    print(has_cycle(head))  # Output: False
