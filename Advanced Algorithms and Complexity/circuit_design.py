# python3

import sys
import threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


def post_order(i, graph, visited, post):
    global clock
    visited[i] = True
    for v in graph[i]:
        if not visited[v]:
            post_order(v, graph, visited, post)
    post[i] = clock
    clock += 1


def dfs(n, graph):
    global clock
    visited = [False] * (2 * n + 1)
    post = [0] * (2 * n + 1)
    for v in range(1, 2 * n + 1):
        if not visited[v]:
            post_order(v, graph, visited, post)
    post = list(enumerate(post[1:], start=1))
    post.sort(key=lambda x:x[1], reverse=True)
    post_vertex = []
    for v, order in post:
        post_vertex.append(v)
    return post_vertex


def explore(i, graph, visited, scc, scc_number, u):
    visited[i] = True
    scc.append(i)
    scc_number[i] = u
    for v in graph[i]:
        if not visited[v]:
            explore(v, graph, visited, scc, scc_number, u)

def find_sccs(n, rev_graph, graph):
    global clock
    post_vertex = dfs(n, rev_graph)
    visited = [False] * (2 * n + 1)
    sccs = []
    scc_number = [0] * (2 * n + 1)
    u = 1
    for i in post_vertex:
        if not visited[i]:
            scc = []
            explore(i, graph, visited, scc, scc_number, u)
            sccs.append(scc)
            u += 1
    return sccs, scc_number


def two_sat(n, rev_graph, graph):
    sccs, scc_number = find_sccs(n, rev_graph, graph)
    
    for i in range(1, n + 1):
        if scc_number[i] == scc_number[i + n]:
            return False
    solution = [[] for _ in range(2 * n + 1)]
    assigned = [False] * (2 * n + 1)
    for scc in sccs:
        for v in scc:
            if not assigned[v]:
                assigned[v] = True
                solution[v] = 1
                if v > n:
                    solution[v - n] = 0
                    assigned[v - n] = True
                else:
                    solution[v + n] = 0
                    assigned[v + n] = True
    return solution


clock = 1
def main():
    n, m = map(int, input().split())
    edges = [[] for _ in range(2 * n + 1)]
    rev_edges = [[] for _ in range(2 * n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        if a > 0 and b > 0:
            edges[a + n].append(b)
            edges[b + n].append(a)
            rev_edges[b].append(a + n)
            rev_edges[a].append(b + n)
        elif a < 0 and b < 0:
            edges[-a].append(-b + n)
            edges[-b].append(-a + n)
            rev_edges[-b + n].append(-a)
            rev_edges[-a + n].append(-b)
        elif a < 0 and b > 0 :
            edges[-a].append(b)
            edges[b + n].append(-a + n)
            rev_edges[b].append(-a)
            rev_edges[-a + n].append(b + n)
        elif a > 0 and b < 0:
            edges[a + n].append(-b + n)
            edges[-b].append(a)
            rev_edges[-b + n].append(a + n)
            rev_edges[a].append(-b)
   
    result = two_sat(n, rev_edges, edges)
    if not result:
        print('UNSATISFIABLE')
    else:
        print('SATISFIABLE')
        for i in range(1, n + 1):
            if result[i] > 0:
                print(i, end=' ')
            else:
                print(-i, end=' ')


threading.Thread(target=main).start()