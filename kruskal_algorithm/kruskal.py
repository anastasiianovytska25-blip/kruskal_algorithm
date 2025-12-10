from .dsu import DSU

def kruskal(g):
    dsu = DSU(g.n)
    mst = []
    total_weight = 0
    for w, u, v in sorted(g.edges):
        if dsu.union(u, v):
            mst.append((u, v, w))
            total_weight += w
    return mst, total_weight

# Через матриці
def kruskal_from_matrix(graph):
    dsu = DSU(graph.n)
    mst = []
    total_weight = 0
    edges = []
    for u in range(graph.n):
        for v in range(u + 1, graph.n):
            if graph.matrix[u][v] != 0:
                edges.append((graph.matrix[u][v], u, v))
    for w, u, v in sorted(edges):
        if dsu.union(u, v):
            mst.append((u, v, w))
            total_weight += w
    return mst, total_weight

# Через списки
def kruskal_from_list(graph):
    dsu = DSU(graph.n)
    mst = []
    total_weight = 0
    edges = []
    for u in range(graph.n):
        for v, w in graph.list[u]:
            if u < v:
                edges.append((w, u, v))
    for w, u, v in sorted(edges):
        if dsu.union(u, v):
            mst.append((u, v, w))
            total_weight += w
    return mst, total_weight