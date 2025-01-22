from typing import Union, List
import math
import time


class AbsoluteValue:
    """
    Demonstrates and implements absolute value calculations for different numeric types.
    The absolute value is the non-negative value of a number without regard to its sign.

    Time Complexity: O(1) for all operations
    Space Complexity: O(1) for all operations
    """

    @staticmethod
    def abs_integer(x: int) -> int:
        """
        Calculates absolute value of an integer.
        Returns the magnitude without the sign.
        """
        return x if x >= 0 else -x

    @staticmethod
    def abs_float(x: float) -> float:
        """
        Calculates absolute value of a float.
        Returns the positive magnitude.
        """
        return float(abs(x))

    @staticmethod
    def abs_complex(x: complex) -> float:
        """
        Calculates absolute value (magnitude) of a complex number.
        Returns sqrt(real² + imaginary²)
        """
        return math.sqrt(x.real**2 + x.imag**2)

    @staticmethod
    def abs_generic(x: Union[int, float, complex]) -> Union[int, float]:
        """
        Generic absolute value function handling multiple numeric types.
        """
        if isinstance(x, complex):
            return AbsoluteValue.abs_complex(x)
        elif isinstance(x, float):
            return AbsoluteValue.abs_float(x)
        elif isinstance(x, int):
            return AbsoluteValue.abs_integer(x)
        else:
            raise TypeError(f"Unsupported type: {type(x)}")


def benchmark_abs(
    value: Union[int, float, complex], iterations: int = 1000000
) -> float:
    """Measures performance of absolute value calculation."""
    start = time.perf_counter()
    for _ in range(iterations):
        abs(value)
    return (time.perf_counter() - start) / iterations


def main():
    abs_calculator = AbsoluteValue()

    # Test cases for different numeric types
    test_cases = [
        # Integers
        -42,
        0,
        100,
        # Floats
        -3.14159,
        0.0,
        2.71828,
        # Complex Numbers
        3 + 4j,
        1 - 1j,
        -2 + 0j,
    ]

    for value in test_cases:
        print(f"\nTesting absolute value of {value}")
        print(f"Type: {type(value)}")

        try:
            # Calculate using our implementation
            result = abs_calculator.abs_generic(value)
            print(f"Custom abs result: {result}")

            # Compare with built-in abs()
            builtin_result = abs(value)
            print(f"Built-in abs result: {builtin_result}")

            # Verify results match
            assert math.isclose(
                result, builtin_result, rel_tol=1e-9
            ), "Results don't match!"

            # Benchmark performance
            avg_time = benchmark_abs(value)
            print(f"Average time per operation: {avg_time:.9f} seconds")

        except Exception as e:
            print(f"Error: {e}")

        # Show mathematical properties
        if isinstance(value, (int, float)):
            print("\nMathematical properties:")
            print(f"1. |x| ≥ 0: {abs(value) >= 0}")
            print(f"2. |-x| = |x|: {abs(-value) == abs(value)}")
            print(f"3. |x²| = x²: {abs(value**2) == value**2}")


if __name__ == "__main__":
    main()
