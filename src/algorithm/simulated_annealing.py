import math
import random
import time
import matplotlib.pyplot as plt
from cube.magic_cube import MagicCube

class SimulatedAnnealing:
    def __init__(self, cube, initial_temp=1000.0, final_temp=1.0, cooling_rate=0.995):
        self.cube = cube
        self.initial_temp = initial_temp
        self.final_temp = final_temp
        self.cooling_rate = cooling_rate
        self.best_score = self.cube.objective_function()
        self.scores = [self.best_score]
        self.probabilities = []  # Store e^(Delta E / T) values
        self.stuck_count = 0     # Count how often it gets stuck in local optima

    def swap_elements(self, pos1, pos2):
        x1, y1, z1 = pos1
        x2, y2, z2 = pos2
        self.cube.cube[x1][y1][z1], self.cube.cube[x2][y2][z2] = self.cube.cube[x2][y2][z2], self.cube.cube[x1][y1][z1]

    def find_random_neighbor(self, best_delta):
        pos1 = (random.randint(0, self.cube.size - 1), random.randint(0, self.cube.size - 1), random.randint(0, self.cube.size - 1))
        pos2 = (random.randint(0, self.cube.size - 1), random.randint(0, self.cube.size - 1), random.randint(0, self.cube.size - 1))
        while pos1 == pos2:
            pos2 = (random.randint(0, self.cube.size - 1), random.randint(0, self.cube.size - 1), random.randint(0, self.cube.size - 1))
        
        # Swap elements to create a neighbor
        self.swap_elements(pos1, pos2)
        new_score = self.cube.objective_function()
        delta = self.best_score - new_score
        
        if delta <= best_delta:
            self.swap_elements(pos1, pos2)
        else:
            best_delta = delta
        return new_score, pos1, pos2


    def acceptance_probability(self, old_score, new_score, temperature):
        delta_e = old_score - new_score
        if new_score < old_score:
            return 1.0
        prob = min(1, math.exp(delta_e / temperature))
        return prob

    def run(self, max_iterations=1000):
        start_time = time.perf_counter()
        temperature = self.initial_temp
        best_delta = 0

        for iteration in range(max_iterations):
            new_score, pos1, pos2 = self.find_random_neighbor(best_delta)
            acceptance_prob = self.acceptance_probability(self.best_score, new_score, temperature)

            self.probabilities.append(acceptance_prob) # Track e^(Delta E / T)
            if acceptance_prob > random.random():
                # Accept the new state
                self.best_score = new_score
            else:
                # Revert the swap if not accepted (stuck in a local optimum)
                self.swap_elements(pos1, pos2)
                self.stuck_count += 1

            # Append the best score found so far
            self.scores.append(self.best_score)

            # Cool down the temperature
            temperature *= self.cooling_rate
            if temperature < self.final_temp:
                break

        final_score = self.best_score
        end_time = time.perf_counter()
        duration = end_time - start_time
        self.plot_scores(iteration)
        self.plot_probabilities(iteration)

        return final_score, duration, self.stuck_count

    def plot_scores(self, iteration):
        plt.figure(figsize=(10, 6))
        plt.plot(range(iteration + 2), self.scores, marker='o', color='b', label="Objective Function Value")
        plt.title("Simulated Annealing Progression")
        plt.xlabel("Iteration")
        plt.ylabel("Objective Function Value")
        plt.legend()
        plt.grid(True)
        plt.show()

    def plot_probabilities(self, iteration):
        plt.figure(figsize=(10, 6))
        plt.plot(range(iteration + 1), self.probabilities, marker='x', color='r', label="Acceptance Probability (e^(ΔE/T))")
        plt.title("Acceptance Probability Progression")
        plt.xlabel("Iteration")
        plt.ylabel("e^(ΔE / T)")
        plt.ylim(0, 1)  # Membatasi rentang y-axis dari 0 hingga 1
        plt.yticks([i * 0.1 for i in range(11)]) 
        plt.legend()
        plt.grid(True)
        plt.show()