import sys
import os
import matplotlib.pyplot as plt
from cube.magic_cube import MagicCube
from algorithms.steepest_hill_climbing import SteepestHillClimbing
from algorithms.sideways_move import SidewaysMove
from algorithms.stochastic import StochasticHillClimbing
from algorithms.random_restart import RandomRestartHillClimbing
from algorithms.genetic_algorithm import GeneticAlgorithmMagicCube
from algorithms.simulated_annealing import SimulatedAnnealing

# Variabel global
size = 5
max_iterations = 1
max_sideways_iteration = 10
initial_temp = 1000
final_temp = 1e-20
cooling_rate = 0.9999
threshold = 0.5
algorithms = []

# Mengosongkan terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Pendefinisian warna
LIME_GREEN = "\033[38;5;149m"
TEAL = "\033[38;2;42;157;143m"
GOLDEN_YELLOW = "\033[38;2;233;196;106m"
ORANGE = "\033[38;2;244;162;97m"
RED_ORANGE = "\033[38;2;231;111;81m"
RESET_COLOR = "\033[0m"

# Shortcut text dengan warna
def separator(title):
    print("\n" + "=" * 50)
    print(TEAL + f"===== {title} =====" + RESET_COLOR)
    print("=" * 50 + RESET_COLOR)

def colorText(text, color):
    print(color + f"{text}" + RESET_COLOR)

# Fungsi pemanggilan algoritma
def run_steepest_hill_climbing():
    magic_cube = MagicCube(size)
    steepest_initial_score = magic_cube.objective_function()
    colorText("First state of magic cube:", LIME_GREEN)
    magic_cube.display()
    steepest_hill = SteepestHillClimbing(magic_cube)
    steepest_final_score, steepest_move_duration, steepest_move_iteration = steepest_hill.run(max_iterations)
    colorText("\nState of magic cube after Steepest Hill Climbing:", LIME_GREEN)
    magic_cube.display()
    algorithms.append({
        "algorithm": "Steepest Hill Climbing",
        "initial_score": steepest_initial_score,
        "final_score": steepest_final_score,
        "delta": steepest_initial_score - steepest_final_score,
        "duration": steepest_move_duration,
        "iteration": steepest_move_iteration
    })

def run_sideways_move_hill_climbing():
    magic_cube = MagicCube(size)
    sideways_initial_score = magic_cube.objective_function()
    colorText("First state of magic cube:", LIME_GREEN)
    magic_cube.display()
    sideways_climber = SidewaysMove(magic_cube)
    sideways_final_score, sideways_move_duration, sideways_move_iteration, most_sideways_move_iteration = sideways_climber.run(max_iterations, max_sideways_iteration)
    colorText("\nState of magic cube after Sideways Move Hill Climbing:", LIME_GREEN)
    magic_cube.display()
    algorithms.append({
        "algorithm": "Sideways Move Hill Climbing",
        "initial_score": sideways_initial_score,
        "final_score": sideways_final_score,
        "delta": sideways_initial_score - sideways_final_score,
        "duration": sideways_move_duration,
        "iteration": sideways_move_iteration,
        "most_sideways_iteration": most_sideways_move_iteration
    })

def run_stochastic_hill_climbing():
    magic_cube = MagicCube(size)
    stochastic_initial_score = magic_cube.objective_function()
    colorText("First state of magic cube:", LIME_GREEN)
    magic_cube.display()
    stochastic_climber = StochasticHillClimbing(magic_cube)
    stochastic_final_score, stochastic_duration, stochastic_iteration = stochastic_climber.run(max_iterations)
    colorText("\nState of magic cube after Stochastic Hill Climbing:", LIME_GREEN)
    magic_cube.display()
    algorithms.append({
        "algorithm": "Stochastic Hill Climbing",
        "initial_score": stochastic_initial_score,
        "final_score": stochastic_final_score,
        "delta": stochastic_initial_score - stochastic_final_score,
        "duration": stochastic_duration,
        "iteration": stochastic_iteration
    })

def run_random_restart():
    magic_cube = MagicCube(size)
    randomr_initial_score = magic_cube.objective_function()
    colorText("First state of magic cube:", LIME_GREEN)
    magic_cube.display()
    random_restart = RandomRestartHillClimbing(magic_cube)
    randomr_final_score, randomr_duration, randomr_restart = random_restart.run(max_restart, max_iteration_per_restart)
    colorText("\nState of magic cube after Random Restart Hill Climbing:", LIME_GREEN)
    magic_cube.display()
    algorithms.append({
        "algorithm": "Random Restart Hill Climbing",
        "initial_score": randomr_initial_score,
        "final_score": randomr_final_score,
        "delta": randomr_initial_score - randomr_final_score,
        "duration": randomr_duration,
        "iteration": randomr_restart
    })

def run_genetic_algorithm():
    magic_cube = MagicCube(size)
    population_size = int(input("Enter Population Size: "))
    iteration = int(input("Enter Number of Iterations: "))
    genetic_algorithm = GeneticAlgorithmMagicCube(population_size=population_size, mutation_rate=0.1,
                                                  iterations=iteration)
    colorText("First state of magic cube:", LIME_GREEN)
    magic_cube.display()
    genetic_initial_score, genetic_final_score, duration = genetic_algorithm.run()
    colorText("\nState of magic cube after Genetic Algorithm:", LIME_GREEN)
    magic_cube.display()
    algorithms.append(
        {
            "algorithm": "Genetic Algorithm",
            "initial_score": genetic_initial_score,
            "final_score": genetic_final_score,
            "delta": genetic_initial_score - genetic_final_score,
            "duration": duration,
            "population": population_size,
            "iteration": iteration
        }
    )

def run_simulated_annealing():
    magic_cube = MagicCube(size)
    sim_initial_score = magic_cube.objective_function()
    colorText("First state of magic cube:", LIME_GREEN)
    magic_cube.display()
    simulated_annealing = SimulatedAnnealing(magic_cube, initial_temp, final_temp, cooling_rate, threshold)
    sim_final_score, sim_duration, stuck_frequency, sim_iteration = simulated_annealing.run()
    colorText("\nState of magic cube after Simulated Annealing Algorithm:", LIME_GREEN)
    magic_cube.display()
    algorithms.append(
        {
            "algorithm": "Simulated Annealing Algorithm",
            "initial_score": sim_initial_score,
            "final_score": sim_final_score,
            "delta": sim_initial_score - sim_final_score,
            "duration": sim_duration,
            "iteration": sim_iteration,
            "stuck frequency": stuck_frequency
        }
    )

def run_comparison_algorithms():
    # Perbandingan tiap algoritma
    best_algorithm_delta = max(algorithms, key=lambda algo: algo["delta"])
    worst_algorithm_delta = min(algorithms, key=lambda algo: algo["delta"])
    fastest_algorithm_duration = min(algorithms, key=lambda algo: algo["duration"])
    slowest_algorithm_duration = max(algorithms, key=lambda algo: algo["duration"])

    separator("Algoritma dengan perkembangan paling besar")
    colorText(f"\n🔹 Algoritma: {best_algorithm_delta['algorithm']}", GOLDEN_YELLOW)
    colorText(f"   • Delta: {best_algorithm_delta['delta']}", ORANGE)
    colorText(f"   • Skor Final: {best_algorithm_delta['final_score']}", ORANGE)

    separator("Algoritma dengan perkembangan paling kecil")
    colorText(f"\n🔹 Algoritma: {worst_algorithm_delta['algorithm']}", GOLDEN_YELLOW)
    colorText(f"   • Delta: {worst_algorithm_delta['delta']}", ORANGE)
    colorText(f"   • Skor Final: {worst_algorithm_delta['final_score']}", ORANGE)

    separator("Algoritma dengan perkembangan paling cepat")
    colorText(f"\n🔹 Algoritma: {fastest_algorithm_duration['algorithm']}", GOLDEN_YELLOW)
    colorText(f"   • Durasi: {fastest_algorithm_duration['duration']:.4f} seconds", ORANGE)

    separator("Algoritma dengan perkembangan paling lambat")
    colorText(f"\n🔹 Algoritma: {slowest_algorithm_duration['algorithm']}", GOLDEN_YELLOW)
    colorText(f"   • Durasi: {slowest_algorithm_duration['duration']:.4f} seconds", ORANGE)

clear_screen()
colorText("Welcome to the Magic Cube Solver!\n", GOLDEN_YELLOW)
colorText("Pilihan algoritma yang tersedia:", TEAL)

algo_names = ["Steepest Hill Climbing", "Sideways Move Hill Climbing", "Stochastic Hill Climbing", "Random Restart Hill Climbing", "Genetic Algorithm", "Simulated Annealing"]
i = 1
for algon in algo_names:
    colorText(f"{i}. {algon}", LIME_GREEN)
    i += 1

colorText(f"{i}. Semua Algoritma (Tambahan Info Perbandingan)", LIME_GREEN)

choice = input(TEAL + "Masukkan algoritma yang ingin dicoba (1/2/3/6/7): " + RESET_COLOR)

# Pemilihan algoritma
if "1" in choice or "7" in choice:
    separator("Menjalankan Steepest Hill Climbing")
    run_steepest_hill_climbing()

if "2" in choice or "7" in choice:
    separator("Menjalankan Sideways Move Hill Climbing")
    run_sideways_move_hill_climbing()

if "3" in choice or "7" in choice:
    separator("Menjalankan Stochastic Hill Climbing")
    run_stochastic_hill_climbing()

if "4" in choice or "7" in choice:
    separator("Menjalankan Random Restart Hill Climbing")
    run_random_restart()

if "5" in choice or "7" in choice:
    separator("Menjalankan Genetic Algorithm")
    run_genetic_algorithm()

if "6" in choice or "7" in choice:
    separator("Menjalankan Simulated Annealing")
    run_simulated_annealing()

# Pemaparan informasi setiap algoritma
separator("Informasi Algoritma Terpilih")
for algo in algorithms:
    colorText(f"\n🔹 Algoritma: {algo['algorithm']}", GOLDEN_YELLOW)
    colorText(f"   • Skor inisial: {algo['initial_score']}", ORANGE)
    colorText(f"   • Skor final: {algo['final_score']}", ORANGE)
    colorText(f"   • Delta: {algo['delta']}", ORANGE)
    colorText(f"   • Durasi: {algo['duration']:.4f} seconds", ORANGE)
    if algo['algorithm'] == "Genetic Algorithm":
        colorText(f"   • Populasi: {algo['population']}", ORANGE)

    colorText(f"   • Iterasi: {algo['iteration']}", ORANGE)
    if algo['algorithm'] == "Sideways Move Hill Climbing":
        colorText(f"   • Iterasi sideways terbanyak: {algo['most_sideways_iteration']}", ORANGE)
    elif algo['algorithm'] == "Genetic Algorithm":
        colorText(f"   • Populasi: {algo['population']}", ORANGE)
    elif algo['algorithm'] == "Simulated Annealing":
        colorText(f"   • Stuck Frequency: {algo['stuck_frequency']}", ORANGE)

# Menampilkan informasi perbandingan jika 4 dipilih
if "7" in choice:
    run_comparison_algorithms()