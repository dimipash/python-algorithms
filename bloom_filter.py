import hashlib


class BloomFilter:
    """
    A Bloom Filter is a probabilistic data structure used to test whether an element is a member of a set.
    It allows for fast membership testing with the possibility of false positives but guarantees no false negatives.

    Attributes:
        size (int): The size of the bit array.
        num_hashes (int): The number of hash functions to use.
        bit_array (list): A list representing the bit array initialized to 0.
    """

    def __init__(self, size, num_hashes):
        """
        Initializes the Bloom Filter with a specified size and number of hash functions.

        Parameters:
            size (int): The size of the bit array.
            num_hashes (int): The number of hash functions.
        """
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = [0] * size  # Initialize a bit array

    def _hashes(self, item):
        """
        Generates hash values for the given item using different hash functions.

        Parameters:
            item (str): The item to be hashed.

        Returns:
            list: A list of hash values as hexadecimal strings.
        """
        return [
            hashlib.md5(item.encode()).hexdigest(),
            hashlib.sha1(item.encode()).hexdigest(),
            hashlib.sha256(item.encode()).hexdigest(),
        ]

    def _get_indices(self, item):
        """
        Gets indices in the bit array based on the hash values of the item.

        Parameters:
            item (str): The item for which to get indices.

        Returns:
            list: A list of indices corresponding to the hash values.
        """
        return [int(h, 16) % self.size for h in self._hashes(item)]

    def add(self, item):
        """
        Adds an item to the Bloom Filter by setting bits in the bit array.

        Parameters:
            item (str): The item to add.

        Time Complexity: O(k), where k is the number of hash functions.
        Space Complexity: O(1), as we only use a fixed-size bit array.
        """
        for index in self._get_indices(item):
            self.bit_array[index] = 1

    def contains(self, item):
        """
        Checks if an item is possibly in the Bloom Filter.

        Parameters:
            item (str): The item to check.

        Returns:
            bool: True if the item is possibly in the filter, False if it is definitely not.

        Time Complexity: O(k), where k is the number of hash functions.
        Space Complexity: O(1), as we only use a fixed-size bit array.
        """
        return all(self.bit_array[index] for index in self._get_indices(item))


# Example usage
if __name__ == "__main__":
    bloom = BloomFilter(size=100, num_hashes=3)

    # Adding items to the Bloom Filter
    bloom.add("hello")
    bloom.add("world")

    # Checking membership
    print("Contains 'hello':", bloom.contains("hello"))  # Output: True
    print("Contains 'world':", bloom.contains("world"))  # Output: True
    print("Contains 'python':", bloom.contains("python"))  # Output: False
