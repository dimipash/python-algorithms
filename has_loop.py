class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def has_loop(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next  # Move slow by 1
        fast = fast.next.next  # Move fast by 2
        if slow == fast:
            return True
    return False


# Example usage:
if __name__ == "__main__":
    # Create a linked list with a loop
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = second  # Creating a loop
    print(has_loop(head))  # Output: True

    # Remove the loop and check again
    fourth.next = None
    print(has_loop(head))  # Output: False
