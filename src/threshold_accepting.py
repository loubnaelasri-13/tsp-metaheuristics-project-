import numpy as np
from tsp_utils import tour_length, swap_neighbor

def threshold_accepting(D, init_tour, S0=50, Smin=0.1, alpha=0.95, iter_per_S=500):
    current = init_tour
    current_cost = tour_length(current, D)
    S = S0
    while S > Smin:
        for _ in range(iter_per_S):
            neighbor = swap_neighbor(current)
            cost = tour_length(neighbor, D)
            if cost - current_cost <= S:
                current = neighbor
                current_cost = cost
        S *= alpha
    return current
