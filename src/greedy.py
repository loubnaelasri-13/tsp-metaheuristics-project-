import numpy as np

def nearest_neighbor(D, start=None):

    n = len(D)
    
    if start is None:
        start = np.random.randint(n)
    
    visited = [start]
    current = start
    
    while len(visited) < n:
        distances = D[current]
        
        # trouver la ville non visitée la plus proche
        nearest = None
        best_dist = float('inf')
        for j in range(n):
            if j not in visited and distances[j] < best_dist:
                nearest = j
                best_dist = distances[j]
        
        visited.append(nearest)
        current = nearest
    
    return visited
