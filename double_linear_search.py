from typing import List, Optional, Tuple
import time


class DoubleLinearSearch:
    """
    Implements Double Linear Search to find elements in two lists simultaneously.
    Time Complexity: O(n) where n is length of lists
    Space Complexity: O(1)
    """

    @staticmethod
    def search(
        list1: List[int], list2: List[int], target: int
    ) -> Optional[Tuple[int, int]]:
        """
        Searches for target value in both lists simultaneously.

        Args:
            list1: First list to search
            list2: Second list to search
            target: Value to find

        Returns:
            Tuple of (list_number, index) if found, None otherwise
            list_number is 1 or 2 indicating which list contained the target

        Raises:
            ValueError: If lists have different lengths
        """
        if len(list1) != len(list2):
            raise ValueError("Lists must have equal length")

        for i in range(len(list1)):
            if list1[i] == target:
                return (1, i)
            if list2[i] == target:
                return (2, i)

        return None


def benchmark_search(
    list1: List[int], list2: List[int], target: int
) -> tuple[Optional[Tuple[int, int]], float]:
    """Measures search performance."""
    start = time.perf_counter()
    result = DoubleLinearSearch.search(list1, list2, target)
    duration = time.perf_counter() - start
    return result, duration


def main():
    # Test cases
    test_cases = [
        ([10, 20, 30, 40, 50], [15, 25, 35, 45, 55], 30, "Found in list1"),
        ([10, 20, 30, 40, 50], [15, 25, 35, 45, 55], 25, "Found in list2"),
        ([10, 20, 30, 40, 50], [15, 25, 35, 45, 55], 100, "Not found"),
        ([1], [2], 1, "Single element lists"),
        ([], [], 1, "Empty lists"),
    ]

    for list1, list2, target, case_type in test_cases:
        try:
            result, duration = benchmark_search(list1, list2, target)

            print(f"\nCase: {case_type}")
            print(f"List1: {list1}")
            print(f"List2: {list2}")
            print(f"Target: {target}")
            if result:
                list_num, index = result
                print(f"Found in list{list_num} at index {index}")
            else:
                print("Target not found")
            print(f"Time: {duration:.6f} seconds")

        except ValueError as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    main()
