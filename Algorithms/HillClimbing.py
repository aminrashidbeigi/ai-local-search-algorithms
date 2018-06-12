class HillClimbing(object):

    def __init__(self, problem, type='greedy'):
        self.problem = problem
        self.type = type
        self.problem_solver(problem, type)

    def problem_solver(self, initial_state, type):

        best_state_found = False
        current_state = initial_state
        while not best_state_found:
            neighbors = self.problem.get_neighbors(current_state)
            if type is 'greedy':
                current_state = self.find_best_neighbor(neighbors)
            if(self.problem.is_best_state(current_state)):
                best_state_found = True

    def find_best_neighbor(self, neighbors):
        best_neighbor = None
        return best_neighbor
