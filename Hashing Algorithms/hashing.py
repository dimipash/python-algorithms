"""
Hashing is a technique used to uniquely identify data and facilitate fast data 
retrieval in data structures like hash tables. This module provides examples 
of hashing for password storage and data integrity checks.
"""


class HashTable:
    """
    A simple hash table implementation using chaining to handle collisions.

    Attributes:
        size (int): The size of the hash table.
        table (list): The list that holds the chains for each index.
    """

    def __init__(self, size=10):
        """
        Initializes the hash table with a specified size.

        Parameters:
            size (int): The size of the hash table (default is 10).
        """
        self.size = size
        self.table = [
            [] for _ in range(size)
        ]  # Create a list of empty lists for chaining

    def _hash(self, key):
        """
        Computes the hash value for a given key.

        Parameters:
            key (str): The key to be hashed.

        Returns:
            int: The index in the hash table where the key-value pair will be stored.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Inserts a key-value pair into the hash table.

        Parameters:
            key (str): The key to insert.
            value (any): The value associated with the key.

        Time Complexity:
            - Average case: O(1)
            - Worst case: O(n) (if many keys collide)

        Space Complexity:
            - O(m), where m is the number of slots in the hash table.
        """
        index = self._hash(key)

        # Check if the key already exists and update it
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return

        # If not found, append new key-value pair
        self.table[index].append([key, value])

    def search(self, key):
        """
        Searches for a value by its key in the hash table.

        Parameters:
            key (str): The key to search for.

        Returns:
            any: The value associated with the key if found, else None.

        Time Complexity:
            - Average case: O(1)
            - Worst case: O(n) (if many keys collide)

        Space Complexity:
            - O(1) (no additional space used)
        """
        index = self._hash(key)

        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]

        return None

    def display(self):
        """Displays the contents of the hash table."""
        for index, chain in enumerate(self.table):
            print(f"Index {index}: ", end="")
            for pair in chain:
                print(f"{pair[0]} -> {pair[1]} ", end="")
            print()


# Example usage
if __name__ == "__main__":
    ht = HashTable()

    # Inserting key-value pairs into the hash table
    ht.insert("name", "Alice")
    ht.insert("age", 30)
    ht.insert("city", "New York")

    print("Hash Table Contents:")
    ht.display()

    # Searching for values by keys
    print("\nSearching for 'name':", ht.search("name"))
    print("Searching for 'age':", ht.search("age"))
    print("Searching for 'country':", ht.search("country"))
