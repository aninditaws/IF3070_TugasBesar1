from cube.magic_cube import MagicCube
from algorithm.simulated_annealing import SimulatedAnnealing

size = 5
initial_temperature = 1000
final_temperature = 1e-20
cooling_rate = 0.9999
threshold = 0.5

print(f"\n=== Running Simulated Annealing ===")
magic_cube = MagicCube(size=size)
simulated_initial_score = magic_cube.objective_function()
print("\nFirst state of magic cube:")
magic_cube.display()

simulated_annealing = SimulatedAnnealing(
    cube=magic_cube,
    initial_temperature=initial_temperature,
    final_temperature=final_temperature,
    cooling_rate=cooling_rate,
    threshold=threshold
)
best_score, duration, stuck_frequency, iteration = simulated_annealing.run()

print("\nState of magic cube after Simulated Annealing:")
magic_cube.display()

print(f"\nInitial Objective Score: {simulated_initial_score}")
print(f"Best Objective Score: {best_score}")
print(f"Delta: {simulated_initial_score - best_score}")
print(f"Duration: {duration:.6f} seconds")
print(f"Total Iterations: {iteration}")
print(f"Stuck Frequency: {stuck_frequency}")