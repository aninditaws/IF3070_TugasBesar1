import random
import time
import matplotlib.pyplot as plt
from cube.magic_cube import MagicCube

class SidewaysMove:
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
                    elif delta == best_delta and best_delta == 0:
                        # Allow sideways move if delta is zero
                        best_positions = (pos1, pos2)

                    # Swap back to restore original state
                    self.swap_elements(pos1, pos2)

        return best_positions, best_delta

    def run(self, max_iterations=1000, max_sideways_iteration=100):
        """Runs the algorithm with a limit on sideways moves."""
        start_time = time.perf_counter()
        iteration = 0
        sideways_iteration = 0

        while iteration < max_iterations:
            self.scores.append(self.best_score)
            
            # Find the best swap
            best_positions, best_delta = self.find_best_neighbor()

            # If no improvement and sideways limit reached, stop
            if best_delta == 0:
                sideways_iteration += 1
                if sideways_iteration >= max_sideways_iteration:
                    print(f"Reached sideways limit of {max_sideways_iteration}. Stopping.")
                    break
            else:
                sideways_iteration = 0  # Reset sideways counter if improvement

            # Perform the best swap
            if best_positions:
                self.swap_elements(*best_positions)
                self.best_score -= best_delta
            iteration += 1

        # Record the final score and stop timing
        self.scores.append(self.best_score)
        end_time = time.perf_counter()
        duration = end_time - start_time

        # Plot the objective score progression
        self.plot_scores(iteration)

        print(f"Final score after {iteration} iterations: {self.best_score}")
        print(f"Duration of the search process: {duration:.4f} seconds")
        return self.best_score

    def plot_scores(self, iteration):
        # plt.gcf().canvas.manager.set_window_title("Hill-Climbing with Sideways Move Progression")
        plt.figure(figsize=(10, 6))
        plt.plot(range(iteration + 1), self.scores, marker='o', color='b', label="Objective Function Value")
        plt.xticks(range(0, iteration + 1, 1))
        plt.title("Hill-Climbing with Sideways Move Progression")
        plt.xlabel("Iteration")
        plt.ylabel("Objective Function Value")
        plt.legend()
        plt.grid(True)
        plt.show()
