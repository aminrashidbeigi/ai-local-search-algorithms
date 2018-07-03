import random

class HillClimbing(object):

    def __init__(self, problem, type='greedy'):
        self.problem = problem
        self.type = type
        self.problem_solver(problem.initial_state())

    def problem_solver(self, initial_state):
        number_of_expanded_nodes = 0
        number_of_visited_nodes = 0
        best_state_found = False
        current_state = initial_state
        last_state = initial_state
        number_of_attempts = 5
        attempts = 0
        while not best_state_found:
            number_of_expanded_nodes = number_of_expanded_nodes + 1
            neighbors = self.problem.successor(current_state)
            number_of_visited_nodes = number_of_visited_nodes + len(neighbors)
            if self.type is 'greedy':
                current_state = self.find_neighbor_in_greedy_way(current_state, neighbors)
                best_state_found = True if last_state == current_state else False
            elif self.type is 'stochastic':
                current_state = self.find_neighbor_in_stochastic_way(current_state, neighbors)
                best_state_found = True if last_state == current_state else False
            elif self.type is 'random_restart':
                current_state = self.find_neighbor_in_greedy_way(current_state, neighbors)
                if last_state == current_state:
                    if attempts < number_of_attempts:
                        best_state_found = True
                    attempts = attempts + 1
            elif self.type is 'first_choice':
                current_state = self.find_neighbor_in_first_choice_way(current_state, neighbors)
                best_state_found = True if last_state == current_state else False
            if self.problem.heuristic(current_state) == 0:
                best_state_found = True
            last_state = current_state
        print("Type of hill climbing: " + str(self.type))
        print("Last state: " + str(current_state))
        print("Number of visited nodes: " + str(number_of_visited_nodes))
        print("Number of expanded nodes: " + str(number_of_expanded_nodes))

    def find_neighbor_in_greedy_way(self, current_state, neighbors):
        best_neighbor = current_state
        best_heuristic = self.problem.heuristic(current_state)
        for neighbor in neighbors:
            heuristic = self.problem.heuristic(neighbor)
            if heuristic < best_heuristic:
                best_heuristic = heuristic
                best_neighbor = neighbor
        return best_neighbor

    def find_neighbor_in_stochastic_way(self, current_state, neighbors):
        valuable_neighbors = []
        for neighbor in neighbors:
            if self.problem.heuristic(neighbor) < self.problem.heuristic(current_state):
                valuable_neighbors.append(neighbor)
        return random.choice(valuable_neighbors) if len(valuable_neighbors) > 0 else current_state

    def find_neighbor_in_first_choice_way(self, current_state, neighbors):
        best_heuristic = self.problem.heuristic(current_state)
        for neighbor in neighbors:
            heuristic = self.problem.heuristic(neighbor)
            if heuristic < best_heuristic:
                return neighbor
        return current_state
