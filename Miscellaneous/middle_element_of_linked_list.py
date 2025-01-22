class Node:
    """
    A class representing a node in a singly linked list.

    Attributes:
        data: The data stored in the node.
        next: Reference to the next node in the list.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


def find_middle(head):
    """
    Find the middle element of a linked list using the two-pointer technique.

    This function uses the "slow and fast pointer" approach to efficiently
    determine the middle node of the linked list.

    Args:
        head (Node): The head node of the linked list.

    Returns:
        Node: The middle node of the linked list.
        If the list has an even number of nodes, it returns the second middle node.

    Time Complexity: O(n)
        Where n is the number of nodes in the linked list.
        We traverse the list once with the fast pointer moving twice as fast.

    Space Complexity: O(1)
        We only use two pointers regardless of the list size.

    Example:
        >>> head = Node(1)
        >>> head.next = Node(2)
        >>> head.next.next = Node(3)
        >>> middle_node = find_middle(head)
        >>> print(middle_node.data)
        2
    """
    if not head or not head.next:
        return head

    slow = fast = head

    while fast and fast.next:
        slow = slow.next  # Move slow pointer by one step
        fast = fast.next.next  # Move fast pointer by two steps

    return slow  # slow pointer will be at the middle node


def create_linked_list(elements):
    """
    Create a linked list from a list of elements.

    Args:
        elements (list): A list of elements to create the linked list from.

    Returns:
        Node: The head of the created linked list.
    """
    if not elements:
        return None

    head = Node(elements[0])
    current = head

    for element in elements[1:]:
        current.next = Node(element)
        current = current.next

    return head


def print_linked_list(head):
    """
    Print the elements of a linked list.

    Args:
        head (Node): The head node of the linked list.
    """
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


# Example usage
if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    elements = [1, 2, 3, 4, 5]
    head = create_linked_list(elements)

    print("Original linked list:")
    print_linked_list(head)

    middle_node = find_middle(head)
    print(f"Middle element: {middle_node.data}")

    # Create a linked list with even number of elements: 1 -> 2 -> 3 -> 4 -> 5 -> 6
    elements = [1, 2, 3, 4, 5, 6]
    head = create_linked_list(elements)

    print("\nLinked list with even number of elements:")
    print_linked_list(head)

    middle_node = find_middle(head)
    print(f"Middle element (second of the two middle): {middle_node.data}")
