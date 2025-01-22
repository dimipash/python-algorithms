from typing import Callable, Tuple
import math
import random
import time


class SimulatedAnnealing:
    """
    Implements Simulated Annealing optimization algorithm.
    Finds approximate global minimum through probabilistic search.
    """

    def __init__(
        self,
        objective_function: Callable[[float], float],
        neighbor_function: Callable[[float], float],
        initial_temp: float = 1000.0,
        cooling_rate: float = 0.95,
        min_temp: float = 1e-10,
    ):
        """
        Args:
            objective_function: Function to minimize
            neighbor_function: Function to generate neighbors
            initial_temp: Starting temperature
            cooling_rate: Rate of cooling
            min_temp: Minimum temperature for termination
        """
        self.objective = objective_function
        self.neighbor = neighbor_function
        self.initial_temp = initial_temp
        self.cooling_rate = cooling_rate
        self.min_temp = min_temp

    def optimize(self, initial_solution: float) -> Tuple[float, float]:
        """
        Performs simulated annealing optimization.

        Args:
            initial_solution: Starting point

        Returns:
            Tuple of (optimal_solution, optimal_energy)
        """
        current = initial_solution
        current_energy = self.objective(current)
        best = current
        best_energy = current_energy
        temp = self.initial_temp

        iterations = 0

        while temp > self.min_temp:
            iterations += 1

            # Generate neighbor
            new = self.neighbor(current)
            new_energy = self.objective(new)

            # Calculate energy change
            delta_e = new_energy - current_energy

            # Accept if better or probabilistically if worse
            if delta_e < 0 or random.random() < math.exp(-delta_e / temp):
                current = new
                current_energy = new_energy

                # Update best solution
                if current_energy < best_energy:
                    best = current
                    best_energy = current_energy

            # Cool system
            temp *= self.cooling_rate

        return best, best_energy, iterations


def main():
    # Test functions
    test_functions = [
        (lambda x: x**2, "Quadratic"),
        (lambda x: abs(x), "Absolute value"),
        (lambda x: math.sin(x) + x**2 / 20, "Sinusoidal"),
    ]

    # Neighbor generation function
    def random_neighbor(x: float, scale: float = 1.0) -> float:
        return x + random.uniform(-scale, scale)

    for objective, name in test_functions:
        print(f"\nOptimizing {name} function:")

        # Initialize optimizer
        optimizer = SimulatedAnnealing(
            objective_function=objective,
            neighbor_function=lambda x: random_neighbor(x),
            initial_temp=1000.0,
            cooling_rate=0.95,
        )

        # Try multiple starting points
        start_points = [-10.0, 0.0, 10.0]

        for start in start_points:
            start_time = time.perf_counter()
            solution, energy, iters = optimizer.optimize(start)
            duration = time.perf_counter() - start_time

            print(f"\nStarting point: {start}")
            print(f"Solution: {solution:.6f}")
            print(f"Energy: {energy:.6f}")
            print(f"Iterations: {iters}")
            print(f"Time: {duration:.6f} seconds")


if __name__ == "__main__":
    main()
