class Node:
    """Represents a node in a singly linked list."""

    def __init__(self, data):
        """
        Initialize a new node with given data.

        :param data: The data to be stored in the node.
        """
        self.data = data
        self.next = None  # Initially points to nothing


class LinkedList:
    """A singly linked list implementation."""

    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None  # Head of the list

    def insert(self, data):
        """
        Insert a new node at the beginning of the linked list.

        :param data: The data to be inserted.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        """
        Delete the first occurrence of a node with the given data.

        :param key: The data to be deleted.
        Time Complexity: O(N) where N is the number of nodes
        Space Complexity: O(1)
        """
        current = self.head
        previous = None

        # If head node itself holds the key
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        # Search for the key
        while current and current.data != key:
            previous = current
            current = current.next

        # If key was not present in the list
        if current is None:
            return

        # Remove the node
        previous.next = current.next
        current = None

    def display(self):
        """
        Display the elements of the linked list.

        Time Complexity: O(N) where N is the number of nodes
        Space Complexity: O(1)
        """
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))


# Example usage
if __name__ == "__main__":
    # Create a linked list and insert some elements
    ll = LinkedList()
    ll.insert(3)
    ll.insert(2)
    ll.insert(1)

    print("Linked list after insertion:")
    ll.display()  # Output: 1 -> 2 -> 3

    # Delete an element
    ll.delete(2)
    print("Linked list after deleting 2:")
    ll.display()  # Output: 1 -> 3
