class FenwickTree:
    """
    A class to represent a Fenwick Tree (Binary Indexed Tree).

    The Fenwick Tree is a data structure that allows efficient updates and prefix sum queries.
    Both operations can be performed in O(log n) time, making it suitable for scenarios with
    frequent updates and queries, such as cumulative frequency tables.

    Attributes:
        size (int): The size of the tree.
        tree (list): The internal array representing the Fenwick Tree.
    """

    def __init__(self, size):
        """
        Initializes the Fenwick Tree with a given size.

        :param size: The size of the Fenwick Tree.
        """
        self.size = size
        self.tree = [0] * (size + 1)  # Initialize tree with zeros (1-based indexing)

    def update(self, index, value):
        """
        Updates the Fenwick Tree by adding a value at a specific index.

        :param index: The index at which to add the value (1-based).
        :param value: The value to add at the specified index.

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        while index <= self.size:
            self.tree[index] += value
            index += index & -index  # Move to the next index

    def query(self, index):
        """
        Computes the prefix sum from the start of the array to the given index.

        :param index: The index up to which to calculate the sum (1-based).
        :return: The prefix sum from index 1 to the specified index.

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index  # Move to the parent index
        return total


# Example usage:
if __name__ == "__main__":
    ft = FenwickTree(5)  # Create a Fenwick Tree of size 5
    ft.update(1, 3)  # Add 3 to index 1
    ft.update(2, 2)  # Add 2 to index 2
    ft.update(3, 5)  # Add 5 to index 3
    print(ft.query(3))  # Output: 10 (3 + 2 + 5)
    print(ft.query(2))  # Output: 5 (3 + 2)
