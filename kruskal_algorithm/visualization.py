import matplotlib.pyplot as plt
import networkx as nx

def draw_graph_from_adj_list(graph):
    """Малює граф зі списків суміжності"""
    G = nx.Graph()
    for u in range(graph.n):
        for v, w in graph.list[u]:
            if u < v:  # щоб не дублювати ребра
                G.add_edge(u+1, v+1, weight=w)
    _draw_nx_graph(G)

def draw_graph_from_matrix(graph):
    """Малює граф з матриці суміжності"""
    G = nx.Graph()
    for u in range(graph.n):
        for v in range(u, graph.n):
            w = graph.matrix[u][v]
            if w != 0:
                G.add_edge(u+1, v+1, weight=w)
    _draw_nx_graph(G)

def _draw_nx_graph(G):
    """Внутрішня допоміжна функція для малювання networkx"""
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()