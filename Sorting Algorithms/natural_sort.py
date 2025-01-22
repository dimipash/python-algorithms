from typing import List
import re


class NaturalSorter:
    """
    Implements natural sorting for strings containing mixed alphanumeric content.
    Sorts in human-intuitive order (e.g., file2 comes before file10).
    """

    @staticmethod
    def natural_key(text: str) -> List:
        """
        Converts string into sortable key by splitting into numeric and non-numeric parts.

        Args:
            text: Input string to convert

        Returns:
            List of alternating string and integer parts

        Example:
            'file123test' -> ['file', 123, 'test']
        """

        def convert(part: str) -> int | str:
            return int(part) if part.isdigit() else part.lower()

        return [convert(c) for c in re.split("([0-9]+)", text)]

    @classmethod
    def sort(cls, arr: List[str]) -> List[str]:
        """
        Sorts list of strings using natural sorting order.

        Args:
            arr: List of strings to sort

        Returns:
            Naturally sorted list of strings

        Time Complexity: O(n log n * m) where m is average string length
        Space Complexity: O(n) for storing converted keys
        """
        return sorted(arr, key=cls.natural_key)


def demonstrate_sorting():
    """Shows different cases of natural sorting."""
    test_cases = [
        # Mixed alphanumeric
        ["file1", "file10", "file2", "file20", "file3"],
        # Version numbers
        ["v1.2", "v1.10", "v2.1", "v1.3"],
        # Mixed case
        ["File1", "file2", "FILE3", "file10"],
        # Special cases
        ["1", "10", "2", "20", "3"],
        ["", "1", "a", "2", "b"],
    ]

    sorter = NaturalSorter()

    for case in test_cases:
        original = case.copy()
        sorted_list = sorter.sort(case)
        print(f"\nOriginal: {original}")
        print(f"Sorted  : {sorted_list}")


if __name__ == "__main__":
    demonstrate_sorting()
