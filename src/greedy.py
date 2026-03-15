import random
from tsp_utils import tour_length

def greedy_tsp(d):

    n = len(d)

    start = random.randint(0, n-1)

    unvisited = list(range(n))
    unvisited.remove(start)

    tour = [start]

    current = start

    while unvisited:

        next_city = min(unvisited, key=lambda x: d[current][x])

        tour.append(next_city)

        unvisited.remove(next_city)

        current = next_city

    return tour, tour_length(tour, d)
