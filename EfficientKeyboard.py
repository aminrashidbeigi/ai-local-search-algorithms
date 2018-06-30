from Algorithms.Genetic import *
from copy import deepcopy
import string
import random
import math

class Problem(object):

    def __init__(self, common_chars, common_char_pairs):
        self.common_chars = common_chars
        self.common_char_pairs = common_char_pairs

    def initial_population(self):
        keyboard = []
        alphabet = list(string.ascii_lowercase)
        for i in range(0, 3):
            temp = []
            for j in range(0, 10):
                if i == 0:
                    temp.append(alphabet.pop(alphabet.index(random.choice(alphabet))))
                else:
                    if j == 0 or j == 9:
                        temp.append('-')
                    else:
                        temp.append(alphabet.pop(alphabet.index(random.choice(alphabet))))
            keyboard.append(deepcopy(temp))
        return keyboard

    def heuristic(self, keyboard):
        left_single_char = 0
        right_single_char = 0
        score = 0
        single_score = 0
        pair_score = 0
        for row in keyboard:
            for col in row:
                for key in common_chars:
                    if col == key and row.index(col) < 5:
                        left_single_char = left_single_char + 1
                    elif col == key:
                        right_single_char = right_single_char + 1
        single_score = single_score + 9 - abs(right_single_char - left_single_char)

        score = single_score + pair_score
        return score

    def successor(self, current_state):
        all_neighbors = self.find_all_neighbors()
        num_of_neighbors = {}
        neighbors = []
        for i in current_state:
            num_of_neighbors[i] = 0
        for neighbor in all_neighbors:
            if current_state[neighbor[0]] == current_state[neighbor[1]]:
                num_of_neighbors[neighbor[0]] = num_of_neighbors[neighbor[0]] + 1
                num_of_neighbors[neighbor[1]] = num_of_neighbors[neighbor[1]] + 1
        worst_node = max(num_of_neighbors, key=num_of_neighbors.get)
        for i in range(1, self.number_of_colors + 1):
            temp_state = deepcopy(current_state)
            if temp_state[worst_node] != i:
                temp_state[worst_node] = i
                neighbors.append(temp_state)
        return neighbors

    def find_all_neighbors(self):
        all_neighbors = []
        for i in self.graph:
            for j in graph[i]:
                all_neighbors.append((i, j))
        return all_neighbors


common_chars = ['a', 'i', 'n', 'o', 's', 'h', 'r']
common_char_pairs = ['th', 'er', 'on', 'an', 're', 'he', 'in', 'ed']

p = Problem(common_chars, common_char_pairs)
p.heuristic(p.initial_population())