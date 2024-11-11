import math
import random
import copy
import time
import matplotlib.pyplot as plt

class SimulatedAnnealing:
    def __init__(self, initial_state, initial_temp, cooling_rate, min_temp):
        self.current_state = initial_state
        self.current_score = self.objective_function(self.current_state)
        self.best_state = copy.deepcopy(self.current_state)
        self.best_score = self.current_score
        self.temperature = initial_temp
        self.cooling_rate = cooling_rate
        self.min_temp = min_temp
        self.scores = []           # Track scores at each accepted move
        self.temperatures = []      # Track temperature (move threshold) over time
        self.stuck_count = 0        # Count of stuck states

    def objective_function(self, state):
        # Replace this with the actual objective function for your problem
        return sum(state)  # Example objective function (sum of elements in state)

    def get_neighbor(self, state):
        # Define how to generate a neighboring state
        neighbor = copy.deepcopy(state)
        index = random.randint(0, len(state) - 1)
        neighbor[index] += random.choice([-1, 1])  # Small random change
        return neighbor

    def accept_probability(self, delta, temperature):
        # Calculate acceptance probability
        return math.exp(-delta / temperature)

    def run(self):
        start_time = time.perf_counter()
        iteration = 0

        while self.temperature > self.min_temp:
            # Track the temperature and current score at each iteration
            self.temperatures.append(self.temperature)
            self.scores.append(self.current_score)

            # Generate a neighboring state
            neighbor_state = self.get_neighbor(self.current_state)
            neighbor_score = self.objective_function(neighbor_state)
            delta = neighbor_score - self.current_score

            # Determine if we should accept the neighbor state
            if delta < 0 or random.random() < self.accept_probability(delta, self.temperature):
                # Move to the neighbor state if accepted
                self.current_state = neighbor_state
                self.current_score = neighbor_score
                if self.current_score < self.best_score:
                    self.best_state = copy.deepcopy(self.current_state)
                    self.best_score = self.current_score
            else:
                # Increment stuck count if no improvement
                self.stuck_count += 1

            # Cool down the temperature
            self.temperature *= self.cooling_rate
            iteration += 1

        end_time = time.perf_counter()
        duration = end_time - start_time

        # Final score tracking for plot consistency
        self.scores.append(self.current_score)
        self.temperatures.append(self.temperature)

        return self.best_state, self.best_score, duration, iteration, self.stuck_count

    def plot_progress(self, iteration):
        plt.figure(figsize=(12, 6))

        # Plot Objective Function Value
        plt.plot(range(iteration + 1), self.scores, marker='o', color='b', label="Objective Function Value")

        # Plot Move Threshold (Temperature)
        plt.plot(range(iteration + 1), self.temperatures, color='r', linestyle='--', label="Move Threshold (Temperature)")

        # Set x-axis ticks
        plt.xticks(range(0, iteration + 1, 1))
        plt.title("Simulated Annealing Progression")
        plt.xlabel("Iteration")
        plt.ylabel("Value")
        plt.legend()
        plt.grid(True)
        plt.show()






























































# import sys
# import time
# import random
# import matplotlib.pyplot as plt
# from cube.magic_cube import MagicCube
# from algorithms.steepest_hill_climbing import SteepestHillClimbing
# from algorithms.sideways_move import SidewaysMove
# from algorithms.stochastic import StochasticHillClimbing
# from algorithms.simulated_annealing import SimulatedAnnealing

# size = 5
# max_iterations = 1000
# max_sideways_iteration = 5
# initial_temp = 100.0
# cooling_rate = 0.95
# min_temp = 1e-3

# algorithms = []

# # print("\n=== Running Steepest Hill Climbing ===")
# # magic_cube = MagicCube(size)
# # steepest_initial_score = magic_cube.objective_function()
# # print("First state of magic cube:")
# # magic_cube.display()
# # steepest_hill = SteepestHillClimbing(magic_cube)
# # steepest_final_score, steepest_move_duration, steepest_move_iteration = steepest_hill.run(max_iterations)
# # print("\nState of magic cube after Steepest Hill Climbing:")
# # magic_cube.display()
# # algorithms.append(
# #     {
# #         "algorithm": "Steepest Hill Climbing",
# #         "initial_score": steepest_initial_score,
# #         "final_score": steepest_final_score,
# #         "delta": steepest_initial_score - steepest_final_score,
# #         "duration": steepest_move_duration,
# #         "iteration": steepest_move_iteration
# #     }
# # )

# # print("\n=== Running Sideways Move Hill Climbing ===")
# # magic_cube = MagicCube(size)
# # sideways_initial_score = magic_cube.objective_function()
# # print("First state of magic cube:")
# # magic_cube.display()
# # sideways_climber = SidewaysMove(magic_cube)
# # sideways_final_score, sideways_move_duration, sideways_move_iteration = sideways_climber.run(max_iterations, max_sideways_iteration)
# # print("\nState of magic cube after Sideways Move Hill Climbing:")
# # magic_cube.display()
# # algorithms.append(
# #     {
# #         "algorithm": "Sideways Move Hill Climbing",
# #         "initial_score": sideways_initial_score,
# #         "final_score": sideways_final_score,
# #         "delta": sideways_initial_score - sideways_final_score,
# #         "duration": sideways_move_duration,
# #         "iteration": sideways_move_iteration
# #     }
# # )

# # print("\n=== Running Stochastic Hill Climbing ===")
# # magic_cube = MagicCube(size)
# # stochastic_initial_score = magic_cube.objective_function()
# # print("First state of magic cube:")
# # magic_cube.display()
# # stochastic_climber = StochasticHillClimbing(magic_cube)
# # stochastic_final_score, stochastic_duration, stochastic_iteration = stochastic_climber.run(max_iterations)
# # print("\nState of magic cube after Stochastic Hill Climbing:")
# # magic_cube.display()
# # algorithms.append(
# #     {
# #         "algorithm": "Stochastic Hill Climbing",
# #         "initial_score": stochastic_initial_score,
# #         "final_score": stochastic_final_score,
# #         "delta": stochastic_initial_score - stochastic_final_score,
# #         "duration": stochastic_duration,
# #         "iteration": stochastic_iteration
# #     }
# # )

# print("\n=== Running Simulated Annealing ===")
# initial_state = [random.randint(1, 100) for _ in range(size)]  
# simulated_annealing = SimulatedAnnealing(initial_state, initial_temp, cooling_rate, min_temp)
# best_state, simulated_final_score, simulated_duration, simulated_iteration, stuck_count = simulated_annealing.run()  # Adjusted unpacking to five values
# simulated_initial_score = simulated_annealing.objective_function(initial_state)
# print("\nFinal state after Simulated Annealing:", best_state)
# algorithms.append(
#     {
#         "algorithm": "Simulated Annealing",
#         "initial_score": simulated_initial_score,
#         "final_score": simulated_final_score,
#         "delta": simulated_initial_score - simulated_final_score,
#         "duration": simulated_duration,
#         "iteration": simulated_iteration
#     }
# )

# best_algorithm_delta = max(algorithms, key=lambda algo: algo["delta"])
# best_algorithm_duration = min(algorithms, key=lambda algo: algo["duration"])

# print("\n=== Comparison of Algorithm Improvements ===")
# for algo in algorithms:
#     print(f"\nAlgorithm: {algo['algorithm']}")
#     print(f"Initial Score: {algo['initial_score']}")
#     print(f"Final Score: {algo['final_score']}")
#     print(f"Delta: {algo['delta']}")
#     print(f"Duration: {algo['duration']:.4f} seconds")
#     print(f"Iteration: {algo['iteration']}")

# print("\n" + "-" * 50)

# print("\n=== Algorithm with the Largest Improvement ===")
# print(f"Algorithm: {best_algorithm_delta['algorithm']}")
# print(f"Delta: {best_algorithm_delta['delta']}")
# print(f"Final Score: {best_algorithm_delta['final_score']}")

# print("\n=== Algorithm with the Fastest Duration ===")
# print(f"Algorithm: {best_algorithm_duration['algorithm']}")
# print(f"Duration: {best_algorithm_duration['duration']:.4f} seconds")