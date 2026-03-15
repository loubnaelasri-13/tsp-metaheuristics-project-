import time
import pandas as pd
import matplotlib.pyplot as plt
from reader import read_instance
from greedy import nearest_neighbor
from threshold_accepting import threshold_accepting
from simulated_annealing import simulated_annealing
from hybrid_metaheuristic import hybrid_solver
from tsp_utils import tour_length

def run_experiment(instance_file):
    D = read_instance(instance_file)
    results = []

    start = time.time()
    s = nearest_neighbor(D)
    results.append(["Greedy", tour_length(s,D), round(time.time()-start,3)])

    start = time.time()
    s = threshold_accepting(D, s)
    results.append(["Threshold Accepting", tour_length(s,D), round(time.time()-start,3)])

    start = time.time()
    s = simulated_annealing(D, s)
    results.append(["Simulated Annealing", tour_length(s,D), round(time.time()-start,3)])

    start = time.time()
    s = hybrid_solver(D)
    results.append(["Hybrid", tour_length(s,D), round(time.time()-start,3)])

    df = pd.DataFrame(results, columns=["Méthode", "Distance", "Temps (s)"])
    return df

def save_results(df, instance_name):
    table_file = f"results/tables/{instance_name}_results.csv"
    df.to_csv(table_file, index=False)

    plt.figure(figsize=(6,4))
    plt.bar(df["Méthode"], df["Distance"], color=["skyblue","orange","green","red"])
    plt.ylabel("Distance")
    plt.title(f"Comparaison des métaheuristiques - {instance_name}")
    figure_file = f"results/figures/{instance_name}_comparison.png"
    plt.savefig(figure_file)
    plt.close()

if __name__ == "__main__":
    for instance_path in ["data/instance_29.txt", "data/instance_51.txt"]:
        instance_name = instance_path.split("/")[-1].replace(".txt","")
        df = run_experiment(instance_path)
        save_results(df, instance_name)
        print(f"Résultats pour {instance_name}:")
        print(df)
        print(f"Tableau CSV sauvegardé dans results/tables/{instance_name}_results.csv")
        print(f"Figure sauvegardée dans results/figures/{instance_name}_comparison.png")
