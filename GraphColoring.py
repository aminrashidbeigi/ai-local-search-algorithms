from Algorithms.HillClimbing import *
from copy import deepcopy

graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': [],
    'E': ['F'],
    'F': ['C']
}


class Problem(object):

    def __init__(self, graph, number_of_colors=3):
        self.graph = graph
        self.number_of_colors = number_of_colors

    def initial_state(self):
        node_colors = {}
        for g in self.graph:
            node_colors[g] = 1
        return node_colors

    def heuristic(self, node_colors):
        score = 0
        all_neighbors = self.find_all_neighbors()
        for i in all_neighbors:
            if node_colors[i[0]] == node_colors[i[1]]:
                score = score + 1
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


p = Problem(graph, 3)
hc = HillClimbing(p, 'first_choice')
