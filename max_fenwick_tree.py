class MaxFenwickTree:
    """
    A class to represent a Maximum Fenwick Tree (or Maximum Binary Indexed Tree).

    This data structure supports efficient queries and updates for finding the
    maximum element within a range of an array. It is an extension of the
    standard Fenwick Tree designed specifically for maximum queries.

    Attributes:
        size (int): The size of the tree.
        tree (list): The internal array representing the Maximum Fenwick Tree.
    """

    def __init__(self, size):
        """
        Initializes the Maximum Fenwick Tree with a given size.

        :param size: The size of the Maximum Fenwick Tree.
        """
        self.size = size
        self.tree = [float("-inf")] * (
            size + 1
        )  # Initialize tree with negative infinity

    def update(self, index, value):
        """
        Updates the Maximum Fenwick Tree by setting the value at a specific index.

        :param index: The index at which to update the value (1-based).
        :param value: The value to set at the specified index.

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        while index <= self.size:
            self.tree[index] = max(self.tree[index], value)  # Store the maximum value
            index += index & -index  # Move to the next index

    def query(self, index):
        """
        Computes the maximum value from the start of the array to the given index.

        :param index: The index up to which to calculate the maximum (1-based).
        :return: The maximum value from index 1 to the specified index.

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        max_val = float("-inf")
        while index > 0:
            max_val = max(
                max_val, self.tree[index]
            )  # Update max_val with current tree value
            index -= index & -index  # Move to the parent index
        return max_val

    def range_max(self, left, right):
        """
        Computes the maximum value in a specified range [left, right].

        :param left: The starting index of the range (1-based).
        :param right: The ending index of the range (1-based).
        :return: The maximum value in the range [left, right].

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        return max(self.query(right), self.query(left - 1))  # Get max in range


# Example usage:
if __name__ == "__main__":
    fenwick_tree = MaxFenwickTree(5)
    fenwick_tree.update(1, 10)
    fenwick_tree.update(2, 20)
    fenwick_tree.update(3, 15)

    print(f"Maximum value between index 1 and 3: {fenwick_tree.range_max(1, 3)}")
    # Output: Maximum value between index 1 and 3: 20
