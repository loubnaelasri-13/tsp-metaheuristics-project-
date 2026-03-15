import numpy as np
from tsp_utils import tour_length, swap_neighbor

def simulated_annealing(D, init_tour, T0=100, Tmin=0.1, alpha=0.95, iter_per_T=500):
    current = init_tour
    current_cost = tour_length(current, D)
    best = current
    best_cost = current_cost
    T = T0
    while T > Tmin:
        for _ in range(iter_per_T):
            neighbor = swap_neighbor(current)
            cost = tour_length(neighbor, D)
            d = cost - current_cost
            if d < 0 or np.random.rand() < np.exp(-d/T):
                current = neighbor
                current_cost = cost
                if cost < best_cost:
                    best = neighbor
                    best_cost = cost
        T *= alpha
    return best
