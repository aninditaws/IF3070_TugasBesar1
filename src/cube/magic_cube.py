import random

class MagicCube:
    def __init__(self, size=5):
        self.size = size
        self.cube = [[[0 for _ in range(size)] for _ in range(size)] for _ in range(size)]
        self.initialize_random_state()

    def initialize_random_state(self):
        numbers = list(range(1, self.size ** 3 + 1))
        random.shuffle(numbers)
        
        index = 0
        for i in range(self.size):
            for j in range(self.size):
                for k in range(self.size):
                    self.cube[i][j][k] = numbers[index]
                    index += 1

    def display(self):
        for layer in range(self.size):
            print(f"Layer {layer + 1}:")
            for element in self.cube[layer]:
                print(" ".join(f"{num:3}" for num in element))
            print("\n" + "-" * 25 + "\n")


