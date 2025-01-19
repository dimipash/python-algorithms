from typing import Dict, List, Set
import matplotlib.pyplot as plt
import networkx as nx


class ConnectedComponentsFinder:
    """
    Implementation of connected components detection using DFS.

    Time Complexity: O(V + E) where V is vertices and E is edges
    Space Complexity: O(V) for visited set and recursion stack

    Example:
        >>> graph = {0: [1], 1: [0, 2], 2: [1], 3: [4], 4: [3]}
        >>> finder = ConnectedComponentsFinder()
        >>> components = finder.find_components(graph)
    """

    def find_components(self, graph: Dict[int, List[int]]) -> List[List[int]]:
        """
        Find all connected components in undirected graph

        Args:
            graph: Adjacency list representation of graph

        Returns:
            List of components where each component is a list of vertices
        """
        visited = set()
        components = []

        def dfs(vertex: int, component: List[int]) -> None:
            """DFS helper to explore component"""
            visited.add(vertex)
            component.append(vertex)

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    dfs(neighbor, component)

        # Find components for all unvisited vertices
        for vertex in graph:
            if vertex not in visited:
                component = []
                dfs(vertex, component)
                components.append(component)

        return components

    def get_component_sizes(self, components: List[List[int]]) -> List[int]:
        """Get sizes of all components"""
        return [len(component) for component in components]

    def get_largest_component(self, components: List[List[int]]) -> List[int]:
        """Get the largest connected component"""
        return max(components, key=len) if components else []

    def visualize_components(
        self, graph: Dict[int, List[int]], components: List[List[int]]
    ) -> None:
        """Visualize graph with colored components"""
        G = nx.Graph(graph)
        pos = nx.spring_layout(G)

        plt.figure(figsize=(10, 8))

        # Generate colors for components
        colors = plt.cm.rainbow(np.linspace(0, 1, len(components)))

        # Draw each component with different color
        for component, color in zip(components, colors):
            nx.draw_networkx_nodes(
                G, pos, nodelist=component, node_color=[color], node_size=500
            )

        nx.draw_networkx_edges(G, pos)
        nx.draw_networkx_labels(G, pos)

        plt.title("Connected Components Visualization")
        plt.axis("off")
        plt.show()


if __name__ == "__main__":
    # Example usage
    graph = {0: [1], 1: [0, 2], 2: [1], 3: [4], 4: [3, 5], 5: [4]}

    finder = ConnectedComponentsFinder()

    # Find components
    components = finder.find_components(graph)
    print(f"Connected Components: {components}")

    # Get component sizes
    sizes = finder.get_component_sizes(components)
    print(f"Component sizes: {sizes}")

    # Get largest component
    largest = finder.get_largest_component(components)
    print(f"Largest component: {largest}")

    # Visualize
    finder.visualize_components(graph, components)
