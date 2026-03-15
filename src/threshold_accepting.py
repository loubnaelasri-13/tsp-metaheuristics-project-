import random
from tsp_utils import swap_neighbor, tour_length

def threshold_accepting(d, S0=100, Smin=1, alpha=0.95, iterations=1000):

    n = len(d)

    x = list(range(n))
    random.shuffle(x)

    S = S0

    best = x
    best_cost = tour_length(x, d)

    while S > Smin:

        for _ in range(iterations):

            x_new = swap_neighbor(x)

            diff = tour_length(x_new, d) - tour_length(x, d)

            if diff <= S:

                x = x_new

                if tour_length(x, d) < best_cost:
                    best = x
                    best_cost = tour_length(x, d)

        S *= alpha

    return best, best_cost
