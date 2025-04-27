import random

class Individual:
    def __init__(self, k):
        self.genes = [random.randint(0, 9) for _ in range(k)]
        self.fitness = 0
        self.calculate_fitness()

    def calculate_fitness(self, target_sum=None):
        if target_sum is not None:
            self.fitness = -abs(sum(self.genes) - target_sum)

class Population:
    def __init__(self, size, k, target_sum):
        self.individuals = [Individual(k) for _ in range(size)]
        self.target_sum = target_sum
        self.fittest = None
        self.calculate_fitness()

    def calculate_fitness(self):
        for individual in self.individuals:
            individual.calculate_fitness(self.target_sum)
        self.fittest = max(self.individuals, key=lambda ind: ind.fitness)

    def get_second_fittest(self):
        sorted_individuals = sorted(self.individuals, key=lambda ind: ind.fitness, reverse=True)
        return sorted_individuals[1]

    def get_least_fittest_index(self):
        min_fit = min(self.individuals, key=lambda ind: ind.fitness)
        return self.individuals.index(min_fit)

class GeneticAlgorithm:
    def __init__(self, target_sum, k, population_size=10):
        self.target_sum = target_sum
        self.k = k
        self.population = Population(population_size, k, target_sum)
        self.generation = 0

    def selection(self):
        self.fittest = self.population.fittest
        self.second_fittest = self.population.get_second_fittest()

    def crossover(self):
        crossover_point = random.randint(1, self.k - 1)
        for i in range(crossover_point):
            self.fittest.genes[i], self.second_fittest.genes[i] = self.second_fittest.genes[i], self.fittest.genes[i]

    def mutation(self):
        mutation_point = random.randint(0, self.k - 1)
        self.fittest.genes[mutation_point] = random.randint(0, 9)

        mutation_point = random.randint(0, self.k - 1)
        self.second_fittest.genes[mutation_point] = random.randint(0, 9)

    def add_fittest_offspring(self):
        self.fittest.calculate_fitness(self.target_sum)
        self.second_fittest.calculate_fitness(self.target_sum)

        offspring = self.fittest if self.fittest.fitness > self.second_fittest.fitness else self.second_fittest
        least_fit_index = self.population.get_least_fittest_index()
        self.population.individuals[least_fit_index] = offspring

    def evolve(self):
        while abs(self.population.fittest.fitness) != 0:
            self.generation += 1
            self.selection()
            self.crossover()
            if random.random() < 0.5:  
                self.mutation()
            self.add_fittest_offspring()
            self.population.calculate_fitness()

        return self.population.fittest.genes

def main():
    T = int(input("Enter the value of T: "))
    k = int(input("Enter the value of k: "))
    
    ga = GeneticAlgorithm(T, k)
    solution = ga.evolve()
    print("Output:")
    print(" ".join(map(str, solution)))

if __name__ == "__main__":
    main()
