from typing import List, Union
import numpy as np
import time


class AverageMedian:
    """
    Calculates median of a dataset.
    Median is the middle value when data is arranged in order.
    For even-length datasets, takes average of two middle values.

    Time Complexity: O(n log n) due to sorting
    Space Complexity: O(n) for sorting
    """

    @staticmethod
    def calculate(data: List[Union[int, float]]) -> float:
        """
        Calculates median using NumPy.

        Args:
            data: List of numerical values

        Returns:
            Median of the dataset

        Raises:
            ValueError: If data is empty
        """
        if not data:
            raise ValueError("Dataset cannot be empty")

        return float(np.median(data))

    @staticmethod
    def calculate_manual(data: List[Union[int, float]]) -> float:
        """
        Calculates median without NumPy.

        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        if not data:
            raise ValueError("Dataset cannot be empty")

        sorted_data = sorted(data)
        n = len(sorted_data)
        mid = n // 2

        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        return sorted_data[mid]


def benchmark_methods(data: List[Union[int, float]], iterations: int = 1000) -> None:
    """Measures performance of different calculation methods."""
    calculator = AverageMedian()

    # Test NumPy implementation
    start = time.perf_counter()
    for _ in range(iterations):
        numpy_result = calculator.calculate(data)
    numpy_time = time.perf_counter() - start

    # Test manual implementation
    start = time.perf_counter()
    for _ in range(iterations):
        manual_result = calculator.calculate_manual(data)
    manual_time = time.perf_counter() - start

    print("\nPerformance comparison:")
    print(f"NumPy implementation: {numpy_time/iterations:.6f} seconds per iteration")
    print(f"Manual implementation: {manual_time/iterations:.6f} seconds per iteration")

    assert abs(numpy_result - manual_result) < 1e-10, "Results don't match!"


def main():
    calculator = AverageMedian()

    test_cases = [
        ([10, 20, 30, 40, 50], "Odd length array"),
        ([10, 20, 30, 40], "Even length array"),
        ([1, 1, 1, 1, 1], "All same values"),
        ([100, 1, 10, 50, 20], "Unsorted array"),
        ([1.5, 2.5, 3.5, 4.5], "Float values"),
        ([-10, 0, 10, 20], "Negative values"),
    ]

    for data, case_type in test_cases:
        print(f"\nTest case: {case_type}")
        print(f"Dataset: {data}")

        try:
            median = calculator.calculate(data)
            print(f"Median: {median:.4f}")

            # Additional statistics
            print(f"Sorted data: {sorted(data)}")
            print(f"Length: {len(data)}")

            # Benchmark for non-trivial datasets
            if len(data) > 2:
                benchmark_methods(data)

        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
