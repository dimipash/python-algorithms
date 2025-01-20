from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
        
    def add_edge(self, u, v):
        self.graph[u].append(v)
        
    def scc(self):
        disc = [-1] * self.V
        low = [-1] * self.V
        stack_member = [False] * self.V
        st = []
        time = 0
        result = []
        
        def scc_util(u):
            nonlocal time
            disc[u] = low[u] = time
            time += 1
            st.append(u)
            stack_member[u] = True
            
            for v in self.graph[u]:
                if disc[v] == -1:
                    scc_util(v)
                    low[u] = min(low[u], low[v])
                elif stack_member[v]:
                    low[u] = min(low[u], disc[v])
                    
            w = -1
            if low[u] == disc[u]:
                component = []
                while w != u:
                    w = st.pop()
                    component.append(w)
                    stack_member[w] = False
                result.append(component)
                
        for i in range(self.V):
            if disc[i] == -1:
                scc_util(i)
                
        return result

# Example usage:
if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(0, 3)
    g.add_edge(3, 4)
    
    print("Strongly Connected Components:")
    sccs = g.scc()
    for component in sccs:
        print(component)
