from collections import deque
from typing import Dict, List, Set, Optional
import matplotlib.pyplot as plt
import networkx as nx


class BipartiteChecker:
    """
    Implementation of bipartite graph checker using BFS.

    Time Complexity: O(V + E) where V is vertices and E is edges
    Space Complexity: O(V) for color mapping and queue

    Example:
        >>> graph = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}
        >>> checker = BipartiteChecker()
        >>> is_bipartite = checker.check_bipartite(graph)
    """

    def check_bipartite(
        self, graph: Dict[int, List[int]], start: Optional[int] = None
    ) -> bool:
        """
        Check if graph is bipartite using BFS coloring

        Args:
            graph: Adjacency list representation of graph
            start: Starting vertex (optional)

        Returns:
            True if graph is bipartite, False otherwise
        """
        if not graph:
            return True

        # Initialize coloring
        colors = {}

        # Handle disconnected components
        for vertex in graph:
            if vertex not in colors:
                if not self._bfs_color(graph, vertex, colors):
                    return False

        return True

    def _bfs_color(
        self, graph: Dict[int, List[int]], start: int, colors: Dict[int, int]
    ) -> bool:
        """Helper method to color graph using BFS"""
        queue = deque([start])
        colors[start] = 0  # Start with color 0

        while queue:
            vertex = queue.popleft()
            current_color = colors[vertex]

            # Check all neighbors
            for neighbor in graph[vertex]:
                if neighbor not in colors:
                    # Color neighbor with opposite color
                    colors[neighbor] = 1 - current_color
                    queue.append(neighbor)
                elif colors[neighbor] == current_color:
                    # Adjacent vertices have same color
                    return False

        return True

    def get_partitions(self, graph: Dict[int, List[int]]) -> Optional[tuple]:
        """
        Get the two partitions if graph is bipartite

        Returns:
            Tuple of (set0, set1) representing partitions, or None if not bipartite
        """
        colors = {}

        # Color the graph
        for vertex in graph:
            if vertex not in colors:
                if not self._bfs_color(graph, vertex, colors):
                    return None

        # Separate vertices by color
        set0 = {v for v, c in colors.items() if c == 0}
        set1 = {v for v, c in colors.items() if c == 1}

        return (set0, set1)

    def visualize_graph(
        self, graph: Dict[int, List[int]], partitions: Optional[tuple] = None
    ) -> None:
        """Visualize graph with optional partition coloring"""
        G = nx.Graph(graph)
        pos = nx.spring_layout(G)

        plt.figure(figsize=(10, 8))

        if partitions:
            set0, set1 = partitions
            # Draw nodes with partition colors
            nx.draw_networkx_nodes(
                G, pos, nodelist=list(set0), node_color="lightblue", node_size=500
            )
            nx.draw_networkx_nodes(
                G, pos, nodelist=list(set1), node_color="lightgreen", node_size=500
            )
        else:
            nx.draw_networkx_nodes(G, pos, node_color="lightgray", node_size=500)

        nx.draw_networkx_edges(G, pos)
        nx.draw_networkx_labels(G, pos)

        plt.title("Bipartite Graph Visualization")
        plt.axis("off")
        plt.show()


if __name__ == "__main__":
    # Example usage
    graph = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}

    checker = BipartiteChecker()

    # Check if graph is bipartite
    is_bipartite = checker.check_bipartite(graph)
    print(f"Is graph bipartite? {is_bipartite}")

    # Get partitions
    partitions = checker.get_partitions(graph)
    if partitions:
        set0, set1 = partitions
        print(f"\nPartitions:")
        print(f"Set 0: {set0}")
        print(f"Set 1: {set1}")

    # Visualize
    checker.visualize_graph(graph, partitions)

    # Non-bipartite example
    non_bipartite = {0: [1, 2], 1: [0, 2], 2: [0, 1]}

    print(f"\nIs triangle graph bipartite? {checker.check_bipartite(non_bipartite)}")
