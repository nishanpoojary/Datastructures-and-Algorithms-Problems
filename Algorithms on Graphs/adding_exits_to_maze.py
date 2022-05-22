def explore(adj_list, vis, x):
    visited[x] = True
    for vertex in adj_list[x]:
        if not visited[vertex]:
            explore(adj_list, vis, vertex)
            
def number_of_components(n_vertices, adj_list, vis):
    n_cc = 0
    
    for i in range(1, n_vertices + 1):
         if not visited[i]:
            explore(adj_list, vis, i)
            n_cc += 1
    
    return n_cc
    

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
    
    print(number_of_components(n_vertices, adjacency_list, visited))
    