import random
import time
import matplotlib.pyplot as plt
from cube.magic_cube import MagicCube
#Class untuk Random Restart Hill Climbing
class RandomRestartHillClimbing:
    #Memulai tahap inisialisasi
    def __init__(self, cube, max_restarts, max_iterations_per_restart):
        self.cube = cube 
        self.max_restarts = max_restarts
        self.max_iterations_per_restart = max_iterations_per_restart
        self.scores = [] #menyimpan objective score setiap iterasi
    
    #Fungsi untuk melakukan pengacakan posisi elemen dalam cube
    def randomize_cube(self):
        
        number_swaps = self.cube.size ** 3   #swap berdasarkan bentuk -> pangkat 3 karena cube
        for i in range(number_swaps):
            pos1 = (
                random.randint(0, self.cube.size - 1),
                random.randint(0, self.cube.size - 1),
                random.randint(0, self.cube.size - 1)
            )
            pos2 = (
                random.randint(0, self.cube.size - 1),
                random.randint(0, self.cube.size - 1),
                random.randint(0, self.cube.size - 1)
            )
            
            self.swap_elements(pos1, pos2)
    
    #Fungsi untuk menukar elemen di dua posisi dalam cube
    def swap_elements(self, pos1, pos2):
        x1, y1, z1 = pos1
        x2, y2, z2 = pos2
        self.cube.cube[x1][y1][z1], self.cube.cube[x2][y2][z2] = self.cube.cube[x2][y2][z2], self.cube.cube[x1][y1][z1]
    
    #Fungsi untuk mencari neighbor terbaik
    def find_best_neighbor(self):
    
        delta = 0 
        best_delta = 0  
        best_positions = 0 
        #Semua posisi dalam kubus
        positions = [(x, y, z) for x in range(self.cube.size) for y in range(self.cube.size) for z in range(self.cube.size)]
        random.shuffle(positions)  

        current_score = self.cube.objective_function() #Menetapkan nilai objektif awal
        for pos1 in positions:
            for pos2 in positions:
                if pos2 > pos1:
                    self.swap_elements(pos1, pos2)
                    new_score = self.cube.objective_function() #Menghitung nilai objektif baru
                    delta = current_score - new_score #Perubahan nilai

                    if delta > best_delta: #Melakukan pemeriksaan apakah perubahan lebih baik / terbaik
                        best_delta = delta
                        best_positions = (pos1, pos2)

                    self.swap_elements(pos1, pos2) 

        return best_positions, best_delta
    #Fungsi Steepest Hill Climbing 
    def run_steepest_hill_climbing(self, max_iterations):
        iteration = 0
        last_best_delta = 0
        best_score = self.cube.objective_function()
        scores = []
        print(f"Initial score: {best_score}")

        while iteration < max_iterations:
            best_positions, best_delta = self.find_best_neighbor()

            
            if best_delta == last_best_delta: #Jika tidak ada peningkatan / perbaikan, maka proses dihentikan
                break

            self.swap_elements(*best_positions)
            best_score -= best_delta #Melakukan update untuk skor terbaik
            iteration += 1
            scores.append(best_score)
            print(f"Iteration {iteration}, New score: {best_score}")

        final_score = self.cube.objective_function()
        print(f"Final score after hill climbing: {final_score}")
        return final_score, iteration, scores
    #Fungsi Random Restart Hill Climbing
    def run(self):
        start_time = time.perf_counter() #Pencatatan waktu
        best_solution_score = 0 #Inisialisasi skor terbaik
        total_iterations = 0 #Inisialisasi total iterasi
        number_restart = 0 #Perhitungan terhadap restart
            
        while number_restart < self.max_restarts:
            print(f"\n=== Restart {number_restart + 1} ===")
            obj_scores = [] #Nilai objektif akan dicatat setiap dilakukan restart

            #Melakukan pengacakan untuk setiap restart 
            self.randomize_cube()
            randomized_score = self.cube.objective_function()
            print(f"Score after randomization: {randomized_score}")
            #Memanggil dan menjalankan fungsi steepest hill climbing setiap restart dilakukan
            final_score, iteration, obj_scores = self.run_steepest_hill_climbing(self.max_iterations_per_restart)

            for i in range(len(obj_scores)):
                self.scores.append(obj_scores[i]) #Menyimpan skor ke self.scores untuk plotting
            
            #Update nilai skor terbaik
            if final_score < best_solution_score:
                best_solution_score = final_score

            total_iterations += iteration #Menambahkan iterasi ke total iterasi
            number_restart += 1  #Menambah jumlah restart

            print(f"Objective score after restart {number_restart}: {final_score}")
            plt.close() #Menutup plot yang sebelumnya terbuka 

        end_time = time.perf_counter()
        overall_duration = end_time - start_time 

        self.plot_scores(total_iterations)
        return best_solution_score, overall_duration, total_iterations
    
    #Fungsi untuk plotting
    def plot_scores(self,iteration):
        plt.figure(figsize=(10, 6))
        plt.plot(range(len(self.scores)), self.scores, marker='o', color='b', label="Objective Score")
        plt.xticks(range(0, iteration + 1, 10))
        plt.title("Random Restart Hill-Climbing Progression")
        plt.xlabel("Iteration")
        plt.ylabel("Objective Score")
        plt.legend()
        plt.grid(True)
        plt.show()

