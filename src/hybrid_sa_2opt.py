from simulated_annealing import simulated_annealing
from tsp_utils import tour_length

def two_opt(tour, d):

    best = tour
    improved = True

    while improved:

        improved = False

        for i in range(1, len(tour)-2):

            for j in range(i+1, len(tour)):

                if j-i == 1:
                    continue

                new_tour = tour[:]
                new_tour[i:j] = tour[j-1:i-1:-1]

                if tour_length(new_tour, d) < tour_length(best, d):

                    best = new_tour
                    improved = True

        tour = best

    return best


def hybrid_sa_2opt(d):

    tour, cost = simulated_annealing(d)

    improved = two_opt(tour, d)

    return improved, tour_length(improved, d)
