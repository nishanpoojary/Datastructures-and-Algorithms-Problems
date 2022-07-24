# python3

import sys
import threading

sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size

class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.children = []


def read_tree():
    size = int(input())
    tree = [Vertex(w) for w in map(int, input().split())]
    for i in range(1, size):
        a, b = list(map(int, input().split()))
        tree[a - 1].children.append(b - 1)
        tree[b - 1].children.append(a - 1)
    return tree


def dfs(tree, v, parent, D):
    if D[v] == - 1:
        if len(tree[v].children) == 1 and v != 0:
            D[v] = tree[v].weight
        else:
            m1 = tree[v].weight
            for u in tree[v].children:
                if u != parent:
                    for w in tree[u].children:
                        if w != v:
                            m1 += dfs(tree, w, u, D)
            m0 = 0
            for u in tree[v].children:
                if u != parent:
                    m0 += dfs(tree, u, v, D)
            D[v] = max(m0, m1)
    return D[v]


def max_weight_independent_tree_subset(tree):
    size = len(tree)
    if size == 0:
        return 0
    D = [-1] * size
    return dfs(tree, 0, -1, D)


def main():
    tree = read_tree()
    weight = max_weight_independent_tree_subset(tree)
    print(weight)


threading.Thread(target=main).start()