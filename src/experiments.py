import pandas as pd
from tsp_utils import read_instance
from greedy import greedy_tsp
from threshold_accepting import threshold_accepting
from simulated_annealing import simulated_annealing
from hybrid_sa_2opt import hybrid_sa_2opt

instances = [
    "../data/instance_29.txt",
    "../data/instance_51.txt"
]

results = []

for inst in instances:

    d = read_instance(inst)

    g = greedy_tsp(d)[1]
    ta = threshold_accepting(d)[1]
    sa = simulated_annealing(d)[1]
    hybrid = hybrid_sa_2opt(d)[1]

    results.append([inst, g, ta, sa, hybrid])

df = pd.DataFrame(results,
                  columns=["Instance", "Greedy", "TA", "SA", "Hybrid"])

print(df)

df.to_csv("../results/results_table.csv", index=False)
