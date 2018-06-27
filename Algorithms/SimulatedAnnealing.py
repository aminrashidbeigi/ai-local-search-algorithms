import random
import math


class SimulatedAnnealing(object):

    def __init__(self, problem):
        self.problem = problem
        self.problem_solver(problem.initial_state())

    def problem_solver(self, initial_state):
        current_state = initial_state
        initial_temperature = 10000
        current_temperature = initial_temperature
        while current_temperature > 1:
            neighbors = self.problem.successor(current_state)
            chosen_neighbor = random.choice(neighbors)
            efficiency = self.problem.heuristic(chosen_neighbor) - self.problem.heuristic(current_state)
            if efficiency >= 0:
                current_state = chosen_neighbor
            else:
                if math.exp(efficiency/current_temperature) > random.random():
                    print(math.exp(efficiency/current_temperature))
                    current_state = chosen_neighbor
            # 1
            # current_temperature = current_temperature - 1
            # 2
            # current_temperature = current_temperature * 0.99
            # 3
            # current_temperature = math.sqrt(current_temperature)

        print(current_state)
