class Graph:
    def __init__(self, n):
        self.n = n
        self.matrix = [[0] * n for i in range(n)]
        self.list = [[] for i in range(n)]
        self.edges = []

    def add_edge(self, u, v, w):
        if u == v:
            return
        self.matrix[u][v] = w
        self.matrix[v][u] = w
        self.list[u].append((v, w))
        self.list[v].append((u, w))
        self.edges.append((w, u, v))
