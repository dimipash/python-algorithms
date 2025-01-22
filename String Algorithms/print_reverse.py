from typing import Optional


class Node:
    """
    A class representing a node in a singly linked list.

    Attributes:
        data: The value stored in the node
        next: Reference to the next node
    """

    def __init__(self, data: int) -> None:
        self.data = data
        self.next: Optional[Node] = None


def print_reverse(head: Optional[Node]) -> None:
    """
    Prints the linked list in reverse order using recursion.

    Args:
        head: The head node of the linked list

    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(n) due to recursive call stack
    """
    if head is None:
        return

    # Recursively traverse to the end
    print_reverse(head.next)

    # Print current node's data after recursive calls return
    print(head.data, end=" ")


def create_linked_list(values: list[int]) -> Optional[Node]:
    """
    Helper function to create a linked list from a list of values.

    Args:
        values: List of integers to create nodes from

    Returns:
        Head node of the created linked list
    """
    if not values:
        return None

    head = Node(values[0])
    current = head

    for value in values[1:]:
        current.next = Node(value)
        current = current.next

    return head


def main():
    # Create a sample linked list: 1->2->3->4->5
    values = [1, 2, 3, 4, 5]
    head = create_linked_list(values)

    print("Original list:", *values)
    print("Reversed list:", end=" ")
    print_reverse(head)
    print()  # New line after reversed output


if __name__ == "__main__":
    main()
