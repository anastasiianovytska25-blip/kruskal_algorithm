import time
from kruskal_algorithm import *

def main():
    density_range = [0.2, 0.4, 0.6, 0.8, 1]
    n_range = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]

    with open("results_all.txt", "w", encoding="utf-8") as f_all, \
         open("results_avg.txt", "w", encoding="utf-8") as f_avg:

        for n in n_range:
            f_all.write(f"\n===== n = {n} =====\n")
            f_avg.write(f"\n===== n = {n} =====\n")
            print(f"\n===== n = {n} =====")

            for density in density_range:
                times_matrix = []
                times_adj = []
                weights_matrix = []
                weights_adj = []

                f_all.write(f"\n--- Щільність = {density} ---\n")

                for i in range(20):
                    g = generate_random_connected(n, density)

                    # Матриця суміжності
                    start_matrix = time.time()
                    mst_edges_matrix, total_w_matrix = kruskal_from_matrix(g)
                    time_matrix = time.time() - start_matrix

                    times_matrix.append(time_matrix)
                    weights_matrix.append(total_w_matrix)

                    # Списки суміжності
                    start_adj = time.time()
                    mst_edges_adj, total_w_adj = kruskal_from_list(g)
                    time_adj = time.time() - start_adj

                    times_adj.append(time_adj)
                    weights_adj.append(total_w_adj)

                    # Запис усіх результатів
                    f_all.write(f"Прогін {i+1}:\n")
                    f_all.write(f"  Матриця: час = {time_matrix:.6f}, вага MST = {total_w_matrix}\n")
                    f_all.write(f"  Списки: час = {time_adj:.6f}, вага MST = {total_w_adj}\n")
                    if time_matrix < time_adj:
                        faster = time_adj / time_matrix
                        f_all.write(f"  Матриця швидша у {faster:.2f} разів\n")
                    else:
                        faster = time_matrix / time_adj
                        f_all.write(f"  Списки швидші у {faster:.2f} разів\n")

                # Обчислення середніх значень
                avg_time_matrix = sum(times_matrix) / len(times_matrix)
                avg_time_adj = sum(times_adj) / len(times_adj)
                avg_weight_matrix = sum(weights_matrix) / len(weights_matrix)
                avg_weight_adj = sum(weights_adj) / len(weights_adj)

                # Визначення, що швидше
                if avg_time_matrix < avg_time_adj:
                    faster = avg_time_adj / avg_time_matrix
                    faster_str = f"Матриця швидша у {faster:.2f} разів"
                else:
                    faster = avg_time_matrix / avg_time_adj
                    faster_str = f"Списки швидші у {faster:.2f} разів"

                # Запис середніх значень
                f_avg.write(f"\n--- Щільність = {density} ---\n")
                f_avg.write(f"Матриця суміжності: середній час = {avg_time_matrix:.6f}, середня вага MST = {avg_weight_matrix}\n")
                f_avg.write(f"Списки суміжності: середній час = {avg_time_adj:.6f}, середня вага MST = {avg_weight_adj}\n")
                f_avg.write(f"{faster_str}\n")

                print(f"--- Щільність = {density} --- {faster_str}")

        print("\nГотово! Результати записано у файли results_all.txt та results_avg.txt")

if __name__ == "__main__":
    main()