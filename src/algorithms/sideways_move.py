import random
import time
import matplotlib.pyplot as plt
from cube.magic_cube import MagicCube

class SidewaysMove:
    # Fungsi untuk menyimpan informasi inisialisasi kubus untuk digunakan pada algoritma ini
    def __init__(self, cube):
        self.cube = cube
        self.best_score = self.cube.objective_function() 
        self.scores = []

    # Fungsi untuk menukar dua elemen dalam kubus
    def swap_elements(self, pos1, pos2):
        x1, y1, z1 = pos1
        x2, y2, z2 = pos2
        self.cube.cube[x1][y1][z1], self.cube.cube[x2][y2][z2] = self.cube.cube[x2][y2][z2], self.cube.cube[x1][y1][z1]

    # Fungsi untuk mencari state neighbour yang terbaik
    def find_best_neighbor(self):
        delta = 0
        best_delta = 0

        positions = [(x, y, z) for x in range (self.cube.size) for y in range (self.cube.size) for z in range (self.cube.size)]
        for pos1 in positions:
            for pos2 in positions:
                if pos2 > pos1:
                    self.swap_elements(pos1, pos2)
                    new_score = self.cube.objective_function()
                    delta = self.best_score - new_score

                    if delta >= best_delta:
                        best_delta = delta
                        best_positions = (pos1, pos2)

                    self.swap_elements(pos1, pos2)

        return best_positions, best_delta

    # Fungsi untuk menjalankan algoritma steepest
    def run(self, max_iterations=1000, max_sideways_iteration=100):
        start_time = time.perf_counter()
        last_best_delta = 0
        iteration = 0
        most_sideways_iteration = 0
        sideways_iteration = 0

        self.scores.append(self.cube.objective_function())

        while iteration < max_iterations:
            best_positions, best_delta = self.find_best_neighbor()

            if best_delta == last_best_delta:                             # kondisi untuk menambahkan jumlah iterasi sideways jika melalui sideways
                sideways_iteration += 1
                if sideways_iteration > most_sideways_iteration:
                    most_sideways_iteration = sideways_iteration
            else:                                                         # kondisi untuk mereset jumlah iterasi sideways jika state algoritma sudah tidak sideways 
                sideways_iteration = 0
                most_sideways_iteration = 0
                
            if sideways_iteration >= max_sideways_iteration:              # kondisi untuk memberhentikan algoritma jika iterasi sideways melebihi batas yang ditentukan 
                break

            self.swap_elements(*best_positions)
            self.scores.append(self.cube.objective_function())
            # print(f"Iteration {iteration}: objective score {self.cube.objective_function()}\n")
            last_best_delta = best_delta
            iteration += 1

        final_score = self.cube.objective_function()
        end_time = time.perf_counter()
        duration = end_time - start_time
        self.plot_scores(iteration)

        return final_score, duration, iteration, most_sideways_iteration

    # Fungsi untuk membuat plot diagram 
    def plot_scores(self, iteration):
        plt.figure(figsize=(10, 6))
        plt.plot(range(iteration + 1), self.scores, marker='o', color='b', label="Objective Function Value")
        plt.xticks(range(0, iteration + 1, 1))
        plt.title("Hill-Climbing with Sideways Move Progression")
        plt.xlabel("Iteration")
        plt.ylabel("Objective Function Value")
        plt.legend()
        plt.grid(True)
        plt.show()