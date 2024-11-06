import random
import time
import matplotlib.pyplot as plt
from cube.magic_cube import MagicCube

class StochasticHillClimbing:
    def __init__(self, cube):
        self.cube = cube
        self.best_score = self.cube.objective_function()
        self.scores = []

    def swap_elements(self, pos1, pos2):
        x1, y1, z1 = pos1
        x2, y2, z2 = pos2
        self.cube.cube[x1][y1][z1], self.cube.cube[x2][y2][z2] = self.cube.cube[x2][y2][z2], self.cube.cube[x1][y1][z1]

    def find_random_neighbor(self, best_delta):
        pos1 = (random.randint(0, self.cube.size - 1), random.randint(0, self.cube.size - 1), random.randint(0, self.cube.size - 1))
        pos2 = (random.randint(0, self.cube.size - 1), random.randint(0, self.cube.size - 1), random.randint(0, self.cube.size - 1))
        while pos1 == pos2:
            pos2 = (random.randint(0, self.cube.size - 1), random.randint(0, self.cube.size - 1), random.randint(0, self.cube.size - 1))
        
        self.swap_elements(pos1, pos2)
        new_score = self.cube.objective_function()
        delta = self.best_score - new_score

        if delta <= best_delta:
            self.swap_elements(pos1, pos2)
        else:
            best_delta = delta

        return best_delta
        

    def run(self, max_iterations=1000):
        start_time = time.perf_counter()
        best_delta = 0
        iteration = 0

        self.scores.append(self.cube.objective_function())

        while iteration < max_iterations:
            best_delta = self.find_random_neighbor(best_delta)
            self.scores.append(self.cube.objective_function())
            iteration += 1

        final_score = self.cube.objective_function()
        end_time = time.perf_counter()
        duration = end_time - start_time
        self.plot_scores(iteration)

        return final_score, duration

    def plot_scores(self, iteration):
        # plt.gcf().canvas.manager.set_window_title("Stochastic Hill-Climbing Progression")
        plt.figure(figsize=(10, 6))
        plt.plot(range(iteration + 1), self.scores, marker='o', color='b', label="Objective Function Value")
        plt.xticks(range(0, iteration + 1, 1))
        plt.title("Stochastic Hill-Climbing Progression")
        plt.xlabel("Iteration")
        plt.ylabel("Objective Function Value")
        plt.legend()
        plt.grid(True)
        plt.show()
