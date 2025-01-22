class AntColonyOptimizer:
    """
    Implementation of Ant Colony Optimization algorithm for solving TSP.

    Time Complexity: O(iterations * num_ants * n^2), where n is number of cities
    Space Complexity: O(n^2) for pheromone matrix

    Example:
        >>> distances = [[0, 2, 9, 10], [1, 0, 6, 4], [15, 7, 0, 8], [6, 3, 12, 0]]
        >>> aco = AntColonyOptimizer(distances, num_ants=5)
        >>> best_tour, best_length = aco.solve()
    """

    def __init__(
        self,
        distances: list,
        num_ants: int = 5,
        num_iterations: int = 100,
        alpha: float = 1.0,
        beta: float = 2.0,
        evaporation_rate: float = 0.5,
        pheromone_constant: float = 100,
    ):
        self.distances = distances
        self.num_cities = len(distances)
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.alpha = alpha  # Pheromone importance
        self.beta = beta  # Distance importance
        self.evaporation_rate = evaporation_rate
        self.pheromone_constant = pheromone_constant

        # Initialize pheromone matrix
        self.pheromones = [
            [1.0 for _ in range(self.num_cities)] for _ in range(self.num_cities)
        ]

    def _select_next_city(self, current_city: int, unvisited: list) -> int:
        """Select next city using probability based on pheromone and distance"""
        probabilities = []
        total = 0

        # Calculate probabilities for each unvisited city
        for city in unvisited:
            pheromone = self.pheromones[current_city][city] ** self.alpha
            distance = (1.0 / self.distances[current_city][city]) ** self.beta
            probability = pheromone * distance
            probabilities.append(probability)
            total += probability

        # Normalize probabilities
        probabilities = [p / total for p in probabilities]

        # Select city using roulette wheel selection
        r = random.random()
        for i, prob in enumerate(probabilities):
            r -= prob
            if r <= 0:
                return unvisited[i]
        return unvisited[-1]

    def _construct_solution(self) -> tuple:
        """Construct a single ant's solution"""
        start = random.randint(0, self.num_cities - 1)
        tour = [start]
        unvisited = list(set(range(self.num_cities)) - {start})

        while unvisited:
            next_city = self._select_next_city(tour[-1], unvisited)
            tour.append(next_city)
            unvisited.remove(next_city)

        return tour, self._calculate_tour_length(tour)

    def _calculate_tour_length(self, tour: list) -> float:
        """Calculate total tour length"""
        return (
            sum(self.distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
            + self.distances[tour[-1]][tour[0]]
        )

    def _update_pheromones(self, all_tours: list):
        """Update pheromone levels on all edges"""
        # Evaporation
        for i in range(self.num_cities):
            for j in range(self.num_cities):
                self.pheromones[i][j] *= 1 - self.evaporation_rate

        # Add new pheromones
        for tour, length in all_tours:
            pheromone_amount = self.pheromone_constant / length
            for i in range(len(tour) - 1):
                self.pheromones[tour[i]][tour[i + 1]] += pheromone_amount
            self.pheromones[tour[-1]][tour[0]] += pheromone_amount

    def solve(self) -> tuple:
        """
        Execute ACO algorithm to find best tour

        Returns:
            Tuple of (best_tour, best_length)
        """
        best_tour = None
        best_length = float("inf")

        for _ in range(self.num_iterations):
            # Construct solutions for all ants
            all_tours = [self._construct_solution() for _ in range(self.num_ants)]

            # Update best solution
            for tour, length in all_tours:
                if length < best_length:
                    best_tour = tour
                    best_length = length

            # Update pheromone trails
            self._update_pheromones(all_tours)

        return best_tour, best_length


if __name__ == "__main__":
    # Example usage
    distances = [[0, 2, 9, 10], [1, 0, 6, 4], [15, 7, 0, 8], [6, 3, 12, 0]]

    aco = AntColonyOptimizer(
        distances=distances,
        num_ants=5,
        num_iterations=100,
        alpha=1.0,
        beta=2.0,
        evaporation_rate=0.5,
        pheromone_constant=100,
    )

    best_tour, best_length = aco.solve()
    print(f"Best tour: {best_tour}")
    print(f"Tour length: {best_length}")
