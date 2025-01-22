from typing import List, Optional
import time


class InterpolationSearch:
    """
    Implements Interpolation Search algorithm for sorted arrays.
    Most efficient for uniformly distributed data.

    Time Complexity:
        Average case: O(log(log n))
        Worst case: O(n)
    Space Complexity: O(1)
    """

    @staticmethod
    def search(arr: List[int], target: int) -> Optional[int]:
        """
        Searches for target value using interpolation search.

        Args:
            arr: Sorted list of integers
            target: Value to find

        Returns:
            Index of target if found, None otherwise
        """
        if not arr:
            return None

        low = 0
        high = len(arr) - 1

        while (
            low <= high
            and target >= arr[low]
            and target <= arr[high]
            and arr[low] != arr[high]
        ):  # Prevent division by zero

            # Calculate probable position using interpolation formula
            pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))

            if arr[pos] == target:
                return pos
            elif arr[pos] < target:
                low = pos + 1
            else:
                high = pos - 1

        # Check boundaries
        if low <= high and arr[low] == target:
            return low

        return None


def benchmark_search(arr: List[int], target: int) -> tuple[Optional[int], float]:
    """Measures search performance."""
    start = time.perf_counter()
    result = InterpolationSearch.search(arr, target)
    duration = time.perf_counter() - start
    return result, duration


def main():
    # Test cases with different distributions
    test_cases = [
        # Uniform distribution
        (list(range(10, 110, 10)), 70, "Uniform distribution"),
        # Non-uniform distribution
        ([1, 4, 7, 10, 20, 50, 100], 20, "Non-uniform distribution"),
        # Edge cases
        ([1, 2, 3, 4, 5], 1, "First element"),
        ([1, 2, 3, 4, 5], 5, "Last element"),
        ([1, 2, 3, 4, 5], 6, "Not present"),
        ([], 1, "Empty array"),
        ([1], 1, "Single element"),
    ]

    for arr, target, case_type in test_cases:
        result, duration = benchmark_search(arr, target)

        print(f"\nCase: {case_type}")
        print(f"Array: {arr}")
        print(f"Target: {target}")
        print(f"Found at index: {result}")
        print(f"Time: {duration:.6f} seconds")


if __name__ == "__main__":
    main()
