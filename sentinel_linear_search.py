from typing import List, Optional
import time


class SentinelSearch:
    """
    Implements Sentinel Linear Search algorithm.
    Uses sentinel value to eliminate bounds checking.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    @staticmethod
    def search(arr: List[int], target: int) -> Optional[int]:
        """
        Searches for target using sentinel optimization.

        Args:
            arr: List of integers to search
            target: Value to find

        Returns:
            Index of target if found, None otherwise

        Note: Modifies array temporarily but restores original value
        """
        if not arr:
            return None

        # Save last element and place sentinel
        last = arr[-1]
        arr[-1] = target

        index = 0
        # Search without bounds checking
        while arr[index] != target:
            index += 1

        # Restore original last element
        arr[-1] = last

        # Check if actually found
        if index < len(arr) - 1 or arr[-1] == target:
            return index
        return None


def benchmark_search(arr: List[int], target: int) -> tuple[Optional[int], float]:
    """Measures search performance."""
    start = time.perf_counter()
    result = SentinelSearch.search(arr.copy(), target)
    duration = time.perf_counter() - start
    return result, duration


def compare_with_standard(arr: List[int], target: int) -> None:
    """Compares sentinel search with standard linear search."""
    # Standard linear search
    start = time.perf_counter()
    std_result = next((i for i, x in enumerate(arr) if x == target), None)
    std_time = time.perf_counter() - start

    # Sentinel search
    sent_result, sent_time = benchmark_search(arr, target)

    print(f"Standard search time: {std_time:.6f} seconds")
    print(f"Sentinel search time: {sent_time:.6f} seconds")
    print(f"Improvement: {((std_time - sent_time) / std_time) * 100:.2f}%")


def main():
    # Test cases
    test_cases = [
        ([3, 5, 2, 1, 4], 1, "Middle element"),
        ([3, 5, 2, 1, 4], 4, "Last element"),
        ([3, 5, 2, 1, 4], 3, "First element"),
        ([3, 5, 2, 1, 4], 6, "Not present"),
        ([1], 1, "Single element"),
        ([1, 1, 1, 1, 1], 1, "All same elements"),
    ]

    for arr, target, case_type in test_cases:
        print(f"\nCase: {case_type}")
        print(f"Array: {arr}")
        print(f"Target: {target}")

        result, duration = benchmark_search(arr, target)
        print(f"Found at index: {result}")

        # Compare with standard linear search
        print("\nPerformance comparison:")
        compare_with_standard(arr, target)


if __name__ == "__main__":
    main()
