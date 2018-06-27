from Algorithms.SimulatedAnnealing import *
from copy import deepcopy
import random

table = [
    ['a', 'p', 't'],
    ['m', 'l', 'b'],
    ['k', 'l', 'o'],
    ['u', 'o', 'c']
]

# table = [
#     ['c', 'o', 'o'],
#     ['a', 't', 'l'],
#     ['l', 'm', 'b'],
#     ['k', 'u', 'p']
# ]

words = ["go", "cool", "cat", "talk"]


class Problem(object):

    def __init__(self, table, words):
        self.table = table
        self.words = words

    def initial_state(self):
        return table

    def heuristic(self, table):
        def word_score_in_table(table, word, position, index):
            score_of_word = 0
            if index == len(word) - 1:
                return 1
            elif position[0] > 0 and table[position[0] - 1][position[1]] == word[index]:
                score_of_word = score_of_word + word_score_in_table(table, word, [position[0] - 1, position[1]], index + 1)
            elif position[0] < len(table) - 1 and table[position[0] + 1][position[1]] == word[index]:
                score_of_word = score_of_word + word_score_in_table(table, word, [position[0] + 1, position[1]], index + 1)
            elif position[1] > 0 and table[position[0]][position[1] - 1] == word[index]:
                score_of_word = score_of_word + word_score_in_table(table, word, [position[0], position[1] - 1], index + 1)
            elif position[1] < len(table[0]) - 1 and table[position[0]][position[1] + 1] == word[index]:
                score_of_word = score_of_word + word_score_in_table(table, word, [position[0], position[1] + 1], index + 1)
            return score_of_word

        score = 0
        for word in words:
            for row in table:
                for col in row:
                    if list(word)[0] == col:
                        score = score + word_score_in_table(table, word, [table.index(row), row.index(col)], 1)
        # print(score)
        return score

    def successor(self, state):
        neighbors = []
        rows_number = list(range(len(state)))
        cols_number = list(range(len(state[0])))
        for i in range(0,10):
            temp_state = deepcopy(state)
            random_row1 = random.choice(rows_number)
            random_row2 = random.choice(rows_number)
            random_col1 = random.choice(cols_number)
            random_col2 = random.choice(cols_number)
            temp_state[random_row1][random_col1], temp_state[random_row2][random_col2] = state[random_row2][random_col2], state[random_row1][random_col1]
            neighbors.append(temp_state)
        return neighbors


p = Problem(table, words)
sa = SimulatedAnnealing(p)
