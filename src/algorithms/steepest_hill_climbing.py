import random
import time
import matplotlib.pyplot as plt
from cube.magic_cube import MagicCube

class SteepestHillClimbing:
    def __init__(self, cube):
        self.cube = cube
        self.best_score = self.cube.objective_function()
        self.scores = []

    def swap_elements(self, pos1, pos2):
        x1, y1, z1 = pos1
        x2, y2, z2 = pos2
        self.cube.cube[x1][y1][z1], self.cube.cube[x2][y2][z2] = self.cube.cube[x2][y2][z2], self.cube.cube[x1][y1][z1]

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

                    if delta > best_delta:
                        best_delta = delta
                        best_positions = (pos1, pos2)

                    self.swap_elements(pos1, pos2)

        return best_positions, best_delta

    def run(self, max_iterations=1000):
        start_time = time.perf_counter()
        last_best_delta = 0
        iteration = 0

        self.scores.append(self.cube.objective_function())

        while iteration < max_iterations:
            best_positions, best_delta = self.find_best_neighbor()

            if best_delta == last_best_delta:
                break

            self.swap_elements(*best_positions)
            self.scores.append(self.cube.objective_function())
            print(f"Iteration {iteration}: objective score {self.cube.objective_function()}, best delta: {best_delta}\n")
            last_best_delta = best_delta
            iteration += 1

        final_score = self.cube.objective_function()
        end_time = time.perf_counter()
        duration = end_time - start_time
        self.plot_scores(iteration)

        return final_score, duration

    def plot_scores(self, iteration):
        plt.figure(figsize=(10, 6))
        plt.plot(range(iteration + 1), self.scores, marker='o', color='b', label="Objective Function Value")
        plt.xticks(range(0, iteration + 1, 1))
        plt.title("Steepest Ascent Hill-Climbing Progression")
        plt.xlabel("Iteration")
        plt.ylabel("Objective Function Value")
        plt.legend()
        plt.grid(True)
        plt.show()