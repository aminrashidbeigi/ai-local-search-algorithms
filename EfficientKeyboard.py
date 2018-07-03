from Algorithms.Genetic import *
from copy import deepcopy
import string
import random


class Problem(object):

    def __init__(self, common_chars, common_char_pairs):
        self.common_chars = common_chars
        self.common_char_pairs = common_char_pairs

    def initial_state(self):
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
        left_pair_char = 0
        right_pair_char = 0
        single_score = 0
        pair_score = 0
        for i in range(0, 3):
            for j in range(0, 10):
                for key in common_chars:
                    if keyboard[i][j] == key and j < 5:
                        left_single_char = left_single_char + 1
                    elif keyboard[i][j] == key:
                        right_single_char = right_single_char + 1
                for key in common_char_pairs:
                    key = list(key)
                    if keyboard[i][j] == key[0]:
                        if i > 0 and keyboard[i - 1][j] == key[1] and j < 5:
                            left_pair_char = left_pair_char + 1
                        elif i > 0 and keyboard[i - 1][j] == key[1] and j > 5:
                            right_pair_char = right_pair_char + 1
                        if i < 2 and keyboard[i + 1][j] == key[1] and j < 5:
                            left_pair_char = left_pair_char + 1
                        elif i < 2 and keyboard[i + 1][j] == key[1] and j > 5:
                            right_pair_char = right_pair_char + 1
                        if j > 0 and keyboard[i][j - 1] == key[1] and j < 5:
                            left_pair_char = left_pair_char + 1
                        elif j < 9 and keyboard[i][j - 1] == key[1] and j > 5:
                            right_pair_char = right_pair_char + 1

        single_score = single_score + 9 - abs(right_single_char - left_single_char)
        pair_score = pair_score + 8 - abs(right_single_char - left_single_char)
        return single_score + pair_score

    def crossover(self, population1, population2):
        linear_population1 = []
        linear_population2 = []

        for i in range(0, len(population1)):
            for j in range(0, len(population1[1])):
                if population1[i][j] != '-':
                    linear_population1.append(population1[i][j])
                    linear_population2.append(population2[i][j])

        new_population1 = deepcopy(linear_population1)
        new_population2 = deepcopy(linear_population2)
        new_population1[4:23], new_population2[4:23] = linear_population2[4:23], linear_population1[4:23]
        temp_list1 = []
        for i in range(0, 26):
            i = (i + 4) % 26
            if new_population1[i] not in temp_list1:
                temp_list1.append(new_population1[i])
            else:
                for j in range(0, 26):
                    j = (j + 23) % 26
                    if new_population2[j] not in new_population1:
                        new_population1[i] = new_population2[j]
                        temp_list1.append(new_population1[i])
        temp_list2 = []
        for i in range(0, 26):
            i = (i + 4) % 26
            if new_population2[i] not in temp_list2:
                temp_list2.append(new_population2[i])
            else:
                for j in range(0, 26):
                    j = (j + 23) % 26
                    if new_population1[j] not in new_population2:
                        new_population2[i] = new_population1[j]
                        temp_list2.append(new_population2[i])

        new_population1_correct_format = deepcopy(population1)
        new_population2_correct_format = deepcopy(population2)
        row = 0
        col = 0
        for i in range(0, 26):
            if i < 10:
                new_population1_correct_format[row][col] = new_population1[i]
                new_population2_correct_format[row][col] = new_population2[i]
            else:
                if col == 0:
                    row = row + 1
                    new_population1_correct_format[row][col] = '-'
                    new_population2_correct_format[row][col] = '-'
                else:
                    new_population1_correct_format[row][col] = new_population1[i]
                    new_population2_correct_format[row][col] = new_population2[i]
            col = (col + 1) % 10
        return [new_population1_correct_format, new_population2_correct_format]

    def mutation(self, keyboard):
        not_dash = False
        while not not_dash:
            i1 = keyboard.index(random.choice(keyboard))
            j1 = keyboard[i1].index(random.choice(keyboard[i1]))
            i2 = keyboard.index(random.choice(keyboard))
            j2 = keyboard[i2].index(random.choice(keyboard[i2]))
            if keyboard[i1][j1] != '-' and keyboard[i2][j2] != '-':
                keyboard[i1][j1], keyboard[i2][j2] = keyboard[i2][j2], keyboard[i1][j1]
                not_dash = True
        return keyboard

    def is_goal(self, keyboard):
        return self.heuristic(keyboard) == 15


common_chars = ['a', 'i', 'n', 'o', 's', 'h', 'r']
common_char_pairs = ['th', 'er', 'on', 'an', 're', 'he', 'in', 'ed']

p = Problem(common_chars, common_char_pairs)
g = Genetic(p, 10)
