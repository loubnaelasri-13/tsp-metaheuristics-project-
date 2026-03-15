import numpy as np
import random

def read_instance(filename):
    with open(filename, 'r') as f:
        text = f.read()

    start = text.find("[[")
    end = text.rfind("]]") + 2
    matrix_str = text[start:end]

    d = np.array(eval(matrix_str))

    return d


def tour_length(tour, d):

    n = len(tour)
    cost = 0

    for i in range(n):
        cost += d[tour[i]][tour[(i+1) % n]]

    return cost


def swap_neighbor(tour):

    i, j = random.sample(range(len(tour)), 2)
    new_tour = tour.copy()

    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]

    return new_tour
