from typing import List, Tuple, Dict, Set, Optional
import heapq
import numpy as np
import matplotlib.pyplot as plt


class AStar:
    """
    A* pathfinding algorithm implementation.

    Time Complexity: O(E * log(V)) where E is number of edges, V is number of vertices
    Space Complexity: O(V) for storing visited nodes and path

    Example:
        >>> grid = np.array([
        ...     [0, 1, 0, 0],
        ...     [0, 0, 0, 1],
        ...     [1, 0, 0, 0]
        ... ])
        >>> pathfinder = AStar()
        >>> path = pathfinder.find_path(grid, (0,0), (2,3))
    """

    def __init__(self, diagonal: bool = False):
        """
        Args:
            diagonal: Allow diagonal movement if True
        """
        self.diagonal = diagonal
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        if diagonal:
            self.directions += [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    def manhattan_distance(self, a: Tuple[int, int], b: Tuple[int, int]) -> float:
        """Calculate Manhattan distance heuristic"""
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def euclidean_distance(self, a: Tuple[int, int], b: Tuple[int, int]) -> float:
        """Calculate Euclidean distance heuristic"""
        return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

    def get_neighbors(
        self, pos: Tuple[int, int], grid: np.ndarray
    ) -> List[Tuple[int, int]]:
        """Get valid neighboring positions"""
        neighbors = []
        rows, cols = grid.shape

        for dx, dy in self.directions:
            new_x, new_y = pos[0] + dx, pos[1] + dy
            if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x, new_y] == 0:
                neighbors.append((new_x, new_y))

        return neighbors

    def reconstruct_path(
        self, came_from: Dict, current: Tuple[int, int]
    ) -> List[Tuple[int, int]]:
        """Reconstruct path from came_from dictionary"""
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        return path[::-1]

    def find_path(
        self,
        grid: np.ndarray,
        start: Tuple[int, int],
        goal: Tuple[int, int],
        heuristic: str = "manhattan",
    ) -> Optional[List[Tuple[int, int]]]:
        """
        Find path using A* algorithm

        Args:
            grid: Binary grid where 0 is traversable, 1 is obstacle
            start: Starting position (row, col)
            goal: Goal position (row, col)
            heuristic: 'manhattan' or 'euclidean'

        Returns:
            List of positions forming the path, or None if no path exists
        """
        h = (
            self.manhattan_distance
            if heuristic == "manhattan"
            else self.euclidean_distance
        )

        open_set = []
        heapq.heappush(open_set, (0, start))

        came_from = {}
        g_score = {start: 0}
        f_score = {start: h(start, goal)}

        while open_set:
            current = heapq.heappop(open_set)[1]

            if current == goal:
                return self.reconstruct_path(came_from, current)

            for neighbor in self.get_neighbors(current, grid):
                # Cost is 1 for cardinal directions, sqrt(2) for diagonal
                move_cost = (
                    1
                    if abs(neighbor[0] - current[0]) + abs(neighbor[1] - current[1])
                    == 1
                    else 1.414
                )
                tentative_g = g_score[current] + move_cost

                if tentative_g < g_score.get(neighbor, float("inf")):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + h(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

        return None

    def visualize_path(
        self,
        grid: np.ndarray,
        path: List[Tuple[int, int]],
        start: Tuple[int, int],
        goal: Tuple[int, int],
    ) -> None:
        """Visualize the grid, obstacles, and found path"""
        plt.figure(figsize=(10, 10))
        plt.imshow(grid, cmap="binary")

        if path:
            path = np.array(path)
            plt.plot(path[:, 1], path[:, 0], "r-", linewidth=2, label="Path")

        plt.plot(start[1], start[0], "go", label="Start", markersize=15)
        plt.plot(goal[1], goal[0], "ro", label="Goal", markersize=15)

        plt.grid(True)
        plt.legend()
        plt.title("A* Pathfinding")
        plt.show()


if __name__ == "__main__":
    # Example usage
    grid = np.array(
        [
            [0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0],
        ]
    )

    start = (0, 0)
    goal = (4, 4)

    # Create pathfinder and find path
    pathfinder = AStar(diagonal=True)
    path = pathfinder.find_path(grid, start, goal)

    if path:
        print(f"Path found: {path}")
        pathfinder.visualize_path(grid, path, start, goal)
    else:
        print("No path found!")
