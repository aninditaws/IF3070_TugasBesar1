# import random
# import time
# import matplotlib.pyplot as plt
# from cube.magic_cube import MagicCube

# class StochasticHillClimbing:
#     def __init__(self, cube):
#         self.cube = cube
#         self.best_score = self.cube.objective_function()
#         self.scores = []

#     def swap_elements(self, pos1, pos2):
#         x1, y1, z1 = pos1
#         x2, y2, z2 = pos2
#         self.cube.cube[x1][y1][z1], self.cube.cube[x2][y2][z2] = self.cube.cube[x2][y2][z2], self.cube.cube[x1][y1][z1]

#     def find_random_neighbor(self):
#         # Randomly select two unique positions in the cube
#         pos1 = (random.randint(0, self.cube.size - 1), random.randint(0, self.cube.size - 1), random.randint(0, self.cube.size - 1))
#         pos2 = (random.randint(0, self.cube.size - 1), random.randint(0, self.cube.size - 1), random.randint(0, self.cube.size - 1))
        
#         # Ensure the two positions are different
#         while pos1 == pos2:
#             pos2 = (random.randint(0, self.cube.size - 1), random.randint(0, self.cube.size - 1), random.randint(0, self.cube.size - 1))
        
#         # Swap and evaluate
#         self.swap_elements(pos1, pos2)
#         new_score = self.cube.objective_function()
#         delta = self.best_score - new_score

#         # Decide to keep the new configuration or revert
#         if delta > 0:  # Improvement
#             self.best_score = new_score
#             return True
#         else:
#             # Revert swap if no improvement
#             self.swap_elements(pos1, pos2)
#             return False

#     def run(self, max_iterations=1000):
#         start_time = time.perf_counter()
#         iteration = 0
#         iteration_improve = 0

#         while iteration < max_iterations:             
#             # Try a random neighbor
#             improved = self.find_random_neighbor()

#             # If no improvement, skip to next iteration
#             if not improved:
#                 iteration += 1
#                 continue
            
#             # If improvement is found, count the iteration and continue
#             # print(f"Iteration {iteration + 1}: Score = {self.best_score}")
#             self.scores.append(self.best_score)
#             iteration += 1
#             iteration_improve += 1

#         # Record the final score and stop timing
#         self.scores.append(self.best_score)
#         end_time = time.perf_counter()
#         duration = end_time - start_time

#         # Plot the objective score progression
#         self.plot_scores(iteration_improve)

#         print(f"Final score after {iteration} iterations: {self.best_score}")
#         print(f"Duration of the search process: {duration:.4f} seconds")
#         return self.best_score, duration 

#     def plot_scores(self, iteration):
#         # plt.gcf().canvas.manager.set_window_title("Stochastic Hill-Climbing Progression")
#         plt.figure(figsize=(10, 6))
#         plt.plot(range(iteration + 1), self.scores, marker='o', color='b', label="Objective Function Value")
#         plt.xticks(range(0, iteration + 1, 1))
#         plt.title("Stochastic Hill-Climbing Progression")
#         plt.xlabel("Iteration")
#         plt.ylabel("Objective Function Value")
#         plt.legend()
#         plt.grid(True)
#         plt.show()





























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
