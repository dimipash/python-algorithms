from typing import List, Tuple
import random


class TabuSearch:
    """
    Implements Tabu Search optimization algorithm.
    Uses memory structures to escape local optima.
    """

    def __init__(self, max_iterations: int = 1000, tabu_tenure: int = 5):
        """
        Args:
            max_iterations: Maximum number of search iterations
            tabu_tenure: Number of iterations a solution remains tabu
        """
        self.max_iterations = max_iterations
        self.tabu_tenure = tabu_tenure

    def objective_function(self, solution: List[float]) -> float:
        """Example objective function to minimize."""
        return sum(x**2 for x in solution)

    def generate_neighbor(self, solution: List[float]) -> List[float]:
        """Generates neighboring solution with small random modification."""
        neighbor = solution.copy()
        index = random.randint(0, len(solution) - 1)
        neighbor[index] += random.uniform(-1, 1)
        return neighbor

    def optimize(self, initial_solution: List[float]) -> Tuple[List[float], float]:
        """
        Performs tabu search optimization.

        Args:
            initial_solution: Starting solution

        Returns:
            Tuple of (best_solution, best_energy)
        """
        current = initial_solution
        best = current.copy()
        best_energy = self.objective_function(best)

        tabu_list = []
        tabu_counter = {}

        for _ in range(self.max_iterations):
            # Generate neighborhood excluding tabu solutions
            neighborhood = [self.generate_neighbor(current) for _ in range(100)]
            neighborhood = [s for s in neighborhood if s not in tabu_list]

            # Find best non-tabu neighbor
            best_neighbor = None
            best_neighbor_energy = float("inf")

            for neighbor in neighborhood:
                energy = self.objective_function(neighbor)
                if energy < best_neighbor_energy:
                    best_neighbor = neighbor
                    best_neighbor_energy = energy

            if best_neighbor is None:
                continue

            # Update current solution
            current = best_neighbor

            # Update tabu list
            tabu_list.append(best_neighbor)
            tabu_counter[tuple(best_neighbor)] = self.tabu_tenure

            # Remove expired tabu entries
            tabu_list = [
                sol
                for sol in tabu_list
                if tuple(sol) in tabu_counter and tabu_counter[tuple(sol)] > 0
            ]

            # Decrease tabu counters
            for key in list(tabu_counter.keys()):
                tabu_counter[key] -= 1

            # Update best solution
            if best_neighbor_energy < best_energy:
                best = best_neighbor
                best_energy = best_neighbor_energy

        return best, best_energy


def main():
    # Initialize optimizer
    optimizer = TabuSearch(max_iterations=1000, tabu_tenure=5)

    # Generate random initial solution
    initial_solution = [random.uniform(-10, 10) for _ in range(5)]

    # Run optimization
    best_solution, best_energy = optimizer.optimize(initial_solution)

    print(f"Initial solution: {initial_solution}")
    print(f"Best solution: {best_solution}")
    print(f"Best energy: {best_energy}")


if __name__ == "__main__":
    main()
