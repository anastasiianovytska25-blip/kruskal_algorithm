import random
from .graph import Graph

def generate_random_connected(n, density):
    g = Graph(n)
    max_edges = n * (n-1) / 2
    edges = max(int(max_edges * density), n-1)

    used = set() # Множина для перевірки того що ребра не повторюються

    # Обєднання вершин для звʼязного графу при будь-якій щільності
    for i in range(n-1):
        w = random.randint(1, 120) # Зваженість
        g.add_edge(i, i+1, w)
        used.add((i, i+1))

    edges_added = n-1

    # Додавання випадкових ребер до потрібної щільності
    while edges_added < edges:
        u, v = random.randint(0, n-1), random.randint(0, n-1)
        if u == v or (u,v) in used or (v,u) in used:
            continue
        w = random.randint(1, 120)  # Зваженість
        g.add_edge(u, v, w)
        used.add((u,v))
        edges_added += 1

    return g