import random
import math
import time
import matplotlib.pyplot as plt


class SimulatedAnnealing:
    def __init__(self, cube, initial_temperature=1000, final_temperature=0.1, cooling_rate=0.99, threshold=0.5):
        """
        Menginisialisasi algoritma Simulated Annealing dengan parameter yang diberikan.

        Parameters:
        - cube: Objek MagicCube yang akan dioptimalkan
        - initial_temperature: Suhu awal untuk memulai proses
        - final_temperature: Suhu akhir yang menentukan kapan algoritma berhenti
        - cooling_rate: Laju penurunan suhu per iterasi
        - threshold: batas probabilitas penerimaan solusi yang lebih buruk
        """
        self.cube = cube
        self.initial_temperature = initial_temperature
        self.final_temperature = final_temperature
        self.cooling_rate = cooling_rate
        self.threshold = threshold
        self.scores = []
        self.acceptance_probability = []
        self.stuck_frequency = 0

    def swap_elements(self, pos1, pos2):
        """
        Menukar dua elemen pada posisi 1 dan 2 dalam kubus.

        Parameters:
        - pos1, pos2: Posisi dari elemen yang akan ditukar dalam bentuk koordinat (x, y, z)
        """
        x1, y1, z1 = pos1
        x2, y2, z2 = pos2
        self.cube.cube[x1][y1][z1], self.cube.cube[x2][y2][z2] = self.cube.cube[x2][y2][z2], self.cube.cube[x1][y1][z1]

    def find_random_neighbor(self):
        """
        Menemukan tetangga acak dengan menukar dua elemen dalam kubus secara acak.

        Returns:
        - pos1, pos2: Posisi elemen yang ditukar
        """
        pos1 = (random.randint(0, self.cube.size - 1), random.randint(0, self.cube.size - 1),
                random.randint(0, self.cube.size - 1))
        pos2 = (random.randint(0, self.cube.size - 1), random.randint(0, self.cube.size - 1),
                random.randint(0, self.cube.size - 1))
        while pos1 == pos2:
            pos2 = (random.randint(0, self.cube.size - 1), random.randint(0, self.cube.size - 1),
                    random.randint(0, self.cube.size - 1))  # Memastikan dua posisi yang dipilih berbeda

        # Menukar elemen di kedua posisi tersebut
        self.swap_elements(pos1, pos2)
        return pos1, pos2

    def run(self):
        start_time = time.perf_counter()
        temperature = self.initial_temperature
        self.best_score = self.cube.objective_function()
        current_value = self.best_score

        iteration = 0

        # List untuk menyimpan probabilitas penerimaan solusi buruk
        acc_probability_list = []

        # Berhenti saat temperature mencapai final_temperature
        while temperature > self.final_temperature:
            pos1, pos2 = self.find_random_neighbor()
            neighbor_value = self.cube.objective_function()
            delta = current_value - neighbor_value

            # Jika solusi baru lebih buruk
            if delta < 0:
                acceptance_probability = math.exp(delta / temperature)  # Hitung probabilitas penerimaan solusi buruk
                acc_probability_list.append(acceptance_probability)

                # Menerima solusi buruk jika probabilitasnya lebih besar dari threshold
                if self.threshold < acceptance_probability:
                    current_value = neighbor_value

                # Solusi yang buruk tidak diambil jika probabilitasnya tidak lebih besar dari threshold
                else:
                    self.swap_elements(pos1,
                                       pos2)  # Menukar kembali kedua elemen di posisi tersebut: posisi elemen tidak jadi berubah
                    self.stuck_frequency += 1  # Jumlah stuck di local optima bertambah

            # Jika solusi baru lebih baik, maka langsung diterima tanpa syarat
            else:
                current_value = neighbor_value
                acc_probability_list.append(1)  # Probabilitas penerimaannya adalah 1

            self.scores.append(current_value)

            # Suhu berkurang berdasarkan cooling_rate
            temperature *= self.cooling_rate
            iteration += 1

        # Memperbarui best_score dengan nilai solusi saat ini jika solusi ini lebih baik daripada yang sebelumnya
        self.best_score = current_value

        end_time = time.perf_counter()
        duration = end_time - start_time

        # Plot perkembangan nilai objective function
        plt.figure(figsize=(10, 6))
        plt.plot(self.scores, label="Objective Function Value", alpha=0.5)
        plt.xlabel("Iteration")
        plt.ylabel("Objective Function")
        plt.title("Objective Function")
        plt.legend()
        plt.show()

        # Plot probabilitas penerimaan solusi buruk
        plt.figure(figsize=(10, 6))
        plt.plot(acc_probability_list, label="Acceptance Probability", alpha=0.5)
        plt.xlabel("Iterations")
        plt.ylabel("Acceptance Probability")
        plt.title("Acceptance Probability Over Iterations")
        plt.legend(loc="upper right")  # Memindahkan legend ke ujung kanan atas
        plt.show()

        return self.best_score, duration, self.stuck_frequency, iteration
