from collections import deque
from typing import Dict, List, Set, Optional
import matplotlib.pyplot as plt
import networkx as nx


class BreadthFirstSearch:
    """
    Implementation of Breadth-First Search algorithm.

    Time Complexity: O(V + E) where V is vertices and E is edges
    Space Complexity: O(V) for queue and visited set

    Example:
        >>> graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
        >>> bfs = BreadthFirstSearch()
        >>> path = bfs.find_path(graph, 'A', 'D')
    """

    def traverse(self, graph: Dict[str, List[str]], start: str) -> List[str]:
        """
        Traverse graph using BFS and return visit order

        Args:
            graph: Adjacency list representation of graph
            start: Starting vertex

        Returns:
            List of vertices in order of visitation
        """
        visited = set()
        queue = deque([start])
        visit_order = []

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                visit_order.append(vertex)

                # Add unvisited neighbors to queue
                queue.extend(
                    neighbor for neighbor in graph[vertex] if neighbor not in visited
                )

        return visit_order

    def find_path(
        self, graph: Dict[str, List[str]], start: str, end: str
    ) -> Optional[List[str]]:
        """
        Find shortest path between start and end vertices

        Args:
            graph: Adjacency list representation of graph
            start: Starting vertex
            end: Target vertex

        Returns:
            List representing path from start to end, or None if no path exists
        """
        if start not in graph or end not in graph:
            return None

        visited = {start}
        queue = deque([(start, [start])])

        while queue:
            vertex, path = queue.popleft()

            for neighbor in graph[vertex]:
                if neighbor == end:
                    return path + [neighbor]

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        return None

    def find_levels(self, graph: Dict[str, List[str]], start: str) -> Dict[str, int]:
        """
        Find levels/distances of all vertices from start

        Args:
            graph: Adjacency list representation of graph
            start: Starting vertex

        Returns:
            Dictionary mapping vertices to their levels
        """
        levels = {start: 0}
        visited = {start}
        queue = deque([start])

        while queue:
            vertex = queue.popleft()

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    levels[neighbor] = levels[vertex] + 1
                    queue.append(neighbor)

        return levels

    def visualize_graph(
        self, graph: Dict[str, List[str]], path: Optional[List[str]] = None
    ) -> None:
        """Visualize graph and optionally highlight a path"""
        G = nx.Graph(graph)
        pos = nx.spring_layout(G)

        plt.figure(figsize=(10, 8))

        # Draw graph
        nx.draw_networkx_nodes(G, pos, node_color="lightblue", node_size=500)
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edges(G, pos)

        # Highlight path if provided
        if path:
            path_edges = list(zip(path[:-1], path[1:]))
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="r", width=2)
            nx.draw_networkx_nodes(
                G, pos, nodelist=path, node_color="lightgreen", node_size=500
            )

        plt.title("Graph Visualization")
        plt.axis("off")
        plt.show()


if __name__ == "__main__":
    # Example usage
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }

    bfs = BreadthFirstSearch()

    # Traverse graph
    visit_order = bfs.traverse(graph, "A")
    print(f"Visit order: {' -> '.join(visit_order)}")

    # Find path
    path = bfs.find_path(graph, "A", "F")
    if path:
        print(f"Path from A to F: {' -> '.join(path)}")

    # Find levels
    levels = bfs.find_levels(graph, "A")
    print("\nLevels from A:")
    for vertex, level in levels.items():
        print(f"{vertex}: {level}")

    # Visualize
    bfs.visualize_graph(graph, path)
