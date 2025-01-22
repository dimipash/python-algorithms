class Node:
    """
    A Node in the linked list used for handling collisions in the hash table.

    Attributes:
        key (any): The key associated with the node.
        value (any): The value associated with the key.
        next (Node): Pointer to the next node in the linked list.
    """

    def __init__(self, key, value):
        """
        Initializes a new node with the given key and value.

        Parameters:
            key (any): The key to be stored in the node.
            value (any): The value associated with the key.
        """
        self.key = key
        self.value = value
        self.next = None  # Pointer to the next node in the linked list


class HashTable:
    """
    A Hash Table implementation using linked lists to handle collisions.

    Attributes:
        size (int): The size of the hash table.
        table (list): A list of linked list heads for storing key-value pairs.
    """

    def __init__(self, size=10):
        """
        Initializes the Hash Table with a specified size.

        Parameters:
            size (int): The size of the hash table (default is 10).
        """
        self.size = size
        self.table = [None] * size  # Initialize buckets as None

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
        new_node = Node(key, value)

        if self.table[index] is None:
            # No collision, insert directly
            self.table[index] = new_node
        else:
            # Collision occurred; insert at the beginning of the linked list
            new_node.next = self.table[index]
            self.table[index] = new_node

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

        current = self.table[index]

        while current:
            if current.key == key:
                return current.value  # Key found, return value
            current = current.next  # Move to the next node

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

        current = self.table[index]
        prev = None

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next  # Bypass the current node
                else:
                    self.table[index] = current.next  # Remove head node
                return True  # Key successfully deleted

            prev = current
            current = current.next

        return False  # Key not found


# Example usage
if __name__ == "__main__":
    hash_table = HashTable()

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
