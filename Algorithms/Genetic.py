import random
import math


class Genetic(object):

    def __init__(self, problem):
        self.problem = problem
        self.problem_solver(problem.initial_state())

    def problem_solver(self, initial_state):
        current_state = initial_state
