from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort(self):
        in_degree = [0] * self.V
        for i in self.graph:
            for j in self.graph[i]:
                in_degree[j] += 1

        queue = deque()
        for i in range(self.V):
            if in_degree[i] == 0:
                queue.append(i)

        top_order = []
        while queue:
            u = queue.popleft()
            top_order.append(u)

            for i in self.graph[u]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)

        if len(top_order) != self.V:
            print("There exists a cycle in the graph")
            return None
        else:
            return top_order

# Example usage:
if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    print("Topological Sort of the following graph")
    top_order = g.topological_sort()
    if top_order:
        print(top_order)
