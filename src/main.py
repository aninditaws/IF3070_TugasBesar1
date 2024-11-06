from cube.magic_cube import MagicCube
from algorithms.steepest_hill_climbing import SteepestHillClimbing
from algorithms.sideways_move import SidewaysMove
from algorithms.stochastic import StochasticHillClimbing

# Initialize the magic cube
magic_cube = MagicCube(size=5)

# Display initial objective function value and first state
print("\nFirst state of magic cube:")
magic_cube.display()

# === Steepest Hill Climbing ===
print("\n=== Running Steepest Hill Climbing ===")
print("Initial objective score:", magic_cube.objective_function())
hill_climber = SteepestHillClimbing(magic_cube)
hill_climber.run(max_iterations=3)

# Display final state after Steepest Hill Climbing
print("\nState of magic cube after Steepest Hill Climbing:")
magic_cube.display()

# === Sideways Move Hill Climbing ===
print("\n=== Running Sideways Move Hill Climbing ===")
# Re-initialize the magic cube for a fresh start
magic_cube = MagicCube(size=5)
print("Initial objective score:", magic_cube.objective_function())
sideways_climber = SidewaysMove(magic_cube)
sideways_climber.run(max_iterations=3, max_sideways_iteration=5)

# Display final state after Sideways Move Hill Climbing
print("\nState of magic cube after Sideways Move Hill Climbing:")
magic_cube.display()

# === Stochastic Hill Climbing ===
print("\n=== Running Stochastic Hill Climbing ===")
# Re-initialize the magic cube for a fresh start
magic_cube = MagicCube(size=5)
print("Initial objective score:", magic_cube.objective_function())
stochastic_climber = StochasticHillClimbing(magic_cube)
stochastic_climber.run(max_iterations=3)

# Display final state after Stochastic Hill Climbing
print("\nState of magic cube after Stochastic Hill Climbing:")
magic_cube.display()
