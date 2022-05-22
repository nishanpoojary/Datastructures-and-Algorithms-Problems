# python3

from collections import deque

def BFS(n_vertices, adj_list, start, stop):
    dist = [float('inf')] * (n_vertices+1)
    queue = deque()
    queue.append(start)
    dist[start] = 0
    
    while queue:
        current = queue.popleft()
        for vertex in adj_list[current]:
            if dist[vertex] == float('inf'):
                queue.append(vertex)
                dist[vertex] = dist[current] + 1
    
    return dist[stop]
    
if __name__ == '__main__':
    n_vertices, n_edges = map(int, input().split())
    
    adjacency_list = [[] for _ in range(n_vertices+1)]
    
    for _ in range(n_edges):
        a, b = map(int, input().split())
        adjacency_list[a].append(b)
        adjacency_list[b].append(a)
    
    u, v = map(int, input().split())
    
    distance = BFS(n_vertices, adjacency_list, u, v)
    
    if distance == float('inf'):
        print(-1)
    else:
        print(distance)
    