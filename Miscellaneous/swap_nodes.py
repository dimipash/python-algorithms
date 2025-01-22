from typing import Optional


class ListNode:
    """
    A class representing a node in a singly linked list.

    Attributes:
        val: The value stored in the node
        next: Reference to the next node
    """

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Swaps adjacent nodes in a linked list.

        Args:
            head: The head node of the linked list

        Returns:
            Head of the modified linked list

        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(1) as only pointers are modified
        """
        # Handle empty list or single node
        if not head or not head.next:
            return head

        dummy = ListNode(0, head)  # Dummy node to handle edge cases
        prev = dummy

        while prev.next and prev.next.next:
            # Store nodes to be swapped
            first = prev.next
            second = first.next

            # Perform the swap
            prev.next = second
            first.next = second.next
            second.next = first

            # Move to next pair
            prev = first

        return dummy.next


def create_linked_list(values: list[int]) -> Optional[ListNode]:
    """Helper function to create a linked list from values."""
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


def print_list(head: Optional[ListNode]) -> list[int]:
    """Helper function to convert linked list to array."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def main():
    # Create sample linked list: 1->2->3->4
    values = [1, 2, 3, 4]
    head = create_linked_list(values)

    solution = Solution()
    swapped = solution.swapPairs(head)

    print("Original:", values)
    print("Swapped:", print_list(swapped))  # [2, 1, 4, 3]


if __name__ == "__main__":
    main()
