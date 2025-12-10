import time
from kruskal_algorithm import *

def main():
    n = int(input("Введіть кількість вершин (n): "))
    density = float(input("Введіть щільність графа (від 0 до 1): "))
    # n = 120
    # density = 1
    g = generate_random_connected(n, density)
    # Візуалізація рандомно згенерованого графу
    print("\nПочатковий граф:")
    draw_graph_from_matrix(g)
    # print("Edges in adj list:", len(g_adj.edges))
    # Алгоритм через матрицю суміжності
    print("Матриця суміжності")
    start_matrix = time.time()
    mst_edges_matrix, total_w_matrix = kruskal_from_matrix(g)
    time_matrix = time.time() - start_matrix
    print(f"    Час виконання: {time_matrix:.6f} сек")
    print(f"    Вага MST: {total_w_matrix}")

    # Алгоритм черезсписки суміжності
    print("Списки суміжності")
    start_adj = time.time()
    mst_edges_adj, total_w_adj = kruskal_from_list(g)
    time_adj = time.time() - start_adj
    print(f"    Час виконання: {time_adj:.6f} сек")
    print(f"    Вага MST: {total_w_adj}")

    if time_matrix < time_adj:
        print(f"Матриця швидша у {time_adj / time_matrix:.2f} разів")
    else:
        print(f"Списки швидші у {time_matrix / time_adj:.2f} разів")

    # MST візуалізація
    print("\n  Minimum Spanning Tree(MST):")
    mst_graph = Graph(n)
    for u, v, w in mst_edges_matrix:
        mst_graph.add_edge(u, v, w)
    draw_graph_from_matrix(mst_graph)
if __name__ == "__main__":
    main()