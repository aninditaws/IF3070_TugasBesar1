from cube.magic_cube import MagicCube
from algorithm.simulated_annealing import SimulatedAnnealing

# Parameters
size = 5
initial_temp = 1000
final_temp = 0.1
cooling_rate = 0.999
max_iterations = 1000

# Simulated Annealing
print("\n=== Running Simulated Annealing ===")
magic_cube = MagicCube(size)
simulated_initial_score = magic_cube.objective_function()
print("\nFirst state of magic cube:")
magic_cube.display()
simulated_annealing = SimulatedAnnealing(magic_cube, initial_temp=initial_temp, final_temp=final_temp, cooling_rate=cooling_rate)
simulated_final_score, simulated_duration, simulated_stuck_count = simulated_annealing.run(max_iterations=max_iterations)
print("\nState of magic cube after Simulated Annealing:")
magic_cube.display()

# Display results
print("\n=== Simulated Annealing Results ===")
print(f"Initial Objective Score: {simulated_initial_score}")
print(f"Best Objective Score: {simulated_final_score}")
print(f"Delta: {simulated_initial_score - simulated_final_score}")
print(f"Duration: {simulated_duration} seconds")
print(f"Stuck Count: {simulated_stuck_count}")