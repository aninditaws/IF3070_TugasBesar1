import sys
import time
from cube.magic_cube import MagicCube
# from algorithms.steepest_hill_climbing import SteepestHillClimbing
# from algorithms.sideways_move import SidewaysMove
# from algorithms.stochastic import StochasticHillClimbing
from algorithms.random_restart import RandomRestartHillClimbing

# Meminta input jumlah restart dan jumlah iterasi per restart dari pengguna
max_restarts = int(input("Masukkan jumlah restart: "))
max_iterations_per_restart = int(input("Masukkan jumlah iterasi per restart: "))

size = 5
max_iterations = 1000


algorithms = []

# print("\n=== Running Steepest Hill Climbing ===")
# magic_cube = MagicCube(size)
# steepest_initial_score = magic_cube.objective_function()
# magic_cube.display()
# steepest_hill = SteepestHillClimbing(magic_cube)
# steepest_final_score, steepest_duration, steepest_iteration = steepest_hill.run(max_iterations)
# algorithms.append(
#     {
#         "algorithm": "Steepest Hill Climbing",
#         "initial_score": steepest_initial_score,
#         "final_score": steepest_final_score,
#         "delta": steepest_initial_score - steepest_final_score,
#         "duration": steepest_duration,
#         "iteration": steepest_iteration
#     }
# )

# print("\n=== Running Sideways Move Hill Climbing ===")
# magic_cube = MagicCube(size)
# sideways_initial_score = magic_cube.objective_function()
# sideways_climber = SidewaysMove(magic_cube)
# sideways_final_score, sideways_duration, sideways_iteration = sideways_climber.run(max_iterations, max_sideways_iteration)
# algorithms.append(
#     {
#         "algorithm": "Sideways Move Hill Climbing",
#         "initial_score": sideways_initial_score,
#         "final_score": sideways_final_score,
#         "delta": sideways_initial_score - sideways_final_score,
#         "duration": sideways_duration,
#         "iteration": sideways_iteration
#     }
# )

# print("\n=== Running Stochastic Hill Climbing ===")
# magic_cube = MagicCube(size)
# stochastic_initial_score = magic_cube.objective_function()
# stochastic_climber = StochasticHillClimbing(magic_cube)
# stochastic_final_score, stochastic_duration, stochastic_iteration = stochastic_climber.run(max_iterations)
# algorithms.append(
#     {
#         "algorithm": "Stochastic Hill Climbing",
#         "initial_score": stochastic_initial_score,
#         "final_score": stochastic_final_score,
#         "delta": stochastic_initial_score - stochastic_final_score,
#         "duration": stochastic_duration,
#         "iteration": stochastic_iteration
#     }
# )

print("\n=== Running Random Restart Hill Climbing ===")
magic_cube = MagicCube(size)
random_restart_initial_score = magic_cube.objective_function()
print ("First state of magic cube:")
magic_cube.display()
random_restart_climber = RandomRestartHillClimbing(magic_cube, max_restarts, max_iterations_per_restart)
random_restart_final_score, random_restart_duration, random_restart_iteration = random_restart_climber.run()

magic_cube.display()
algorithms.append(
    {
        "algorithm": "Random Restart Hill Climbing",
        "initial_score": random_restart_initial_score,
        "final_score": random_restart_final_score,
        "delta": random_restart_initial_score - random_restart_final_score,
        "duration": random_restart_duration,
        "iteration": random_restart_iteration
    }
)

# # Display comparison results
# print("\n=== Comparison of Algorithm Improvements ===")
# for algo in algorithms:
#     print(f"\nAlgorithm: {algo['algorithm']}")
#     print(f"Initial Score: {algo['initial_score']}")
#     print(f"Final Score: {algo['final_score']}")
#     print(f"Delta: {algo['delta']}")
#     print(f"Duration: {algo['duration']:.4f} seconds")
#     print(f"Iteration: {algo['iteration']}")
