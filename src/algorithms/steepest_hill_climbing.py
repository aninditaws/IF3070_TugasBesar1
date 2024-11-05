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
        best_delta = 0
        best_positions = None

        # Generate all unique pairs of positions in the cube
        positions = [(x, y, z) for x in range(self.cube.size) for y in range(self.cube.size) for z in range(self.cube.size)]
        for pos1 in positions:
            for pos2 in positions:
                if pos1 < pos2:
                    # Swap and evaluate
                    self.swap_elements(pos1, pos2)
                    new_score = self.cube.objective_function()
                    delta = self.best_score - new_score

                    # Check if this swap improves the score the most
                    if delta > best_delta:
                        best_delta = delta
                        best_positions = (pos1, pos2)

                    # Swap back to restore original state
                    self.swap_elements(pos1, pos2)

        return best_positions, best_delta

    def run(self, max_iterations=1000):
        start_time = time.time()
        iteration = 0

        while iteration < max_iterations:
            self.scores.append(self.best_score)
            
            # Find the best swap
            best_positions, best_delta = self.find_best_neighbor()

            # If no improvement is found, terminate
            if best_delta <= 0:
                print(f"No further improvement found at iteration {iteration}. Final score: {self.best_score}")
                break

            # Perform the best swap
            self.swap_elements(*best_positions)
            self.best_score -= best_delta
            iteration += 1

            # print(f"Iteration {iteration}: Score = {self.best_score}")

        self.scores.append(self.best_score)
        end_time = time.time()
        duration = end_time - start_time

        # Plot the objective score progression
        self.plot_scores(iteration)

        print(f"Final score after {iteration} iterations: {self.best_score}")
        print(f"Duration of the search process: {duration:.2f} seconds")
        return self.best_score

    def plot_scores(self, iteration):
        plt.figure(figsize=(10, 6))
        plt.plot(range(iteration + 1), self.scores, marker='o', color='b', label="Objective Function Value")
        plt.title("Objective Function Value over Iterations")
        plt.xlabel("Iteration")
        plt.ylabel("Objective Function Value")
        plt.legend()
        plt.grid(True)
        plt.show()