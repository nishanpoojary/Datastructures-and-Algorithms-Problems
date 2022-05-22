def explore(adj_list, vis, x, y):
    visited[x] = True
    for vertex in adj_list[x]:
        if not visited[vertex]:
            explore(adj_list, vis, vertex, y)

if __name__ == '__main__':
    n_vertices, n_edges = map(int, input().split())
    edges = []
    adjacency_list = [[] for _ in range(n_vertices + 1)]
    visited = [False]*(n_vertices + 1)
    
    for _ in range(n_edges):
        edges.append(tuple(map(int, input().split())))
        
    for (a,b) in edges:
        adjacency_list[a].append(b)
        adjacency_list[b].append(a)
    
    u, v = map(int, input().split())
    explore(adjacency_list, visited, u, v)
    
    if visited[v]:
        print(1)
    else:
        print(0)
    