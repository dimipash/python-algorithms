from typing import List, Union
import numpy as np
import time


class AverageAbsoluteDeviation:
    """
    Calculates Average Absolute Deviation (AAD) of a dataset.
    AAD measures data dispersion by averaging absolute deviations from the mean.

    Time Complexity: O(n) where n is the size of dataset
    Space Complexity: O(n) for storing deviations
    """

    @staticmethod
    def calculate(data: List[Union[int, float]]) -> float:
        """
        Calculates AAD for given dataset.

        Args:
            data: List of numerical values

        Returns:
            Average Absolute Deviation

        Raises:
            ValueError: If data is empty
        """
        if not data:
            raise ValueError("Dataset cannot be empty")

        # Calculate mean - O(n)
        mean = np.mean(data)

        # Calculate absolute deviations - O(n)
        absolute_deviations = np.abs(data - mean)

        # Calculate AAD - O(n)
        return float(np.mean(absolute_deviations))

    @staticmethod
    def calculate_without_numpy(data: List[Union[int, float]]) -> float:
        """
        Calculates AAD without using NumPy.
        Demonstrates pure Python implementation.
        """
        if not data:
            raise ValueError("Dataset cannot be empty")

        # Calculate mean
        mean = sum(data) / len(data)

        # Calculate absolute deviations
        absolute_deviations = [abs(x - mean) for x in data]

        # Calculate AAD
        return sum(absolute_deviations) / len(absolute_deviations)


def benchmark_methods(data: List[Union[int, float]], iterations: int = 1000) -> None:
    """Compares performance of different AAD calculation methods."""
    calculator = AverageAbsoluteDeviation()

    # Test NumPy implementation
    start = time.perf_counter()
    for _ in range(iterations):
        numpy_result = calculator.calculate(data)
    numpy_time = time.perf_counter() - start

    # Test pure Python implementation
    start = time.perf_counter()
    for _ in range(iterations):
        python_result = calculator.calculate_without_numpy(data)
    python_time = time.perf_counter() - start

    print("\nPerformance comparison:")
    print(f"NumPy implementation: {numpy_time/iterations:.6f} seconds per iteration")
    print(
        f"Pure Python implementation: {python_time/iterations:.6f} seconds per iteration"
    )

    assert abs(numpy_result - python_result) < 1e-10, "Results don't match!"


def main():
    calculator = AverageAbsoluteDeviation()

    test_cases = [
        ([10, 20, 30, 40, 50], "Basic case"),
        ([1, 1, 1, 1, 1], "All same values"),
        ([0, 100], "Two values"),
        ([1.5, 2.5, 3.5], "Float values"),
        ([-10, 0, 10], "Negative values"),
    ]

    for data, case_type in test_cases:
        print(f"\nTest case: {case_type}")
        print(f"Dataset: {data}")

        try:
            aad = calculator.calculate(data)
            print(f"Average Absolute Deviation: {aad:.4f}")

            # Additional statistics
            print(f"Mean: {np.mean(data):.4f}")
            print(f"Standard Deviation: {np.std(data):.4f}")

            # Benchmark for non-trivial datasets
            if len(data) > 2:
                benchmark_methods(data)

        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
