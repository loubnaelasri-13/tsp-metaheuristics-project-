import numpy as np

def tour_length(tour, D):

    n = len(tour)
    length = 0
    for i in range(n-1):
        length += D[tour[i]][tour[i+1]]
    length += D[tour[-1]][tour[0]]  # retour à la ville de départ
    return length

def swap_neighbor(tour):
    
    i, j = np.random.choice(len(tour), 2, replace=False)
    new_tour = tour.copy()
    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
    return new_tour
