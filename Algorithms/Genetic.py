import random
import math
from copy import deepcopy


class Genetic(object):

    def __init__(self, problem, population_size):
        self.problem = problem
        self.population_size = population_size
        self.problem_solver(population_size)

    def problem_solver(self, population_size):
        current_population = [self.problem.initial_state() for i in range(0, population_size)]
        current_evaluation = [self.problem.heuristic(member) for member in current_population]
        attempts = 1000

        while attempts > 0:
            sorted_population = [x for _, x in sorted(zip(current_evaluation, current_population))]
            print("Best evaluation: " + str(max(current_evaluation)))
            print("Worst evaluation: " + str(min(current_evaluation)))
            print("Avg evaluation: " + str(sum(current_evaluation) / len(current_evaluation)))
            new_population = []
            for i in range(0, population_size):
                if i % 2 == 1:
                    crossover_states = self.problem.crossover(sorted_population[i], sorted_population[i-1])
                    new_population.append(crossover_states[0])
                    new_population.append(crossover_states[1])
            random_index_to_mutation = random.randint(0, 9)
            new_population[random_index_to_mutation] = self.problem.mutation(new_population[random_index_to_mutation])
            current_population = deepcopy(new_population)
            current_evaluation = [self.problem.heuristic(member) for member in current_population]

            attempts = attempts - 1
