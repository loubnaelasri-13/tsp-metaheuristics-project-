import random
import math
from tsp_utils import swap_neighbor, tour_length

def simulated_annealing(d, T0=1000, Tmin=0.1, alpha=0.995):

    n = len(d)

    x = list(range(n))
    random.shuffle(x)

    best = x
    best_cost = tour_length(x, d)

    T = T0

    while T > Tmin:

        x_new = swap_neighbor(x)

        diff = tour_length(x_new, d) - tour_length(x, d)

        if diff < 0 or random.random() < math.exp(-diff / T):

            x = x_new

            if tour_length(x, d) < best_cost:

                best = x
                best_cost = tour_length(x, d)

        T *= alpha

    return best, best_cost
