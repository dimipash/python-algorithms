class HashTable:
    """
    A Hash Table implementation that allows for efficient storage and retrieval of key-value pairs.

    Attributes:
        size (int): The size of the hash table.
        table (list): A list of buckets for storing key-value pairs.
    """

    def __init__(self, size=10):
        """
        Initializes the Hash Table with a specified size.

        Parameters:
            size (int): The size of the hash table (default is 10).
        """
        self.size = size
        self.table = [[] for _ in range(size)]  # Initialize buckets

    def _hash(self, key):
        """
        Computes the hash value for a given key.

        Parameters:
            key (any): The key to be hashed.

        Returns:
            int: The index in the hash table where the key-value pair should be stored.
        """
        return hash(key) % self.size  # Hash function to compute index

    def insert(self, key, value):
        """
        Inserts a key-value pair into the hash table.

        Parameters:
            key (any): The key to insert.
            value (any): The value associated with the key.

        Time Complexity:
            - Average case: O(1)
            - Worst case: O(n) if many collisions occur.

        Space Complexity:
            - O(1) since we only use a fixed-size array.
        """
        index = self._hash(key)

        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)  # Update existing key
                return

        self.table[index].append((key, value))  # Insert new key-value pair

    def search(self, key):
        """
        Searches for a value by its key in the hash table.

        Parameters:
            key (any): The key to search for.

        Returns:
            any: The value associated with the key if found, else None.

        Time Complexity:
            - Average case: O(1)
            - Worst case: O(n) if many collisions occur.

        Space Complexity:
            - O(1) as no additional space is used during search.
        """
        index = self._hash(key)

        for k, v in self.table[index]:
            if k == key:
                return v  # Key found, return value

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
            - Worst case: O(n) if many collisions occur.

        Space Complexity:
            - O(1) since we do not use additional space.
        """
        index = self._hash(key)

        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]  # Remove key-value pair
                return True

        return False  # Key not found


# Example usage
if __name__ == "__main__":
    hash_table = HashTable()

    # Inserting key-value pairs into the hash table
    hash_table.insert("apple", 1)
    hash_table.insert("banana", 2)
    hash_table.insert("orange", 3)

    # Searching for values by keys
    print("Search apple:", hash_table.search("apple"))  # Output: 1
    print("Search banana:", hash_table.search("banana"))  # Output: 2
    print("Search grape:", hash_table.search("grape"))  # Output: None

    # Deleting a key
    hash_table.delete("banana")
    print("Search banana after deletion:", hash_table.search("banana"))  # Output: None
