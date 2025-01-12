from typing import List, Union
import statistics
import time


class Mode:
    """
    Implements mode calculation for datasets.
    Mode is the value that appears most frequently in a dataset.

    Time Complexity: O(n) for counting frequencies
    Space Complexity: O(k) where k is number of unique values
    """

    @staticmethod
    def calculate(data: List[Union[int, float]]) -> Union[int, float, str]:
        """
        Calculates single mode using statistics module.
        Returns most frequent value or error message if no unique mode.
        """
        if not data:
            raise ValueError("Dataset cannot be empty")

        try:
            return statistics.mode(data)
        except statistics.StatisticsError:
            return "No unique mode found"

    @staticmethod
    def calculate_multimode(data: List[Union[int, float]]) -> List[Union[int, float]]:
        """
        Calculates all modes in dataset.
        Returns list of values that appear most frequently.
        """
        if not data:
            raise ValueError("Dataset cannot be empty")

        return statistics.multimode(data)

    @staticmethod
    def calculate_manual(data: List[Union[int, float]]) -> List[Union[int, float]]:
        """
        Calculates modes without using statistics module.

        Time Complexity: O(n)
        Space Complexity: O(k) where k is number of unique values
        """
        if not data:
            raise ValueError("Dataset cannot be empty")

        # Count frequencies
        freq = {}
        for value in data:
            freq[value] = freq.get(value, 0) + 1

        # Find maximum frequency
        max_freq = max(freq.values())

        # Return all values with maximum frequency
        return [value for value, count in freq.items() if count == max_freq]


def main():
    test_cases = [
        ([1, 2, 2, 3, 4, 4], "Multiple modes"),
        ([1, 1, 1, 2, 3], "Single mode"),
        ([1, 2, 3, 4, 5], "No mode"),
        ([1.5, 1.5, 2.5], "Float values"),
        ([1], "Single value"),
    ]

    calculator = Mode()

    for data, case_type in test_cases:
        print(f"\nTest case: {case_type}")
        print(f"Dataset: {data}")

        try:
            # Calculate modes
            single_mode = calculator.calculate(data)
            all_modes = calculator.calculate_multimode(data)
            manual_modes = calculator.calculate_manual(data)

            print(f"Single mode: {single_mode}")
            print(f"All modes: {all_modes}")
            print(f"Manual calculation: {manual_modes}")

            # Verify results match
            assert set(all_modes) == set(manual_modes), "Results don't match!"

        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
