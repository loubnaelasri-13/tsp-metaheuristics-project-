import pandas as pd
import matplotlib.pyplot as plt
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

df.to_csv("../results/tables/results_table.csv", index=False)

for i in range(len(df)):
    instance = df.loc[i, "Instance"]
    values = df.loc[i, ["Greedy", "TA", "SA", "Hybrid"]]

    plt.figure()
    plt.bar(["Greedy", "TA", "SA", "Hybrid"], values)
    plt.title("Comparaison des méthodes - " + instance)
    plt.ylabel("Distance")

    name = instance.split("/")[-1].replace(".txt", "")
    plt.savefig("../results/figures/" + name + "_comparison.png")
    plt.close()
