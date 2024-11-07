import sys
import time
import matplotlib.pyplot as plt
from cube.magic_cube import MagicCube
from algorithms.steepest_hill_climbing import SteepestHillClimbing
from algorithms.sideways_move import SidewaysMove
from algorithms.stochastic import StochasticHillClimbing

size = 5
max_iterations = 1000
max_sideways_iteration = 5

algorithms = []

print("\n=== Running Steepest Hill Climbing ===")
magic_cube = MagicCube(size)
steepest_initial_score = magic_cube.objective_function()
print("First state of magic cube:")
magic_cube.display()
steepest_hill = SteepestHillClimbing(magic_cube)
steepest_final_score, steepest_move_duration = steepest_hill.run(max_iterations)
print("\nState of magic cube after Steepest Hill Climbing:")
magic_cube.display()
algorithms.append(
    {
        "algorithm": "Steepest Hill Climbing",
        "initial_score": steepest_initial_score,
        "final_score": steepest_final_score,
        "delta": steepest_initial_score - steepest_final_score,
        "duration": steepest_move_duration
    }
)

print("\n=== Running Sideways Move Hill Climbing ===")
magic_cube = MagicCube(size)
sideways_initial_score = magic_cube.objective_function()
print("First state of magic cube:")
magic_cube.display()
sideways_climber = SidewaysMove(magic_cube)
sideways_final_score, sideways_move_duration = sideways_climber.run(max_iterations, max_sideways_iteration)
print("\nState of magic cube after Sideways Move Hill Climbing:")
magic_cube.display()
algorithms.append(
    {
        "algorithm": "Sideways Move Hill Climbing",
        "initial_score": sideways_initial_score,
        "final_score": sideways_final_score,
        "delta": sideways_initial_score - sideways_final_score,
        "duration": sideways_move_duration
    }
)

print("\n=== Running Stochastic Hill Climbing ===")
magic_cube = MagicCube(size)
stochastic_initial_score = magic_cube.objective_function()
print("First state of magic cube:")
magic_cube.display()
stochastic_climber = StochasticHillClimbing(magic_cube)
stochastic_final_score, stochastic_duration = stochastic_climber.run(max_iterations)
print("\nState of magic cube after Stochastic Hill Climbing:")
magic_cube.display()
algorithms.append(
    {
        "algorithm": "Stochastic Hill Climbing",
        "initial_score": stochastic_initial_score,
        "final_score": stochastic_final_score,
        "delta": stochastic_initial_score - stochastic_final_score,
        "duration": stochastic_duration
    }
)

best_algorithm_delta = max(algorithms, key=lambda algo: algo["delta"])
best_algorithm_duration = min(algorithms, key=lambda algo: algo["duration"])

print("\n=== Comparison of Algorithm Improvements ===")
for algo in algorithms:
    print(f"\nAlgorithm: {algo['algorithm']}")
    print(f"Initial Score: {algo['initial_score']}")
    print(f"Final Score: {algo['final_score']}")
    print(f"Delta: {algo['delta']}")
    print(f"Duration: {algo['duration']:.4f} seconds")

print("\n" + "-" * 50)

print("\n=== Algorithm with the Largest Improvement ===")
print(f"Algorithm: {best_algorithm_delta['algorithm']}")
print(f"Delta: {best_algorithm_delta['delta']}")
print(f"Final Score: {best_algorithm_delta['final_score']}")

print("\n=== Algorithm with the Fastest Duration ===")
print(f"Algorithm: {best_algorithm_duration['algorithm']}")
print(f"Duration: {best_algorithm_duration['duration']:.4f} seconds")