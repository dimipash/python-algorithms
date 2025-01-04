from typing import Callable, Tuple
import random
import math


class HillClimbing:
    """
    Implements Hill Climbing optimization algorithm.
    Finds local maximum of objective function through iterative improvement.
    """

    def __init__(
        self,
        objective_function: Callable[[float], float],
        step_size: float = 0.1,
        max_iterations: int = 1000,
        tolerance: float = 1e-6,
    ):
        """
        Args:
            objective_function: Function to optimize
            step_size: Size of steps in each iteration
            max_iterations: Maximum number of iterations
            tolerance: Minimum improvement required to continue
        """
        self.objective = objective_function
        self.step_size = step_size
        self.max_iterations = max_iterations
        self.tolerance = tolerance

    def optimize(self, start: float) -> Tuple[float, float]:
        """
        Performs hill climbing optimization.

        Args:
            start: Initial solution

        Returns:
            Tuple of (optimal_solution, optimal_value)
        """
        current = start
        current_value = self.objective(current)

        for iteration in range(self.max_iterations):
            # Generate and evaluate neighbors
            neighbors = [current + self.step_size, current - self.step_size]

            # Find best neighbor
            next_solution = max(neighbors, key=self.objective)
            next_value = self.objective(next_solution)

            # Check for improvement
            improvement = next_value - current_value
            if improvement <= self.tolerance:
                break

            current = next_solution
            current_value = next_value

        return current, current_value

    @staticmethod
    def example_objective(x: float) -> float:
        """Example objective function: f(x) = -(x-3)^2 + 9"""
        return -1 * (x - 3) ** 2 + 9


def main():
    # Test cases with different objective functions
    test_cases = [
        (HillClimbing.example_objective, (0, 6), "Parabola"),
        (lambda x: math.sin(x), (0, 2 * math.pi), "Sine wave"),
        (lambda x: -(x**2), (-5, 5), "Negative quadratic"),
    ]

    for objective, (min_val, max_val), case_type in test_cases:
        # Initialize optimizer
        optimizer = HillClimbing(
            objective_function=objective, step_size=0.1, max_iterations=1000
        )

        # Try multiple random starts
        best_solution = None
        best_value = float("-inf")

        for _ in range(5):
            start = random.uniform(min_val, max_val)
            solution, value = optimizer.optimize(start)

            if value > best_value:
                best_solution = solution
                best_value = value

        print(f"\nCase: {case_type}")
        print(f"Best solution: {best_solution:.6f}")
        print(f"Best value: {best_value:.6f}")


if __name__ == "__main__":
    main()
