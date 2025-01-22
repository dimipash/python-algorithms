from typing import Dict, List, Set, Optional
import matplotlib.pyplot as plt
import networkx as nx


class CycleDetector:
    """
    Implementation of cycle detection algorithms for graphs.

    Time Complexity: O(V + E) where V is vertices and E is edges
    Space Complexity: O(V) for recursion stack and visited set

    Example:
        >>> graph = {0: [1], 1: [2], 2: [3], 3: [1]}
        >>> detector = CycleDetector()
        >>> has_cycle = detector.check_cycle(graph)
    """

    def check_cycle(self, graph: Dict[int, List[int]], directed: bool = False) -> bool:
        """
        Check if graph contains a cycle

        Args:
            graph: Adjacency list representation of graph
            directed: True if graph is directed, False otherwise

        Returns:
            True if cycle exists, False otherwise
        """
        visited = set()
        rec_stack = set()  # For directed graph cycle detection

        def dfs_undirected(vertex: int, parent: int) -> bool:
            """DFS helper for undirected graphs"""
            visited.add(vertex)

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    if dfs_undirected(neighbor, vertex):
                        return True
                elif neighbor != parent:
                    # Back edge found
                    return True

            return False

        def dfs_directed(vertex: int) -> bool:
            """DFS helper for directed graphs"""
            visited.add(vertex)
            rec_stack.add(vertex)

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    if dfs_directed(neighbor):
                        return True
                elif neighbor in rec_stack:
                    # Back edge found in current recursion stack
                    return True

            rec_stack.remove(vertex)
            return False

        # Check all vertices to handle disconnected components
        for vertex in graph:
            if vertex not in visited:
                if directed:
                    if dfs_directed(vertex):
                        return True
                else:
                    if dfs_undirected(vertex, -1):
                        return True

        return False

    def find_cycle(
        self, graph: Dict[int, List[int]], directed: bool = False
    ) -> Optional[List[int]]:
        """
        Find and return a cycle if one exists

        Returns:
            List of vertices forming cycle, or None if no cycle exists
        """
        visited = set()
        parent = {}
        rec_stack = set()

        def find_cycle_path(start: int, end: int) -> List[int]:
            """Helper to reconstruct cycle path"""
            path = [end]
            current = start

            while current != end:
                path.append(current)
                current = parent[current]

            path.append(end)
            return path[::-1]

        def dfs_undirected(vertex: int, prev: int) -> Optional[List[int]]:
            """DFS helper for undirected graphs"""
            visited.add(vertex)
            parent[vertex] = prev

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    cycle = dfs_undirected(neighbor, vertex)
                    if cycle:
                        return cycle
                elif neighbor != prev:
                    return find_cycle_path(vertex, neighbor)

            return None

        def dfs_directed(vertex: int) -> Optional[List[int]]:
            """DFS helper for directed graphs"""
            visited.add(vertex)
            rec_stack.add(vertex)

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    parent[neighbor] = vertex
                    cycle = dfs_directed(neighbor)
                    if cycle:
                        return cycle
                elif neighbor in rec_stack:
                    parent[neighbor] = vertex
                    return find_cycle_path(neighbor, neighbor)

            rec_stack.remove(vertex)
            return None

        # Check all vertices
        for vertex in graph:
            if vertex not in visited:
                cycle = dfs_directed(vertex) if directed else dfs_undirected(vertex, -1)
                if cycle:
                    return cycle

        return None

    def visualize_graph(
        self,
        graph: Dict[int, List[int]],
        cycle: Optional[List[int]] = None,
        directed: bool = False,
    ) -> None:
        """Visualize graph with optional cycle highlighting"""
        G = nx.DiGraph(graph) if directed else nx.Graph(graph)
        pos = nx.spring_layout(G)

        plt.figure(figsize=(10, 8))

        # Draw nodes
        nx.draw_networkx_nodes(G, pos, node_color="lightblue", node_size=500)

        # Draw edges
        if cycle:
            # Create cycle edges
            cycle_edges = list(zip(cycle[:-1], cycle[1:]))
            if not directed:
                cycle_edges.append((cycle[-1], cycle[0]))

            # Draw non-cycle edges
            other_edges = [
                (u, v) for u in graph for v in graph[u] if (u, v) not in cycle_edges
            ]

            nx.draw_networkx_edges(G, pos, edgelist=other_edges, arrows=directed)
            nx.draw_networkx_edges(
                G, pos, edgelist=cycle_edges, edge_color="r", width=2, arrows=directed
            )
        else:
            nx.draw_networkx_edges(G, pos, arrows=directed)

        nx.draw_networkx_labels(G, pos)

        plt.title("Graph Cycle Visualization")
        plt.axis("off")
        plt.show()


if __name__ == "__main__":
    # Example usage
    graph = {0: [1], 1: [2], 2: [3], 3: [4], 4: [1]}  # Creates cycle 1->2->3->4->1

    detector = CycleDetector()

    # Check for cycle
    has_cycle = detector.check_cycle(graph, directed=True)
    print(f"Has cycle: {has_cycle}")

    # Find cycle
    cycle = detector.find_cycle(graph, directed=True)
    if cycle:
        print(f"Found cycle: {' -> '.join(map(str, cycle))}")

    # Visualize
    detector.visualize_graph(graph, cycle, directed=True)

    # Undirected example
    undirected_graph = {0: [1, 2], 1: [0, 2], 2: [0, 1], 3: [4], 4: [3]}

    cycle = detector.find_cycle(undirected_graph)
    print(f"\nUndirected cycle: {cycle}")
    detector.visualize_graph(undirected_graph, cycle)
