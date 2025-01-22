import math

class SparseTable:
    """
    A Sparse Table is a data structure that enables efficient querying of the
    minimum or maximum in a static array over a range of indices.

    Args:
        arr (List[int]): The input array.

    Attributes:
        n (int): The length of the input array.
        log (int): The logarithm of the length of the input array.
        table (List[List[int]]): The Sparse Table.

    Methods:
        range_min_query(left: int, right: int) -> int: Returns the minimum value in the range [left, right].
    """
    def __init__(self, arr: list):
        """
        Initializes the Sparse Table.

        Args:
            arr (List[int]): The input array.
        """
        self.n = len(arr)
        self.log = math.ceil(math.log2(self.n)) + 1
        self.table = [[0] * self.log for _ in range(self.n)]
        # Initialize the first column of the table
        for i in range(self.n):
            self.table[i][0] = arr[i]
        # Build the Sparse Table
        for j in range(1, self.log):
            for i in range(self.n - (1 << j) + 1):
                self.table[i][j] = min(self.table[i][j - 1], self.table[i + (1 << (j - 1))][j - 1])

    def range_min_query(self, left: int, right: int) -> int:
        """
        Returns the minimum value in the range [left, right].

        Args:
            left (int): The left index of the range.
            right (int): The right index of the range.

        Returns:
            int: The minimum value in the range [left, right].
        """
        j = int(math.log2(right - left + 1))
        return min(self.table[left][j], self.table[right - (1 << j) + 1][j])

# Example usage:
arr = [1, 3, 2, 7, 9, 11]
sparse_table = SparseTable(arr)
# Range minimum query from index 1 to 4
result = sparse_table.range_min_query(1, 4)
print(result)  # Output: 2


#### Explanation
#   The `SparseTable` class initializes a data structure that enables efficient querying of the minimum or maximum in a static array over a range of indices. The `__init__` method preprocesses the data in O(n log n) time, allowing queries to be answered in O(1) time. The `range_min_query` method returns the minimum value in the range [left, right].

#### Time Complexity
#   The time complexity of building the Sparse Table is O(n log n), where n is the length of the input array.
#   The time complexity of querying the minimum value in a range is O(1).

#### Space Complexity
#   The space complexity of the Sparse Table is O(n log n), where n is the length of the input array.

#### Notes
#   The Sparse Table is particularly effective for immutable arrays where the range queries are frequent but updates are rare.
#   The `range_min_query` method uses the logarithm of the length of the range to determine the correct column in the Sparse Table to query.