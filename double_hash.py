class DoubleHashTable:
    """
    A hash table implementation using double hashing for collision resolution.

    Attributes:
        size (int): The size of the hash table.
        table (list): The list that holds the key-value pairs.
        used (list): A list to track occupied slots in the hash table.
    """

    def __init__(self, size):
        """
        Initializes the Double Hash Table with a specified size.

        Parameters:
            size (int): The size of the hash table.
        """
        self.size = size
        self.table = [None] * size
        self.used = [False] * size  # Track occupied slots

    def _primary_hash(self, key):
        """
        Primary hash function to compute the initial index for a given key.

        Parameters:
            key (int): The key to be hashed.

        Returns:
            int: The index in the hash table where the key should be placed.
        """
        return key % self.size  # Primary hash function

    def _secondary_hash(self, key):
        """
        Secondary hash function to compute the step size for probing.

        Parameters:
            key (int): The key to be hashed.

        Returns:
            int: The step size for probing.
        """
        return 1 + (key % (self.size - 1))  # Secondary hash function

    def insert(self, key, value):
        """
        Inserts a key-value pair into the hash table using double hashing.

        Parameters:
            key (int): The key to insert.
            value (any): The value associated with the key.

        Time Complexity:
            - Average case: O(1)
            - Worst case: O(n) if the table is full and requires probing all slots.

        Space Complexity:
            - O(1) since we only use a fixed-size array.
        """
        index = self._primary_hash(key)
        step_size = self._secondary_hash(key)

        while self.used[index]:  # Find next free slot using double hashing
            index = (index + step_size) % self.size

        self.table[index] = (key, value)
        self.used[index] = True

    def search(self, key):
        """
        Searches for a value by its key in the hash table.

        Parameters:
            key (int): The key to search for.

        Returns:
            any: The value associated with the key if found, else None.

        Time Complexity:
            - Average case: O(1)
            - Worst case: O(n) if we probe all slots without finding the key.

        Space Complexity:
            - O(1) as we do not use additional space during search.
        """
        index = self._primary_hash(key)
        step_size = self._secondary_hash(key)

        start_index = index

        while self.used[index]:
            if self.table[index] and self.table[index][0] == key:
                return self.table[index][1]  # Key found, return value

            index = (index + step_size) % self.size

            if index == start_index:
                break  # If we've looped back to the start, stop search

        return None  # Key not found


# Example usage
if __name__ == "__main__":
    hash_table = DoubleHashTable(7)

    # Inserting key-value pairs into the hash table
    hash_table.insert(10, "A")
    hash_table.insert(20, "B")
    hash_table.insert(15, "C")
    hash_table.insert(7, "D")

    # Searching for values by keys
    print("Search key 10:", hash_table.search(10))  # Output: A
    print("Search key 20:", hash_table.search(20))  # Output: B
    print("Search key 7:", hash_table.search(7))  # Output: D
    print("Search key 99:", hash_table.search(99))  # Output: None
