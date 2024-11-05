from cube.magic_cube import MagicCube
from cube.magic_cube import MagicCube
from algorithms.steepest_hill_climbing import SteepestHillClimbing

magic_cube = MagicCube(size=5)

# Display last objective function value
print("Initial objective score:", magic_cube.objective_function())

# Display first state of magic cube
print("\nFirst state of magic cube:")
magic_cube.display()

# Display last objective function value
hill_climber = SteepestHillClimbing(magic_cube)
hill_climber.run(max_iterations=3)

# Display last state of magic cube
print("\nLast state of magic cube:")
magic_cube.display()