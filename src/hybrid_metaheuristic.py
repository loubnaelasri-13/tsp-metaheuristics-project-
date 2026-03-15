from greedy import nearest_neighbor
from threshold_accepting import threshold_accepting
from simulated_annealing import simulated_annealing

def hybrid_solver(D):
    s0 = nearest_neighbor(D)
    s1 = threshold_accepting(D, s0)
    s2 = simulated_annealing(D, s1)
    return s2
