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
        print(single_score + pair_score)
        return single_score + pair_score



common_chars = ['a', 'i', 'n', 'o', 's', 'h', 'r']
common_char_pairs = ['th', 'er', 'on', 'an', 're', 'he', 'in', 'ed']

p = Problem(common_chars, common_char_pairs)
p.heuristic(p.initial_population())