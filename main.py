import time
from kruskal_algorithm import *

def main():
    density_range = [0.2, 0.4, 0.6, 0.8, 1]
    n_range = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]

    # відкриваємо файл на запис (кожен запуск перезаписує файл)
    with open("results.txt", "w", encoding="utf-8") as f:
        for n in n_range:
            f.write(f"\n===== n = {n} =====\n")
            print(f"\n===== n = {n} =====")   # щоб хоч щось бачити в консолі

            for density in density_range:
                for i in range(20):
                    f.write(f"\n--- Щільність = {density} ---\n")
                    print(f"--- Щільність = {density} ---")

                    g = generate_random_connected(n, density)

                    # Матриця суміжності
                    start_matrix = time.time()
                    mst_edges_matrix, total_w_matrix = kruskal_from_matrix(g)
                    time_matrix = time.time() - start_matrix

                    f.write("Матриця суміжності:\n")
                    f.write(f"    Час виконання: {time_matrix:.6f} сек\n")
                    f.write(f"    Вага MST: {total_w_matrix}\n")

                    # Списки суміжності
                    start_adj = time.time()
                    mst_edges_adj, total_w_adj = kruskal_from_list(g)
                    time_adj = time.time() - start_adj

                    f.write("Списки суміжності:\n")
                    f.write(f"    Час виконання: {time_adj:.6f} сек\n")
                    f.write(f"    Вага MST: {total_w_adj}\n")

                    # Порівняння швидкості
                    if time_matrix < time_adj:
                        faster = time_adj / time_matrix
                        f.write(f"Матриця швидша у {faster:.2f} разів\n")
                    else:
                        faster = time_matrix / time_adj
                        f.write(f"Списки швидші у {faster:.2f} разів\n")

        print("\nГотово! Результати записано у файл results.txt")

if __name__ == "__main__":
    main()