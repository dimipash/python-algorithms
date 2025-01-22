from typing import List, Generator
import time


class FizzBuzz:
    """
    Implements FizzBuzz problem with multiple approaches and optimizations.
    Rules:
    - Print numbers from 1 to n
    - For multiples of 3, print "Fizz"
    - For multiples of 5, print "Buzz"
    - For multiples of both 3 and 5, print "FizzBuzz"
    """

    @staticmethod
    def basic_approach(n: int) -> List[str]:
        """
        Basic implementation using modulo operations.

        Time Complexity: O(n)
        Space Complexity: O(n) for storing results
        """
        result = []
        for i in range(1, n + 1):
            if i % 15 == 0:  # Optimization: Check 15 first
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result

    @staticmethod
    def string_concatenation(n: int) -> List[str]:
        """
        Implementation using string concatenation.
        Avoids multiple modulo operations.
        """
        result = []
        for i in range(1, n + 1):
            output = ""
            if i % 3 == 0:
                output += "Fizz"
            if i % 5 == 0:
                output += "Buzz"
            result.append(output or str(i))
        return result

    @staticmethod
    def generator_approach(n: int) -> Generator[str, None, None]:
        """
        Memory-efficient generator implementation.
        Yields results one at a time.
        """
        for i in range(1, n + 1):
            if i % 15 == 0:
                yield "FizzBuzz"
            elif i % 3 == 0:
                yield "Fizz"
            elif i % 5 == 0:
                yield "Buzz"
            else:
                yield str(i)

    @staticmethod
    def pattern_matching(n: int) -> List[str]:
        """
        Pattern-based approach avoiding modulo operations.
        Uses cyclic pattern of length 15.
        """
        pattern = [
            "1",
            "2",
            "Fizz",
            "4",
            "Buzz",
            "Fizz",
            "7",
            "8",
            "Fizz",
            "Buzz",
            "11",
            "Fizz",
            "13",
            "14",
            "FizzBuzz",
        ]

        result = []
        for i in range(n):
            result.append(pattern[i % 15])
        return result[:n]


def benchmark_approaches(n: int) -> None:
    """Compares performance of different FizzBuzz implementations."""
    approaches = [
        ("Basic", FizzBuzz.basic_approach),
        ("String", FizzBuzz.string_concatenation),
        ("Pattern", FizzBuzz.pattern_matching),
    ]

    print("\nPerformance comparison:")
    for name, method in approaches:
        start = time.perf_counter()
        result = method(n)
        duration = time.perf_counter() - start
        print(f"{name:8}: {duration:.6f} seconds")


def main():
    test_cases = [15, 30, 100, 1000]

    for n in test_cases:
        print(f"\nTesting FizzBuzz up to {n}:")

        # Get results using basic approach
        results = FizzBuzz.basic_approach(n)

        # Print first and last few results
        print("First 5:", results[:5])
        if n > 10:
            print("Last 5:", results[-5:])

        # Count occurrences
        counts = {
            "Fizz": results.count("Fizz"),
            "Buzz": results.count("Buzz"),
            "FizzBuzz": results.count("FizzBuzz"),
        }
        print("\nCounts:", counts)

        # Benchmark different approaches
        benchmark_approaches(n)


if __name__ == "__main__":
    main()
