INF = float('inf')

def floyd_warshall(graph):
    n = len(graph)
    dist = [[0 if i == j else graph[i][j] if graph[i][j] != 0 else INF 
             for j in range(n)] 
            for i in range(n)]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    
    return dist

def print_solution(dist):
    n = len(dist)
    print("Following matrix shows the shortest distances between every pair of vertices")
    for i in range(n):
        for j in range(n):
            if dist[i][j] == INF:
                print("{:>7s}".format("INF"), end="")
            else:
                print("{:>7d}".format(dist[i][j]), end="")
        print()

# Example usage:
if __name__ == "__main__":
    graph = [
        [0, 5, INF, 10],
        [INF, 0, 3, INF],
        [INF, INF, 0, 1],
        [INF, INF, INF, 0]
    ]
    
    dist = floyd_warshall(graph)
    print_solution(dist)
