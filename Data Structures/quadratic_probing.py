class QuadraticProbingHashTable:
    """
    A hash table implementation using quadratic probing for collision resolution.

    Attributes:
        size (int): The size of the hash table.
        table (list): A list to store key-value pairs.
    """

    def __init__(self, size=10):
        """
        Initializes the Quadratic Probing Hash Table with a specified size.

        Parameters:
            size (int): The size of the hash table (default is 10).
        """
        self.size = size
        self.table = [None] * size  # Initialize the table with None

    def _hash(self, key):
        """
        Computes the hash value for a given key.

        Parameters:
            key (any): The key to be hashed.

        Returns:
            int: The index in the hash table where the key-value pair should be stored.
        """
        return hash(key) % self.size  # Basic hash function

    def insert(self, key, value):
        """
        Inserts a key-value pair into the hash table using quadratic probing.

        Parameters:
            key (any): The key to insert.
            value (any): The value associated with the key.

        Time Complexity:
            - Average case: O(1)
            - Worst case: O(N) if the table is nearly full.

        Space Complexity:
            - O(1) since we only use a fixed-size array.
        """
        index = self._hash(key)

        for i in range(self.size):
            new_index = (index + i * i) % self.size  # Quadratic probing
            if self.table[new_index] is None or self.table[new_index][0] == key:
                self.table[new_index] = (key, value)  # Insert key-value pair
                return

    def search(self, key):
        """
        Searches for a value by its key in the hash table.

        Parameters:
            key (any): The key to search for.

        Returns:
            any: The value associated with the key if found, else None.

        Time Complexity:
            - Average case: O(1)
            - Worst case: O(N) if many collisions occur.

        Space Complexity:
            - O(1) as no additional space is used during search.
        """
        index = self._hash(key)

        for i in range(self.size):
            new_index = (index + i * i) % self.size
            if self.table[new_index] is None:
                break  # Key not found
            if self.table[new_index][0] == key:
                return self.table[new_index][1]  # Return value

        return None  # Key not found

    def delete(self, key):
        """
        Deletes a key-value pair from the hash table.

        Parameters:
            key (any): The key to delete.

        Returns:
            bool: True if the key was found and deleted, False otherwise.

        Time Complexity:
            - Average case: O(1)
            - Worst case: O(N) if many collisions occur.

        Space Complexity:
            - O(1) since we do not use additional space.
        """
        index = self._hash(key)

        for i in range(self.size):
            new_index = (index + i * i) % self.size
            if self.table[new_index] is None:
                return False  # Key not found
            if self.table[new_index][0] == key:
                self.table[new_index] = None  # Remove key-value pair
                return True

        return False  # Key not found


# Example usage
if __name__ == "__main__":
    hash_table = QuadraticProbingHashTable()

    # Inserting key-value pairs into the hash table
    hash_table.insert("apple", 1)
    hash_table.insert("banana", 2)
    hash_table.insert("orange", 3)
    hash_table.insert("banana", 4)  # Updating value for existing key

    # Searching for values by keys
    print("Search apple:", hash_table.search("apple"))  # Output: 1
    print("Search banana:", hash_table.search("banana"))  # Output: 4
    print("Search grape:", hash_table.search("grape"))  # Output: None

    # Deleting a key
    hash_table.delete("banana")
    print("Search banana after deletion:", hash_table.search("banana"))  # Output: None
