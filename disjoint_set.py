class DisjointSet:
    """
    A class to represent a Disjoint Set (Union-Find) data structure.

    This data structure maintains a collection of disjoint (non-overlapping)
    sets and supports two primary operations: Union and Find.

    Attributes:
        parent (list): The parent array where each index represents an element and its value is the parent.
        rank (list): The rank array used for union by rank to optimize the union operation.
    """

    def __init__(self, size):
        """
        Initializes a Disjoint Set with a specified size.

        :param size: The number of elements in the disjoint set.
        """
        self.parent = list(range(size))  # Initially, each element is its own parent
        self.rank = [1] * size  # Used for union by rank

    def find(self, x):
        """
        Finds the representative (root) of the set that contains x.

        This method uses path compression to flatten the structure of the tree,
        ensuring that future queries are faster.

        :param x: The element to find the set for.
        :return: The root of the set containing x.

        Time Complexity: O(α(n)), where α is the inverse Ackermann function, which grows very slowly.
        Space Complexity: O(1)
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        """
        Merges the sets that contain x and y.

        This method uses union by rank to keep the tree flat.

        :param x: An element in one of the sets to be merged.
        :param y: An element in another set to be merged.

        Time Complexity: O(α(n)), where α is the inverse Ackermann function.
        Space Complexity: O(1)
        """
        rootX = self
